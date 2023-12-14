import streamlit as st
import random

st.title("Pedra, Papel e Tesoura")
st.text("Vamos jogar? Veja se consegue me vencer!")

opcoes = ['Pedra', 'Papel', 'Tesoura']
jogador = st.radio("Escolha sua arma: ", opcoes)

if st.button("JOGAR"):
    computador = random.choice(opcoes)

    st.text(f"O computador escolheu: {computador}")

    if jogador == computador:
        st.title("Empate!")
    elif (jogador == 'Pedra' and computador == 'Tesoura') or (jogador == 'Papel' and computador == 'Pedra') or (jogador == 'Tesoura' and computador == 'Papel'):
        st.title("Você venceu!")
    else:
        st.title("O computador venceu!")