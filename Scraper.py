import pandas as pd
import requests
import io
import os

def download_fi_data():
    # Denna URL ser konstig ut, men det är den enda som funkar säkert på GitHub
    url = "https://marknadssok.fi.se/Publicerat/Insyn/Sok/Register.csv"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/csv'
    }
    
    try:
        print(f"Anropar FI: {url}")
        response = requests.get(url, headers=headers, timeout=60)
        
        if response.status_code == 200:
            # Finansinspektionen använder ofta utf-16le för sina CSV-filer
            try:
                raw_data = response.content.decode('utf-16')
            except:
                raw_data = response.content.decode('utf-8')
            
            df = pd.read_csv(io.StringIO(raw_data), sep=';')
            
            # Spara filen
            file_path = 'insyn_data.csv'
            df.to_csv(file_path, index=False, encoding='utf-8')
            print(f"SUCCÉ: Hämtade {len(df)} rader!")
        else:
            print(f"FEL: FI svarade med kod {response.status_code}")
            # Om vi får 404 här, så vet vi att adressen måste justeras igen
            
    except Exception as e:
        print(f"FEL vid körning: {str(e)}")

if __name__ == "__main__":
    download_fi_data()
