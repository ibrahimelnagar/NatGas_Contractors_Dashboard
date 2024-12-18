import streamlit as st

# Set the page configuration for better layout and experience
st.set_page_config(page_title="NATGAS Contractors Dashboard", layout="wide")

# Create a layout with a logo and title side-by-side
col1, col2 = st.columns([1, 10])
with col1:
    st.image("NATGAS.png", width=100)
with col2:
    st.title("NATGAS Contractors Monthly Dashboard")

# Embed the Power BI dashboard with an iframe, styled for responsiveness
power_bi_html = """
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
    <iframe id="dashboardFrame" 
            title="Report Section" 
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
            src="https://app.powerbi.com/reportEmbed?reportId=91071687-dcbb-433a-a3a3-159775676fce&autoAuth=true&ctid=a86ca211-c918-4c77-8b32-440c27aa3100" 
            frameborder="0" 
            allowfullscreen>
    </iframe>
</div>
"""
st.markdown(power_bi_html, unsafe_allow_html=True)

# Add a button for users to toggle full-screen mode
st.markdown("""
    <div style="text-align: right; margin-top: 10px;">
        <button onclick="toggleFullScreen()" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;">
            Full Screen
        </button>
    </div>
    <script>
    function toggleFullScreen() {{
        var iframe = document.getElementById("dashboardFrame");
        if (iframe.requestFullscreen) {{
            iframe.requestFullscreen();
        }} else if (iframe.mozRequestFullScreen) {{ /* Firefox */
            iframe.mozRequestFullScreen();
        }} else if (iframe.webkitRequestFullscreen) {{ /* Chrome, Safari & Opera */
            iframe.webkitRequestFullscreen();
        }} else if (iframe.msRequestFullscreen) {{ /* IE/Edge */
            iframe.msRequestFullscreen();
        }}
    }}
    </script>
    """, unsafe_allow_html=True)

# Add credit for the dashboard creator with improved styling
st.markdown("""
    <div style='text-align: right; margin-top: 20px; font-size: 14px; color: #555;'>
        <p><strong>Created by:</strong> Ibrahim Elnagar, Operation Manager</p>
    </div>
    """, unsafe_allow_html=True)

# Styling to ensure the dashboard fits the page width
st.markdown("""
    <style>
    .main .block-container {
        max-width: 100%;
        padding: 2rem 1rem;
    }
    </style>
    """, unsafe_allow_html=True)
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

