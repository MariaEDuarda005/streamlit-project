import streamlit as st
import pandas as pd

# Teste para estilizar
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder


st.title("Detalhes dos contratos")

# Inicializa a conexão com o banco de dados
conn = st.connection('mysql', type='sql')

@st.cache_data(ttl=600)
def carregar_dados():
    query = "SELECT * FROM resultados.informacao;"
    dados = conn.query(query)
    
    # Formatar a data
    dados["Data"] = pd.to_datetime(dados["Data"]).dt.strftime("%d/%m/%Y")

    # Deixar como número
    dados["Contratos"] = pd.to_numeric(dados["Contratos"], errors='coerce')

    return dados

dados = carregar_dados()

# Verificar se os dados foram carregados corretamente
if not dados.empty:
    
    st.header("Tabela de Contratos")

    # Criar configurações do AgGrid
    gd = GridOptionsBuilder.from_dataframe(dados)

    grid_options = gd.build()

    # Renderizar tabela usando AgGrid
    AgGrid(
        dados,
        gridOptions=grid_options,
        theme="balham",  # Temas para estilizar: "streamlit", "light", "dark", "balham", "material"
        height=400, 
        fit_columns_on_grid_load=True,  # Ajustar as colunas
    )

else:
    st.error("Nenhum dado encontrado no banco de dados.")

with st.container():

    # Calcular soma de contratos por pessoa
    soma_contratos = dados.groupby("Nome")["Contratos"].sum().reset_index()
    soma_contratos = soma_contratos.sort_values(by="Contratos", ascending=False)

    with st.container(border=True):

        st.subheader("Análise dos Contratos")
        
        for index, row in soma_contratos.iterrows():
            st.write(f"{row['Nome']}: {row['Contratos']} contratos")

        maior_responsavel = soma_contratos.iloc[0]
        st.write(f"A pessoa com mais contratos no mês de março é {maior_responsavel['Nome']} com {maior_responsavel['Contratos']} contratos.")
   

with st.expander("See explanation"):
    st.write('''
        Testando as funcionalidades
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
