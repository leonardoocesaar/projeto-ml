import streamlit as st
import pandas as pd
from sklearn .linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")
model = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
model.fit(x, y)


st.title("Preço da Pizza")
st.divider()

diametro = st.number_input("Digite o diametro")

if diametro:
    preco_previsto = model.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza de {diametro:.2f} é de R$ {preco_previsto:.2f}")
    st.balloons()