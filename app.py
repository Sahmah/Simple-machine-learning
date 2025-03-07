import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza!")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da pizza em cm: ", min_value=0, max_value=1000)

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor previsto para a pizza de {diametro} cm é R$ {preco_previsto:.2f}.")  
    st.balloons()