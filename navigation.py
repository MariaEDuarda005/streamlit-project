import streamlit as st 

pages = {
    "Information": [
        st.Page("meu_app.py", title="Dashboard de contratos"),
        st.Page("details.py", title="Detalhes dos contratos"),
    ]
}

pg = st.navigation(pages)
pg.run()