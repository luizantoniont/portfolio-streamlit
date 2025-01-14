import streamlit as st


def render_home():
    """
    Renders the home page with data scientist identification and presentation.
    """
    col1, col2 = st.columns([1, 2])

    with col1:
        # Profile image
        st.image("data/images/image_profile.jpg", width=250)

    with col2:
        # Personal information
        st.title("Your Name")
        st.subheader("Data Scientist | Machine Learning Engineer")
        
        st.write("""
        ### About Me
        A passionate data scientist with expertise in machine learning, 
        deep learning, and data analysis. Experienced in Python, 
        scikit-learn, TensorFlow, and building end-to-end ML solutions.
        """)

        # Contact and social links
        st.markdown("""
        ### Contact
        - 📧 your.email@example.com
        - 🔗 [LinkedIn](https://linkedin.com/in/yourprofile)
        - 🐙 [GitHub](https://github.com/yourusername)
        """)