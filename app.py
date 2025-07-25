import streamlit as st
import random

st.title("Volleybuk – analizator meczów siatkówki")

st.write("Wprowadź nazwy dwóch drużyn, które chcesz porównać:")

# 📥 Pola tekstowe
team_1 = st.text_input("Drużyna 1")
team_2 = st.text_input("Drużyna 2")

# 🔘 Przycisk
if st.button("Analizuj"):
    if team_1 and team_2:
        st.success(f"Analizuję: {team_1} vs {team_2} 🔍")

        # 🔢 Testowa analiza — symulowana logika
        form_team_1 = random.randint(0, 100)
        form_team_2 = random.randint(0, 100)

        st.write(f"📊 Forma {team_1}: {form_team_1}/100")
        st.write(f"📊 Forma {team_2}: {form_team_2}/100")

        if form_team_1 > form_team_2:
            st.write(f"🔮 Typ: Zwycięstwo **{team_1}**")
        elif form_team_2 > form_team_1:
            st.write(f"🔮 Typ: Zwycięstwo **{team_2}**")
        else:
            st.write("🤷 Remis niemożliwy w siatkówce – coś poszło dziwnie 😅")

        st.write("⚠️ To tylko testowy wynik — prawdziwa analiza będzie później.")
    else:
        st.warning("Podaj obie drużyny, żeby rozpocząć analizę.")
