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

with st.expander("See explanation"):
    st.write('''
        Testando as funcionalidades
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
