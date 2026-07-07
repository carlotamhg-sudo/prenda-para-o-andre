import streamlit as st
from PIL import Image
import time

# Configuração da página para parecer profissional na aba do browser
st.set_page_config(page_title="Presente especial", page_icon="🎁")

# Título e texto enganadores
st.title("Mensagem Especial da beta! 🎉")
st.write("Temos uma surpresa preparada especialmente para ti para celebrar o teu excelente trabalho recente e por não transformares a Agência numa mercearia.")

# Espaçamento para criar suspense
st.write("Fofoca fresca")

# O botão do "Click bait"
if st.button("Clica aqui para abrires a tua surpresa", type="primary"):
    
    # Um pequeno loading falso para aumentar a ansiedade
    with st.spinner('A carregar a tua surpresa...'):
        time.sleep(2)
    
    # A revelação brutal
    st.success("Surpresa carregada com sucesso!")
    
    try:
        imagem = Image.open('WhatsApp Image 2026-07-07 at 19.22.53.jpeg')
        c1, c2, c3 = st.columns([1, 2, 1]) 
        with c2:
            # st.image agora usa container_width=False e um tamanho fixo (width=300)
            st.image(imagem, caption="Com muito carinho! 😂", width=300)
    except FileNotFoundError:
        st.error("Erro: Não te esqueças de guardar a foto na mesma pasta com o nome 'surpresa.jpg'!")
        
    st.balloons() # Balões para adicionar ao sarcasmo
