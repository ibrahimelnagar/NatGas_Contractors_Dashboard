import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Natgas Contractors Monthly Dash-board")
st.image("NATGAS.png", width=120,)

st.title("Natgas Contractors Monthly Dash-board")
components.iframe("https://app.powerbi.com/reportEmbed?reportId=91071687-dcbb-433a-a3a3-159775676fce&autoAuth=true&ctid=a86ca211-c918-4c77-8b32-440c27aa3100", width=800, height=600)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
