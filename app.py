import streamlit as st

# Title
st.title("🧠 AI Resume Builder")

# Form Start
with st.form("resume_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    job_role = st.text_input("Job Role")
    education = st.text_input("Education")
    experience = st.text_area("Experience")

    submitted = st.form_submit_button("Generate Resume")

# When Button Clicked
if submitted:
    st.success("✅ Form submitted successfully!")
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Phone:", phone)
    st.write("Job Role:", job_role)
    st.write("Education:", education)
    st.write("Experience:", experience)
