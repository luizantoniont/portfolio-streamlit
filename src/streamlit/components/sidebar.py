# src/components/sidebar.py
import streamlit as st


def create_sidebar():
    """
    Create a consistent sidebar for the application.
    """
    st.sidebar.title("Portfolio Navigation")
    
    # Optional: Skills or tech stack visualization
    st.sidebar.header("Tech Stack")
    skills = [
        "Python", "Machine Learning", "Deep Learning", 
        "Streamlit", "Data Analysis", "Data Visualization"
    ]
    
    for skill in skills:
        # Dummy progress, replace with actual skill levels
        st.sidebar.progress(80)  
        st.sidebar.write(skill)