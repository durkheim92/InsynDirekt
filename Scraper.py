import pandas as pd
import requests
import io
import os

def get_data():
    # FI:s server kräver exakt dessa stora/små bokstäver för att inte ge 404
    url = "https://marknadssok.fi.se/Publicerat/Insyn/Sök/Register.csv"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/csv'
    }
    
    print(f"Startar hämtning från: {url}")
    
    try:
        # Vi använder timeout ifall FI är sega
        response = requests.get(url, headers=headers, timeout=60)
        
        if response.status_code == 200:
            print("Lyckades ansluta till FI!")
            
            # Vi testar först den kodning som FI brukar använda (utf-16)
            try:
                content = response.content.decode('utf-16')
            except:
                content = response.content.decode('utf-8-sig') # 'sig' hjälper med svenska tecken
            
            # De använder semikolon som separator
            df = pd.read_csv(io.StringIO(content), sep=';')
            
            # Spara filen som appen läser
            df.to_csv('insyn_data.csv', index=False, encoding='utf-8')
            print(f"KLART: Sparade {len(df)} rader!")
            
        else:
            print(f"FEL: FI svarade med statuskod {response.status_code}")
            print("Tips: Testa att ändra URL till stora/små bokstäver om det står 404.")
            
    except Exception as e:
        print(f"KRITISKT FEL: {str(e)}")

if __name__ == "__main__":
    get_data()
