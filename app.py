import streamlit as st
import requests

st.title("Test połączenia z Volleybox API")

url = "https://volleybox.net/api/matches"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        st.success("Połączenie z Volleybox działa! ✅")
        st.write("Przykładowy mecz:")
        st.json(data[0])  # pokazujemy tylko pierwszy mecz jako test
    else:
        st.error(f"Volleybox API zwrócił kod: {response.status_code}")
except Exception as e:
    st.error(f"Błąd połączenia z Volleybox: {e}")
