import pandas as pd
import requests
import os

# Skapa en mapp som heter 'data' om den inte redan finns
if not os.path.exists('data'):
    os.makedirs('data')

def download_fi_data():
    print("Startar hämtning från Finansinspektionen...")
    
    # URL:er till FI:s register
    urls = {
        'insyn': "https://marknadssök.fi.se/Publicerat/Insyn/Sök/Register.csv",
        'blankning': "https://marknadssök.fi.se/Publicerat/Blankning/Sök/Register.csv"
    }
    
    for name, url in urls.items():
        try:
            # Vi hämtar datan. FI använder ofta latin-1 eller utf-16
            response = requests.get(url)
            response.encoding = 'utf-16' # Justera vid behov efter test
            
            # Spara som en lokal CSV-fil i mappen 'data'
            file_path = f'data/{name}_current.csv'
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(response.text)
            
            print(f"Lyckades spara {name} till {file_path}")
            
        except Exception as e:
            print(f"Kunde inte hämta {name}: {e}")

if __name__ == "__main__":
    download_fi_data()
