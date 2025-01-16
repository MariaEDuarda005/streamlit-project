import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Meu site"
)

# Inicializa a conexão com o banco de dados
conn = st.connection('mysql', type='sql')

# Função para carregar os dados
@st.cache_data(ttl=600)
def carregar_dados():
    query = "SELECT Data, Contratos FROM resultados.informacao;"
    dados = conn.query(query)
    return dados

with st.container():
    st.subheader("Meu primeiro site")
    st.title("Dashboards de contratos")
    st.write("Informações sobre os contratos pela Empresa ao longo de maio")
    st.write("Para conhecer mais sobre o Streamlit? [Clique aqui](https://docs.streamlit.io/)")

with st.container():
    st.write("---")

    #Botão de selecionar
    qtde_dias = st.selectbox("Selecione o periodo", ["All", "7D", "15D", "21D", "30D"])

    dados = carregar_dados()

    if qtde_dias != "All":
        num = int(qtde_dias.replace("D", ""))
        dados = dados[-num:] # o "-" para ele pegar de trás pra frente, e os : para pegar todos os 7,15, e assim por diante
    else:
        st.write("Exibindo todos os dados")

    st.line_chart(dados, x="Data", y="Contratos")
    st.bar_chart(dados, x="Data", y="Contratos")



