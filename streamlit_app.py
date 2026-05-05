import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="EcoAudit EU | AI Compliance", page_icon="🌱")

# 2. Login Logic
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.markdown("<h1 style='text-align: center;'>🌱 EcoAudit EU</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Authorized Access Only</p>", unsafe_allow_html=True)
    
    email = st.text_input("Partner Email")
    password = st.text_input("Security Key", type="password")
    
    if st.button("Access Dashboard", use_container_width=True):
        if email == "admin@ecoaudit.eu" and password == "eu2026":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Invalid credentials. Please contact support.")
else:
    # 3. Main Dashboard
    st.sidebar.success("Account Verified")
    st.title("📊 ESG Compliance Dashboard")
    st.info("Welcome! Your AI Auditor is ready to process reports.")

    company = st.text_input("Enter Client Company Name")
    if st.button("Generate AI Audit Report"):
        st.success(f"Analysis Complete for {company}")
    
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()
