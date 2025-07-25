import streamlit as st
import requests

st.title("Volleybuk – analizator meczów siatkówki")
st.write("Poniżej znajdziesz ostatnie mecze z Volleyboxa:")

url = "https://volleybox.net/api/matches"
response = requests.get(url)

if response.status_code == 200:
    matches = response.json()
    for match in matches[:10]:  # pokazujemy tylko 10 pierwszych
        home = match.get("home_team", {}).get("name", "Brak")
        away = match.get("away_team", {}).get("name", "Brak")
        result = match.get("result") or "Brak wyniku"
        st.write(f"{home} vs {away} → {result}")
else:
    st.error("Nie udało się pobrać danych z Volleybox 😢")
