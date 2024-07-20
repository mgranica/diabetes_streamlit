# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

file_path = "data/diabetes_data_upload.csv"
file_path_clean = "data/diabetes_data_upload_clean.csv"
sub_menu_list = ["Descriptive", "Graph"]
# Función principal que emplearemos en la APP
def run_eda_app():
    st.header("EDA Section")
    st.divider()
    # sub menu select box
    sub_menu = st.sidebar.selectbox("SubMenu", sub_menu_list)
    # read dfs
    df = pd.read_csv(file_path)
    df_clean = pd.read_csv(file_path_clean)
    # Descriptive analysis
    if sub_menu == sub_menu_list[0]:
        st.subheader("Descirptive analysis")
        st.dataframe(df)
        # Data type
        with st.expander("data type"):
            st.write(df.dtypes.astype(str))
        # Descriptive summary
        with st.expander("Descriptive summary"):
            st.write(df_clean.describe(include='all'))
        # Gender distribution
        with st.expander("Gender distribution"):
            st.write(df["Gender"].value_counts())
        # Class distribution
        with st.expander("Class distribution"):
            st.write(df["class"].value_counts())
    # Graph analysis
    elif sub_menu == sub_menu_list[1]:
        st.subheader("Graph analysis")
        col1, col2 = st.columns([3,1])
        with col1:
            with st.expander("Gender Distribution Graph"):
                fig1 = go.Figure()
                fig1.add_trace(go.Histogram(x=df["Gender"], name="Gender"))
                st.plotly_chart(fig1)
            with st.expander("Class Distribution Graph"):
                fig2 = go.Figure()
                fig2.add_trace(go.Histogram(x=df["class"], name="Class"))
                st.plotly_chart(fig2)
        with col2:
            # Gender distribution
            with st.expander("Gender distribution"):
                st.write(df["Gender"].value_counts())
            # Class distribution
            with st.expander("Class distribution"):
                st.write(df["class"].value_counts())
        with st.expander("Age distribution"):
            fig3 = go.Figure()
            fig3.add_trace(
                go.Histogram(
                    x=df["Age"], 
                    xbins=dict(
                        # start=min(df['Age']),
                        # end=max(df['Age']),
                        size=10  # Bin size of 10 years
                    ),
                    name="Age")
            )
            st.plotly_chart(fig3)
        with st.expander("Outlier detection"):
            fig4 = go.Figure()
            # Add box plot for each gender
            for gender in df['Gender'].unique():
                fig4.add_trace(go.Box(
                    y=df[df['Gender'] == gender]['Age'],
                    name=gender,
                #boxmean='sd'
                ))
            st.plotly_chart(fig4)
        with st.expander("Correlation Heatmap"):
            # Compute the correlation matrix
            correlation_matrix = df_clean.corr()
            fig5 = go.Figure()
            fig5.add_trace(
                go.Heatmap(
                    z=correlation_matrix.values,
                    x=correlation_matrix.columns,
                    y=correlation_matrix.columns,  # Both axes should use column names
                    colorscale='Viridis',  # Color scale for the heat map
                    colorbar=dict(title='Correlation'),  # Color bar title
                    text=correlation_matrix.round(2).values,  # Cell values as text annotations
                    texttemplate='%{text}',  # Format the text annotations
                    #textfont=dict(size=12, color='white')  # Font size and color of text
				)
            )
            st.plotly_chart(fig5)
            
        
    # Todo el código a escribir va aquí






# Fin de la FUNCION







