import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
creds_dict = st.secrets["gcp_service_account"]
st.set_page_config(page_title="GuruMantra IT Career Assistant")

st.title("🎯 GuruMantra IT Career Assistant")
st.write("Hi 👋 I help students choose the right IT career path.")

# ---------------- GOOGLE SHEETS CONNECTION ----------------

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds_dict = st.secrets["gcp_service_account"]

creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

sheet = client.open("GuruMantra_Leads").sheet1

# ---------------- SESSION STATE ----------------

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

# STEP 4 – Career Suggestion + Lead Save
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

    st.info("🎁 Get your personalised AI roadmap instantly — takes 30 seconds")

    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

    if st.button("Submit"):

        if not name or not phone or not email:
            st.error("Please fill all details")

        else:
            sheet.append_row([
                name,
                phone,
                email,
                st.session_state.education,
                st.session_state.coding
            ])

            st.success("✅ Your roadmap is ready 🚀")

            st.markdown("### 📥 Download your AI Career Roadmap")
            st.link_button(
                "Download PDF",
                "https://drive.google.com/uc?export=download&id=1q2lrNBkHitLkuhVwq_YtYreYsFKn62LW"
            )




