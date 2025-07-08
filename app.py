import streamlit as st
from chains import generate_summary, generate_experience
from jinja2 import Environment, FileSystemLoader
import pdfkit

st.title("Resume Generator")

with st.form("resume_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    job_role = st.text_input("Job Role")
    education = st.text_input("Education")
    experience_text = st.text_area("Experience")

    submitted = st.form_submit_button("Generate Resume")

if submitted:
    summary = generate_summary(name, job_role, education)
    experience = generate_experience(name, experience_text)

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("resume_template.html")
    html_content = template.render(
        name=name,
        email=email,
        phone=phone,
        job_role=job_role,
        education=education,
        summary=summary,
        experience=experience
    )

    st.markdown(html_content, unsafe_allow_html=True)

    # Save as PDF
    pdfkit.from_string(html_content, "resume.pdf")
    with open("resume.pdf", "rb") as f:
        st.download_button("Download Resume PDF", f, file_name="resume.pdf", mime="application/pdf")
