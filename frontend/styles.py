import streamlit as st


def load_styles():

    st.markdown(
        """
        <style>
        .stMetric{
            border-radius:10px;
            padding:10px;
            background-color:#f5f5f5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )