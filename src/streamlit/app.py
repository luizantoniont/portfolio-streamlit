# src/app.py
import streamlit as st
from components.sidebar import create_sidebar
from components.home import render_home
from components.projects import render_projects


def main():
    """
    Main Streamlit application entry point.
    Manages page navigation and overall app structure.
    """
    # Configure page settings
    st.set_page_config(
        page_title="Data Scientist Portfolio",
        page_icon=":briefcase:",
        layout="wide"
    )

    # Create sidebar for navigation
    create_sidebar()

    # Page routing
    page = st.sidebar.radio(
        "Navigate", 
        ["Home", "Projects"], 
        index=0
    )

    # Render appropriate page
    if page == "Home":
        render_home()
    elif page == "Projects":
        render_projects()


if __name__ == "__main__":
    main()