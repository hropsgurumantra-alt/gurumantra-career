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

    import time

st.markdown("## 🤖 AI Career Intelligence Engine")

q1 = st.radio("Do you enjoy solving problems logically?", ["Yes", "Somewhat", "Not sure"])
q2 = st.radio("How comfortable are you with numbers/data?", ["High", "Medium", "Low"])
q3 = st.radio("Can you commit to learning consistently?", ["Yes", "Maybe", "No"])
q4 = st.radio("What excites you more?", ["Building apps", "Analysing data", "Support roles"])
q5 = st.radio("Coding experience?", ["Experienced", "Beginner", "None"])

if st.button("🔍 Analyse My Career Fit"):

    with st.spinner("🧠 Analysing..."):
        time.sleep(2)

    score = 0
    confidence = 100
    path_python = 0
    path_data = 0
    path_testing = 0

    if q1 == "Yes":
        score += 25
        path_python += 20
    elif q1 == "Somewhat":
        score += 15
    else:
        confidence -= 20

    if q2 == "High":
        score += 20
        path_data += 25
    elif q2 == "Medium":
        score += 10
    else:
        confidence -= 15

    if q3 == "Yes":
        score += 25
    elif q3 == "Maybe":
        score += 10
    else:
        confidence -= 30

    if q4 == "Building apps":
        path_python += 30
    elif q4 == "Analysing data":
        path_data += 30
    else:
        path_testing += 30

    if q5 == "Experienced":
        path_python += 20
    elif q5 == "Beginner":
        path_python += 10
    else:
        path_testing += 20

    best_path = max(
        [("Python Developer", path_python),
         ("Data Analyst", path_data),
         ("Software Testing", path_testing)],
        key=lambda x: x[1]
    )[0]

    st.session_state.score = score
    st.session_state.best_path = best_path

    st.success(f"🎯 Suitability Score: {score}%")
    st.info(f"⭐ Recommended Path: {best_path}")      

    name = st.text_input("Your Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")

    if st.button("Submit"):

    if not name or not phone or not email:
        st.error("Please fill all details")

    else:

        score = st.session_state.get("score", 0)

        if score >= 70:
            lead_label = "HOT 🔥"
        elif score >= 40:
            lead_label = "WARM 🙂"
        else:
            lead_label = "COLD ❄"

        sheet.append_row([
            name,
            phone,
            email,
            st.session_state.education,
            st.session_state.coding,
            score,
            lead_label
        ])

        st.success("✅ Your roadmap is ready 🚀")

        if lead_label.startswith("HOT"):
            st.success("🔥 Strong fit — our mentor should speak with you soon.")
        elif lead_label.startswith("WARM"):
            st.info("🙂 Good potential — roadmap will guide you.")
        else:
            st.warning("❄ Start with fundamentals — consistency matters.")

        st.markdown("### 📥 Download your AI Career Roadmap")
        st.link_button(
            "Download PDF",
            "https://drive.google.com/uc?export=download&id=1q2lrNBkHitLkuhVwq_YtYreYsFKn62LW"
        )
            






