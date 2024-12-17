import streamlit as st

# Set the title of the web page with the logo beside it
col1, col2 = st.columns([1, 10])
with col1:
    st.image("NATGAS.png", width=100)
with col2:
    st.title("NATGAS Contractors Monthly Dashboard")

# Embed the Power BI dashboard using the provided HTML embed code
power_bi_html = """
<div style="position: relative; width: 100%; height: 0; padding-bottom: 75%;">
    <iframe title="Report Section" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0;"
            src="https://app.powerbi.com/reportEmbed?reportId=91071687-dcbb-433a-a3a3-159775676fce&autoAuth=true&ctid=a86ca211-c918-4c77-8b32-440c27aa3100"
            frameborder="0" allowFullScreen="true"></iframe>
</div>
"""
st.markdown(power_bi_html, unsafe_allow_html=True)

# Add a full-screen button
st.markdown("""
    <button onclick="openFullscreen();">Full Screen</button>
    <script>
    function openFullscreen() {
      var elem = document.querySelector('iframe');
      if (elem.requestFullscreen) {
        elem.requestFullscreen();
      } else if (elem.mozRequestFullScreen) { // Firefox
        elem.mozRequestFullScreen();
      } else if (elem.webkitRequestFullscreen) { // Chrome, Safari and Opera
        elem.webkitRequestFullscreen();
      } else if (elem.msRequestFullscreen) { // IE/Edge
        elem.msRequestFullscreen();
      }
    }
    </script>
    """, unsafe_allow_html=True)

# Add credit for the dashboard creator
st.markdown("""
    <div style='text-align: right;'>
        <p><strong>Created by:</strong> Ibrahim Elnagar, Operation Manager</p>
    </div>
    """, unsafe_allow_html=True)

# Add some styling to make the dashboard take the majority of the screen
st.markdown(
    """
    <style>
    .main .block-container{{
        max-width: 1
