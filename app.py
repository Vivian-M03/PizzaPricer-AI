import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

## Criando o app

# Interface do Usuário
st.markdown("<h2 style='text-align: center; color: #E63946;'>🍕 Calculadora de Preço da Pizza 🍕</h2>", unsafe_allow_html=True)
st.divider()

st.markdown("### 📏 Escolha o diâmetro da sua pizza:")
diametro_pizza = st.slider("Tamanho da pizza (cm):", min_value=int(df["diametro"].min()), max_value=int(df["diametro"].max()), step=1)

# Previsão e exibição do resultado
if diametro_pizza:
    preco_previsto = modelo.predict([[diametro_pizza]])[0][0]

    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        st.success(f"💰 O valor estimado da pizza de {diametro_pizza} cm é **R${preco_previsto:.2f}**!")

fig, ax = plt.subplots(figsize=(5, 3))
ax.scatter(df["diametro"], df["preco"], color="blue", label="Dados reais")
ax.plot(np.array(df["diametro"]), modelo.predict(df[["diametro"]]), color="red", linestyle="--", label="Regressão Linear")
ax.set_xlabel("Diâmetro da Pizza (cm)")
ax.set_ylabel("Preço (R$)")
ax.set_title("Relação entre Diâmetro e Preço da Pizza")
ax.legend()

st.pyplot(fig) 

st.markdown("<p style='text-align: center; color: gray;'>Desenvolvido por Vivian Franco!</p>", unsafe_allow_html=True)


