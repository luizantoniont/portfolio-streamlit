# tests/test_app.py
import pytest
import streamlit as st
from portifolio_streamlit.components.home import render_home
from portifolio_streamlit.components.projects import load_projects

def test_load_projects():
    """Test loading projects from JSON"""
    projects = load_projects()
    assert isinstance(projects, list)
    assert len(projects) > 0
    
    # Check project structure
    for project in projects:
        assert 'id' in project
        assert 'title' in project
        assert 'description' in project

def test_home_render(monkeypatch):
    """Test home page rendering"""
    def mock_write(*args, **kwargs):
        pass
    
    monkeypatch.setattr(st, 'title', mock_write)
    monkeypatch.setattr(st, 'subheader', mock_write)
    monkeypatch.setattr(st, 'write', mock_write)
    monkeypatch.setattr(st, 'markdown', mock_write)
    monkeypatch.setattr(st, 'image', mock_write)
    
    try:
        render_home()
    except Exception as e:
        pytest.fail(f"render_home() raised {type(e).__name__} unexpectedly!")