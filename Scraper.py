import pandas as pd
import requests
import io
import os

def download_fi_data():
    url = "https://marknadssok.fi.se/Publicerat/Insyn/Sok/Register.csv"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        if response.status_code == 200:
            # Vi testar att avkoda
            raw_data = response.content.decode('utf-16')
            df = pd.read_csv(io.StringIO(raw_data), sep=';')
            
            # Här tvingar vi fram sparandet i den mapp roboten jobbar i
            file_path = os.path.join(os.getcwd(), 'insyn_data.csv')
            df.to_csv(file_path, index=False, encoding='utf-8')
            
            print(f"SUCCÉ: Sparade {len(df)} rader till {file_path}")
        else:
            print(f"FEL: Kunde inte hämta data, statuskod: {response.status_code}")
    except Exception as e:
        print(f"FEL vid körning: {e}")

if __name__ == "__main__":
    download_fi_data()
