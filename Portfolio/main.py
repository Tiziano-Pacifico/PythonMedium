import streamlit as st
import pandas as pd

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
content2 = """
Below you can find some of the apps I have built in python. Feel free to contact me
"""
st.markdown(f"<p style='font-size: 20px;'>{content2}</p>", unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("Files/data.csv", sep=";")
with col3:
 for index, row in df[:10].iterrows():
     st.header(row["title"])
     st.write(row['description'])
     st.image("Files/images/" + row['image'])
     st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("Files/images/" + row['image'])
        st.write(f"[Source code]({row['url']})")