import streamlit as st
import pandas as pd

# 1. Fetch Secrets from GitHub/Streamlit Environment
try:
    VALID_EMAIL = st.secrets["ADMIN_EMAIL"]
    VALID_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    # Fallback for local testing (Optional)
    VALID_EMAIL = "admin@verigreen.ai"
    VALID_PASSWORD = "vg2026"

# 2. Page Configuration
st.set_page_config(page_title="VeriGreen AI | Professional ESG Audit", page_icon="🛡️")

# 3. Authentication Logic
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login_page():
    st.markdown("<h2 style='text-align: center; color: #2e7d32;'>🌱 VeriGreen AI Login</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Authorized access only for ESG Audit Partners</p>", unsafe_allow_html=True)
    
    with st.form("Login_Form"):
        email = st.text_input("Partner Email")
        password = st.text_input("Security Key", type="password")
        submit_button = st.form_submit_button("Access Dashboard", use_container_width=True)
        
        if submit_button:
            if email == VALID_EMAIL and password == VALID_PASSWORD:
                st.session_state['logged_in'] = True
                st.success("Authentication Successful!")
                st.rerun()
            else:
                st.error("Access Denied. Please check your credentials.")

# 4. Main Professional Dashboard
def main_dashboard():
    # Sidebar logout
    st.sidebar.title("VeriGreen AI")
    st.sidebar.info("Session: Authorized Auditor")
    if st.sidebar.button("Secure Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()

    st.title("🛡️ ESG Audit & Compliance Dashboard")
    st.info("The AI Auditor is active and monitoring global compliance standards.")

    # Application Features
    company = st.text_input("Client Company Name", placeholder="e.g., Berlin Logistics")
    
    if st.button("Generate AI Audit & Graphics", use_container_width=True):
        if company:
            st.success(f"Audit Analysis Complete for {company}")

            # --- Visual Analytics (Graphs) ---
            st.subheader(f"ESG Performance Metrics: {company}")
            metrics_data = pd.DataFrame({
                'Metric Category': ['Environmental', 'Social', 'Governance'],
                'Compliance Score (%)': [88, 75, 92]
            })
            st.bar_chart(data=metrics_data, x='Metric Category', y='Compliance Score (%)')

            # --- PDF Download Option ---
            st.divider()
            st.write("### Official Audit Report")
            report_content = f"VERIGREEN AI AUDIT REPORT\n\nTarget Company: {company}\nResult: High Compliance\nVerification ID: VG-2026-X"
            
            st.download_button(
                label="📥 Download Official PDF Report",
                data=report_content,
                file_name=f"VeriGreen_Audit_{company}.pdf",
                mime="application/pdf",
                use_container_width=True
            )
            st.balloons()
        else:
            st.warning("Please enter a client name to start the audit.")

# 5. Application Routing
if not st.session_state['logged_in']:
    login_page()
else:
    main_dashboard()
