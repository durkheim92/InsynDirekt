import pandas as pd
import requests
import io
import os

def get_data():
    # Vi använder den säkraste versionen av URL:en
    url = "https://marknadssok.fi.se/publicerat/insyn/sok/register.csv"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/csv'
    }
    
    print(f"Startar hämtning från: {url}")
    
    try:
        # Vi sätter timeout till 60 sekunder om FI:s server är seg
        response = requests.get(url, headers=headers, timeout=60)
        
        if response.status_code == 200:
            print("Lyckades ansluta till FI!")
            
            # FI skickar ofta data i utf-16. Vi testar det först.
            try:
                content = response.content.decode('utf-16')
            except:
                content = response.content.decode('utf-8')
            
            # Skapa dataframe. FI använder semikolon (;) som separator
            df = pd.read_csv(io.StringIO(content), sep=';')
            
            # Spara ner filen i huvudmappen
            df.to_csv('insyn_data.csv', index=False, encoding='utf-8')
            print(f"KLART: Sparade {len(df)} rader till insyn_data.csv")
            
        else:
            print(f"FEL: FI svarade med statuskod {response.status_code}")
            
    except Exception as e:
        print(f"KRITISKT FEL: {str(e)}")

if __name__ == "__main__":
    get_data()
