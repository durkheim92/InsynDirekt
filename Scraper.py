import pandas as pd
import requests
import os
import io

# Skapa mappen 'data' om den inte redan finns
if not os.path.exists('data'):
    os.makedirs('data')

def download_fi_data():
    print("Startar hämtning från Finansinspektionen...")
    
    # URL till FI:s register för insynshandel
    url = "https://marknadssök.fi.se/Publicerat/Insyn/Sök/Register.csv"
    
    try:
        # Hämta datan
        response = requests.get(url)
        # FI kör ofta utf-16, vi avkodar det här
        raw_data = response.content.decode('utf-16')
        
        # Läs in i Pandas (detta gör det lättare att hantera i Streamlit sen)
        df = pd.read_csv(io.StringIO(raw_data), sep=';')
        
        # Spara filen i rätt mapp för roboten
        file_path = 'data/insyn_current.csv'
        df.to_csv(file_path, index=False, encoding='utf-8')
        
        print(f"Lyckades spara data till {file_path}")
        print(f"Antal rader hämtade: {len(df)}")
            
    except Exception as e:
        print(f"Något gick fel vid hämtningen: {e}")

if __name__ == "__main__":
    download_fi_data()
