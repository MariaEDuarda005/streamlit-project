import streamlit as st


st.title("Detalhes dos contratos")

# Inicializa a conexão com o banco de dados
conn = st.connection('mysql', type='sql')

# Função para carregar os dados
@st.cache_data(ttl=600)
def carregar_dados():
    query = "SELECT * FROM resultados.informacao;"
    dados = conn.query(query)
    return dados

dados = carregar_dados()

# Verificar se os dados foram carregados corretamente
if not dados.empty:
    st.header("Tabela de Contratos")
    st.dataframe(dados)  # Exibe todos os dados em formato de tabela interativa
else:
    st.error("Nenhum dado encontrado no banco de dados.")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("Data")
#     st.write(dados["Data"])
 

# with col2:
#     st.header("Contratos")
#     st.write(dados["Contratos"])

# with col3:
#     st.header("Nomes dos Responsaveis")
#     st.write(dados["Nome"])

