import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="GuruMantra IT Career Assistant")

st.title("🎯 GuruMantra IT Career Assistant")
st.write("Hi 👋 I help students choose the right IT career path.")

if "step" not in st.session_state:
    st.session_state.step = 1

# STEP 1 – Start
if st.session_state.step == 1:
    if st.button("Start Career Guidance"):
        st.session_state.step = 2

# STEP 2 – Education
if st.session_state.step == 2:
    education = st.selectbox("What is your education?",
                             ["BSc", "BCom", "BE/BTech", "Arts", "Diploma", "Other"])
    if st.button("Next"):
        st.session_state.education = education
        st.session_state.step = 3

# STEP 3 – Interest
if st.session_state.step == 3:
    coding = st.radio("Do you like coding?",
                      ["Yes", "No", "Not Sure"])
    if st.button("See Career Suggestion"):
        st.session_state.coding = coding
        st.session_state.step = 4

# STEP 4 – Career Suggestion
if st.session_state.step == 4:

    if st.session_state.coding == "No":
        st.success("""
        🎯 Recommended Careers:
        ✔ Software Testing
        ✔ IT Support
        ✔ Salesforce Admin
        ✔ Business Analyst
        """)
    else:
        st.success("""
        🎯 Recommended Careers:
        ✔ Python Developer
        ✔ Frontend Developer
        ✔ Data Analyst
        ✔ Full Stack Developer
        """)

    st.write("📩 Enter your details to receive FREE Career Roadmap + Demo Class")

    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

    if st.button("Submit"):

        new_data = pd.DataFrame({
            "Name": [name],
            "Phone": [phone],
            "Email": [email],
            "Education": [st.session_state.education],
            "Coding Interest": [st.session_state.coding]
        })

        if os.path.exists("leads.csv"):
            new_data.to_csv("leads.csv", mode='a', header=False, index=False)
        else:
            new_data.to_csv("leads.csv", index=False)

        st.success("✅ Thank you! Our team will contact you soon 🚀")