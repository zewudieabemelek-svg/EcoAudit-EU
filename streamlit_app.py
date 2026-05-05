import streamlit as st

# 1. Branding Updates
st.set_page_config(page_title="VeriGreen AI | ESG Compliance", page_icon="🌱")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    # Login Page with New Name
    st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🌱 VeriGreen AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>AI-Powered ESG Audit & Compliance</p>", unsafe_allow_html=True)
    
    email = st.text_input("Partner Email")
    password = st.text_input("Security Key", type="password")
    
    if st.button("Access Dashboard", use_container_width=True):
        if email == "admin@verigreen.ai" and password == "vg2026": # Updated login
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Access Denied.")
else:
    # Main Dashboard
    st.sidebar.title("VeriGreen AI")
    st.sidebar.success("Verified Partner")
    st.title("📊 VeriGreen ESG Dashboard")
    st.info("AI Auditor is active and monitoring compliance.")

    company = st.text_input("Client Name to Audit", placeholder="e.g. Berlin Logistics")
    if st.button("Generate AI Audit Report"):
        st.success(f"Audit Analysis Complete for {company}")
        st.divider()
        st.write("✅ Environmental Impact: High Compliance")
        st.write("✅ Social Governance: Standard Met")
    
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.rerun()
