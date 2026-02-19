# InsynDirekt
Hemsida där du snabbt och enkelt får överskådlig information om insynshandel och blankningspositioner i börsnoterade bolag.
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="InsynDirekt", layout="wide")

st.title("🔍 InsynDirekt")
st.subheader("Din genväg till börsens insiders och blankare")

# Funktion för att läsa den sparade datan
def load_local_data():
    insyn_path = 'data/insyn_current.csv'
    blank_path = 'data/blankning_current.csv'
    
    insyn_df = pd.DataFrame()
    blank_df = pd.DataFrame()
    
    if os.path.exists(insyn_path):
        insyn_df = pd.read_csv(insyn_path)
    if os.path.exists(blank_path):
        blank_df = pd.read_csv(blank_path)
        
    return insyn_df, blank_df

insyn_data, blank_data = load_local_data()

# Sökruta
ticker = st.text_input("Sök på bolag (t.ex. Securitas):").upper()

if ticker:
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("### Senaste Insynshandel")
        # Här filtrerar vi på bolagsnamn (Utgivare)
        if not insyn_data.empty:
            res = insyn_data[insyn_data['Utgivare'].str.contains(ticker, case=False, na=False)]
            st.dataframe(res)
        else:
            st.info("Ingen data laddad ännu. Roboten körs i natt!")

    with col2:
        st.write("### Aktuell Blankning")
        if not blank_data.empty:
            res_b = blank_data[blank_data['Emittent'].str.contains(ticker, case=False, na=False)]
            st.dataframe(res_b)
        else:
            st.info("Ingen data hittades.")

st.divider()
st.caption("Data hämtas automatiskt från Finansinspektionen varje natt via InsynDirekt-botten.")
