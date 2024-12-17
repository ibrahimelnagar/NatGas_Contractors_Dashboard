import streamlit as st

# Page configuration
st.set_page_config(page_title="Natgas Contractors Monthly Dashboard")

# Display logo
st.image("NATGAS.png", width=120)

# Page title
st.title("Natgas Contractors Monthly Dashboard")

# Add a clickable link to the Power BI dashboard
st.write("[Click here to view the dashboard](https://app.powerbi.com/groups/me/reports/91071687-dcbb-433a-a3a3-159775676fce)")

# Hide Streamlit's default styling
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
