import streamlit as st


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/Alfonso_profile_pic.jpg")

with col2:
    st.title("Alfonso Núñez")
    content = """
    Fullstack developer with over 8 years of experience in the electronics industry, skilled in a wide range of 
    technologies, including PHP, Python, Javascript, C#, CSS, HTML, SQL, RPA and more. 
    This versatile skill set has allowed me to work with a diverse range of clients and projects, 
    from purchase orders automations to large warehouse management apps, and has given me the flexibility to work 
    with different tech stacks based on each project's unique requirements. My ability to quickly adapt to new 
    technologies and work collaboratively with clients and colleagues sets me apart as a developer, 
    and I am always eager to learn and grow as new technologies emerge.I leverage communication and 
    teamwork skills when developing in group projects and am keen to create a friendly and collaborative 
    workspace environment.
    """
    st.info(content)