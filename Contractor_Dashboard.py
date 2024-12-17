import streamlit as st

# Set the title of the web page with the logo beside it
col1, col2 = st.columns([1, 10])
with col1:
    st.image("NATGAS.png", width=200)
with col2:
    st.title("NATGAS Contractors Monthly Dashboard")

# Add credit for the dashboard creator
st.markdown("""
    <div style='text-align: right;'>
        <p><strong>Created by:</strong> Ibrahim Elnagar, Operation Manager</p>
    </div>
    """, unsafe_allow_html=True)

# Embed the Power BI dashboard
power_bi_url = "https://app.powerbi.com/view?r=your_power_bi_dashboard_url"
st.markdown(f'<iframe width="100%" height="800" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

# Add some styling to make the dashboard take the majority of the screen
st.markdown(
    """
    <style>
    .main .block-container{{
        max-width: 100%;
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
