import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="InsynDirekt", layout="wide")

st.title("🔍 InsynDirekt")
st.write("Här kan du söka efter insynshandel och blankning direkt från FI:s register.")

# Kolla om datan finns
file_path = 'data/insyn_current.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    search_term = st.text_input("Sök på bolag eller person:")
    
    if search_term:
        # Filtrera datan (vi antar att kolumnen heter 'Utgivare' - justera vid behov)
        filtered_df = df[df.apply(lambda row: search_term.lower() in row.astype(str).str.lower().values, axis=1)]
        st.write(filtered_df)
    else:
        st.write(df.head(20))
else:
    st.warning("Hittade ingen data ännu. Kör roboten på GitHub Actions först!")
