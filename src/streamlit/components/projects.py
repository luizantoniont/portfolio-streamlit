# src/components/projects.py
import streamlit as st
import json

def load_projects():
    """
    Load projects from JSON file.
    
    Returns:
        list: List of project dictionaries
    """
    try:
        with open('data/projects.json', 'r') as f:
            data = json.load(f)
            return data.get("projects", [])  # Acessa a chave "projects"
    except FileNotFoundError:
        st.error("Projects file not found!")
        return []

def render_projects():
    """
    Render projects page with clickable project cards.
    """
    st.title("My Data Science Projects")
    
    projects = load_projects()
    
    for project in projects:
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.image(project['image'], use_container_width=True)
        
        with col2:
            st.subheader(project['title'])
            st.write(project['description'])
            
            if st.button(f"View {project['title']} Project", key=project['id']):
                # Navigate to project details page (future enhancement)
                st.write(f"Navigating to {project['title']} details...")