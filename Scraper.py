import pandas as pd
import requests
import io

def download_fi_data():
    url = "https://marknadssök.fi.se/Publicerat/Insyn/Sök/Register.csv"
    print(f"Försöker hämta data från: {url}")
    
    try:
        # Vi lägger till en 'User-Agent' så FI inte tror att vi är en elak bot
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=30)
        
        # Kolla om vi faktiskt fick svar
        if response.status_code == 200:
            print("Lyckades hämta data, avkodar...")
            # Testa utf-16 först, annars utf-8
            try:
                raw_data = response.content.decode('utf-16')
            except:
                raw_data = response.content.decode('utf-8')
                
            df = pd.read_csv(io.StringIO(raw_data), sep=';')
            df.to_csv('insyn_data.csv', index=False, encoding='utf-8')
            print("KLART: Filen 'insyn_data.csv' har skapats!")
        else:
            print(f"FEL: FI svarade med statuskod {response.status_code}")
            
    except Exception as e:
        print(f"OVÄNTAT FEL: {str(e)}")

if __name__ == "__main__":
    download_fi_data()
