#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app


# Función main()
def main():
    page_list = ["Home", "EDA", "ML", "Info"]
    page_menu = st.sidebar.selectbox("Menu", page_list)
    
    if page_menu == page_list[0]:
        home_page()
    elif page_menu == page_list[1]:
        run_eda_app()
    elif page_menu == page_list[2]:
        run_ml_app()
    elif page_menu == page_list[3]:
        info_page()


def home_page():
    st.title("Home")
    st.divider()
    st.subheader("App para la deteccion temprana  de DM")
    st.write("Dataset que contiene señales y sintomas que pueden indicar diabetes o posibilidad de diabetes")
    st.subheader("Fuente de datos")
    st.info("https://archive.ics.uci.edu/dataset/529/early+stage+diabetes+risk+prediction+dataset")
    st.subheader("Contenidos de la App")
    st.markdown(
		"""
		* **EDA Section**: Analisis exploratorio de los datos
		* **ML Section**: Prediccion de diabetes basada en ML
    	"""
	)
    
def info_page():
    st.title("Info")
    st.divider()
    st.text("MBIT, consolidation project")
    stc.iframe("https://www.lanacion.com.ar", height=750, scrolling=True)
    
    

if __name__ == '__main__':
	main()