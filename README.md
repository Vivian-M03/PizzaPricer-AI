# 📌 Projeto: FIRST_PROJECT-ML

## 📖 Descrição
Este projeto utiliza **Machine Learning** para prever o preço de pizzas com base no diâmetro. A implementação é feita em **Python**, utilizando as bibliotecas **pandas, scikit-learn, streamlit e matplotlib**. O objetivo é criar um modelo de regressão linear e disponibilizar uma interface interativa para a previsão de preços.

---

## 🛠 Configuração do Ambiente
### 1️⃣ Criar o ambiente virtual e instalar dependências
```sh
# Criar um novo projeto com Poetry
test -d first_project-ml || poetry new first_project-ml
cd first_project-ml

# Criar e ativar o ambiente virtual
poetry shell

# Instalar dependências
poetry add pandas scikit-learn streamlit matplotlib
```

### 2️⃣ Abrir o projeto no VS Code
```sh
code .
```

---

## 🚀 Desenvolvimento
### 1️⃣ Exploração de Dados (Notebook Jupyter - `teste.ipynb`)
- Importar **pandas** e carregar o dataset `pizzas.csv`.
- Criar um **gráfico de dispersão** para visualizar a relação entre **diâmetro** e **preço**.
- Aplicar um modelo de **Regressão Linear** para prever o preço com base no diâmetro.
- Utilizar `.predict()` para testar previsões.

### 2️⃣ Implementação do Web App (`app.py`)
- Criar um aplicativo com **Streamlit**.
- Importar bibliotecas e carregar o modelo treinado.
- Criar interface interativa para entrada do diâmetro da pizza.
- Exibir o preço previsto e um **gráfico dinâmico**.

### 3️⃣ Rodar o Web App
```sh
streamlit run app.py
```
## 📸 Resultado Final

Aqui está uma prévia do funcionamento do aplicativo:

<img src= https://github.com/Vivian-M03/PizzaPricer-AI/blob/main/webvisualizer.png>
---

## 📂 Estrutura do Projeto
```
first_project-ml/
├── .venv/               # Ambiente virtual
├── src/                 # Códigos fonte
├── tests/               # Testes unitários
├── app.py               # Aplicativo principal (Streamlit)
├── pizzas.csv           # Base de dados
├── poetry.lock          # Dependências do projeto
├── pyproject.toml       # Configuração do Poetry
├── README.md            # Documentação do projeto
├── teste.ipynb          # Análise exploratória (Jupyter Notebook)
```

---

## Tecnologias Utilizadas
- **Python** 
- **pandas** 
- **scikit-learn** 
- **matplotlib** 
- **Streamlit** 
- **Poetry** 

---

#Autor
Projeto desenvolvido por **Vivian Franco**.

