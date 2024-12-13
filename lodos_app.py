# Import Python Libraries
import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import plotly.express as px
from PIL import Image
from collections import namedtuple
from math import radians, isclose, acos, asin, cos, sin, tan, atan, degrees, sqrt


# Insert an icon
icon = Image.open("resource/slb.png")

# State the design of the app
st.set_page_config(page_title="DE App", page_icon=icon)

# Insert css codes to improve the design of the app
st.markdown(
    """
<style>
h1 {text-align: center;
}
body {background-color: #DCE3D5;
      width: 1400px;
      margin: 15px auto;
}
footer {
  display: none;
}
</style>""",
    unsafe_allow_html=True,
)


# Insert title for app
st.title("Lodos de Perforación App")
st.write("---")

# Add information of the app
st.markdown(
    """
    Los lodos de perforación se utilizan en la perforación de pozos para lubricar y enfriar la broca, remover los recortes de perforación y mantener la estabilidad del pozo. Sus actividades incluyen la preparación de la mezcla, el monitoreo continuo de sus propiedades y la gestión de residuos.

    **Python:** Pandas, Numpy, Streamlit, PIL, Plotly."""
)

# Add additional information
expander = st.expander("Información")
expander.write(
    "La aplicación web para la gestión de lodos de perforación tiene varias funcionalidades clave. Los usuarios pueden registrar y monitorear las propiedades de los lodos, como la densidad, viscosidad y contenido de sólidos."
)


# Insert Image
image = Image.open("resource/lodos-de-perforacion.jpg")
st.image(image, width=100, use_container_width=True)

# Insert subheader
st.subheader("**Fundamentos de los lodos de perforación**")


# Insert video
video = open("resource/lodos.mp4", "rb")
st.video(video)


# Insert caption
st.caption("*Video sobre lodos de perforación*")


# Sidebar section
logo = Image.open("resource/SLB_Logo_White.png")
st.sidebar.image(logo)


# Add title to the sidebar section
st.sidebar.title("⬇ Navegador")

# Upload files
file = st.sidebar.file_uploader("Carga tu archivo csv")


# Add sections of the app
with st.sidebar:
    options = option_menu(
        menu_title="Menu",
        options=["Home", "Data", "3D Plots", "Basic Calculations"],
        icons=["house", "clipboard2-data", "badge-3d-fill", "activity"],)

