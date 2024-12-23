import streamlit as st

# Set the page configuration for better layout and experience
st.set_page_config(page_title="NATGAS Contractors Dashboard", layout="wide")

# Create a layout with a logo and title side-by-side
col1, col2 = st.columns([1, 10])
with col1:
    st.image("NATGAS.png", width=100)
with col2:
    st.title("NATGAS Contractors Monthly Dashboard")

# Add a fullscreen button at the top of the page
full_screen_button = """
<div style="text-align: right; margin-bottom: 10px;">
    <button onclick="toggleFullScreen()" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;">
        Full Screen
    </button>
</div>
<script>
function toggleFullScreen() {
    var iframe = document.getElementById("dashboardFrame");
    if (iframe.requestFullscreen) {
        iframe.requestFullscreen();
    } else if (iframe.mozRequestFullScreen) { /* Firefox */
        iframe.mozRequestFullScreen();
    } else if (iframe.webkitRequestFullscreen) { /* Chrome, Safari & Opera */
        iframe.webkitRequestFullscreen();
    } else if (iframe.msRequestFullscreen) { /* IE/Edge */
        iframe.msRequestFullscreen();
    }
}
</script>
"""
st.markdown(full_screen_button, unsafe_allow_html=True)

# Embed the updated Looker Studio dashboard with improved sizing
looker_studio_html = """
<div style="position: relative; padding-bottom: 75%; height: 0; overflow: hidden;">
    <iframe id="dashboardFrame"
            title="Google Looker Studio Dashboard"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;"
            src="https://lookerstudio.google.com/embed/reporting/54ea8915-7b41-4e0a-8ed2-2f00c48cfd77/page/flEaE"
            frameborder="0"
            allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox">
    </iframe>
</div>
"""
st.markdown(looker_studio_html, unsafe_allow_html=True)

# Display a warning message about cookies
st.warning("If the dashboard does not load, please enable third-party cookies in your browser.")

# Provide a direct link to the dashboard
st.markdown("[Click here to view the dashboard directly](https://lookerstudio.google.com/reporting/54ea8915-7b41-4e0a-8ed2-2f00c48cfd77/page/flEaE)")

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

# Hide Streamlit's default menu and footer
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)
