import pandas as pd
import requests
import io

def download_fi_data():
    print("Startar hämtning...")
    url = "https://marknadssök.fi.se/Publicerat/Insyn/Sök/Register.csv"
    
    try:
        response = requests.get(url)
        # FI:s format är ofta utf-16 och använder semikolon
        raw_data = response.content.decode('utf-16')
        df = pd.read_csv(io.StringIO(raw_data), sep=';')
        
        # Vi sparar den direkt i huvudmappen så roboten garanterat ser den
        df.to_csv('insyn_data.csv', index=False, encoding='utf-8')
        print("Filen sparad som insyn_data.csv")
            
    except Exception as e:
        print(f"Fel: {e}")

if __name__ == "__main__":
    download_fi_data()
