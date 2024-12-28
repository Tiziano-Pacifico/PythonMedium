import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("Files/images/photo.png", width=500)

with col2:
    st.title("Tiziano Pacifico")
    content = """
        Sono troppo bravo troppo figo. Mi piaccio un sacco e farò grandi cose nella vita. Voglio essere libero e girare il mondo
        , non mi stressate troppo grazie e a presto
    """
    st.info(content)

st.markdown("<p style='font-size: 20px;'>Below you can find some of the apps I have built in python. Feel free to contact me</p>", unsafe_allow_html=True)