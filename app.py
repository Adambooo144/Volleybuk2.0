import streamlit as st

st.title("Volleybuk – analizator meczów siatkówki")

st.write("Wprowadź nazwy dwóch drużyn, które chcesz porównać:")

# 📥 Pola tekstowe na drużyny
team_1 = st.text_input("Drużyna 1")
team_2 = st.text_input("Drużyna 2")

# 🚀 Przycisk
if st.button("Analizuj"):
    if team_1 and team_2:
        st.success(f"Analizuję: {team_1} vs {team_2} 🔍")
        # tu potem wrzucimy algorytm
    else:
        st.warning("Podaj obie drużyny, żeby rozpocząć analizę.")
