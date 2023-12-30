import streamlit as st
import sqlite3

# Aplicação Streamlit
# Função para cadastrar referencia
def cadastrar_referencia(autora, referencia, capitulo, aula):
    conn = sqlite3.connect('referencia.db')
    c = conn.cursor()
    c.execute("INSERT INTO referencia (autora, referencia, capitulo, aula) VALUES (?, ?, ?, ?)", (autora, referencia, capitulo, aula))
    conn.commit()
    conn.close()
    st.success('referencia cadastrada com sucesso!')

st.title(' Encontre a referencia para aula -       use letras MAIUSCULAS para localizar autora')

# Cadastro de referencia na barra lateral (sidebar)
st.sidebar.header('Cadastrar nova referencia')
autora = st.sidebar.text_input('autora')
referencia = st.sidebar.text_input('referência')
capitulo = st.sidebar.text_input('capitulo')
aula = st.sidebar.text_input('aula')

if st.sidebar.button('Cadastrar referencia'):
    cadastrar_referencia(autora, referencia, capitulo, aula)

 # Busca de referencia por autora ou referencia
filtro = st.radio('Filtrar por:', ('autora', 'referencia'))

if filtro == 'autora':
    autora_input = st.text_input('Digite a autora para encontrar referencias')
    if st.button('Buscar por autora'):
        conn = sqlite3.connect('referencia.db')
        c = conn.cursor()
        c.execute("SELECT * FROM referencia WHERE autora=?", (autora_input,))
        referencias_encontradas = c.fetchall()
        conn.close()

        if referencias_encontradas:
            st.header('referencias encontradas pela autora:')
            for referencia in referencias_encontradas:
                st.write(f"autora: {referencia[1]}, referencia: {referencia[2]}, capitulo: {referencia[3]}, aula: {referencia[4]}")
        else:
            st.warning('Nenhuma referencia encontrada para esta autora.')

else:  # Busca por Referencia
    referencia_input = st.text_input('Digite a referência para encontrar texto')
    if st.button('Buscar por referencia'):
        conn = sqlite3.connect('referencia.db')
        c = conn.cursor()
        c.execute("SELECT * FROM referencia WHERE referencia=?", (referencia_input,))
        referencias_por_referencia = c.fetchall()
        conn.close()

        if referencias_por_referencia:
            st.header(f'referencias encontradas: {referencia_input}')
            for referencia in referencias_por_referencia:
                st.write(f"autora: {referencia[1]}, referencia: {referencia[2]}, capitulo: {referencia[3]}, aula: {referencia[4]}")
        else:
            st.warning(f'Nenhuma referencia encontrada: {referencia_input}.')
