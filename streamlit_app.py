import streamlit as st
import pandas as pd

# 1. Page Configuration & Security Setup
st.set_page_config(page_title="VeriGreen AI | Secure ESG Audit", page_icon="🛡️", layout="centered")

# Initialize session states for logic flow
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'audit_ready' not in st.session_state:
    st.session_state['audit_ready'] = False
if 'payment_confirmed' not in st.session_state:
    st.session_state['payment_confirmed'] = False

# Safely fetch credentials from GitHub/Streamlit Secrets
try:
    VALID_EMAIL = st.secrets["ADMIN_EMAIL"]
    VALID_PASSWORD = st.secrets["ADMIN_PASSWORD"]
except Exception:
    # Default fallback for initial setup only
    VALID_EMAIL = "admin@verigreen.ai"
    VALID_PASSWORD = "vg2026"

# 2. Professional Login Interface
if not st.session_state['logged_in']:
    st.markdown("<h2 style='text-align: center; color: #2e7d32;'>🛡️ VeriGreen AI Portal</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Authorized Partner Access Only</p>", unsafe_allow_html=True)
    
    with st.form("Secure_Login"):
        email = st.text_input("Partner Email")
        password = st.text_input("Security Key", type="password")
        if st.form_submit_button("Enter Dashboard", use_container_width=True):
            if email == VALID_EMAIL and password == VALID_PASSWORD:
                st.session_state['logged_in'] = True
                st.success("Access Granted.")
                st.rerun()
            else:
                st.error("Invalid credentials. Please contact administration.")

# 3. Main Audit Dashboard & Paywall
else:
    st.sidebar.title("VeriGreen AI")
    st.sidebar.info("Signed in as: Authorized Auditor")
    if st.sidebar.button("Secure Logout"):
        st.session_state['logged_in'] = False
        st.rerun()

    st.title("🛡️ ESG Audit & Compliance Dashboard")
    st.markdown("### Step 1: Run Analysis")
    company = st.text_input("Client Company Name", placeholder="e.g., Global Logistics Corp")

    if st.button("Generate AI Audit Report", use_container_width=True):
        if company:
            st.session_state['audit_ready'] = True
            st.success(f"Audit analysis for '{company}' is ready for download.")
        else:
            st.warning("Please enter a valid company name.")

    # --- Secure Paywall Section ---
    if st.session_state['audit_ready'] and not st.session_state['payment_confirmed']:
        st.divider()
        st.error("🔒 ACCESS RESTRICTED: Payment Verification Required")
        st.write("To unlock the full certified PDF report and visual metrics, please complete a payment of **500 ETB / $20**.")

        # Payment Tabs for Local vs International
        tab1, tab2 = st.tabs(["🇪🇹 Local Payment (Telebirr/CBE)", "🌐 International (SWIFT Transfer)"])

        with tab1:
            st.markdown("### Local Options")
            st.info("**Option A: Telebirr**\n\nNumber: **+251930378875**\nName: Abemelek Zewudie Mokriya")
            st.info("**Option B: CBE (Local Transfer)**\n\nAccount: **1000269762776**\nName: Abemelek Zewudie Mokriya")

        with tab2:
            st.markdown("### Global Bank Transfer")
            st.code(f"""
Bank Name: Commercial Bank of Ethiopia
SWIFT Code: CBETETAA
Account Name: Abemelek Zewudie Mokriya
Account No: 1000269762776
Address: Addis Ababa, Ethiopia
            """, language="text")

        st.markdown("---")
        st.subheader("Final Verification")
        trans_id = st.text_input("Enter Transaction ID / Reference Number", placeholder="Paste your receipt ID here...")
        
        if st.button("Unlock Certified Report"):
            if trans_id:
                st.info(f"Checking Reference: {trans_id}. System is awaiting Admin approval.")
                # Manual admin override for demonstration
                if st.checkbox("Admin: Confirm payment received?"):
                    st.session_state['payment_confirmed'] = True
                    st.rerun()
            else:
                st.error("A Transaction ID is required to verify your payment.")

    # --- Success Section: Unlocked Content ---
    if st.session_state['payment_confirmed']:
        st.balloons()
        st.success("✅ Payment Verified! Official Report Unlocked.")
        
        # Display Analytics
        st.subheader(f"ESG Analytics: {company}")
        metrics = pd.DataFrame({'Category': ['Environmental', 'Social', 'Governance'], 'Score (%)': [88, 72, 95]})
        st.bar_chart(data=metrics, x='Category', y='Score (%)')

        # Download Component
        report_pdf_content = f"VERIGREEN AI CERTIFIED AUDIT\n\nClient: {company}\nVerification ID: {trans_id}\nStatus: COMPLIANT"
        st.download_button(
            label="📥 Download Certified PDF Report",
            data=report_pdf_content,
            file_name=f"VeriGreen_Audit_{company}.pdf",
            mime="application/pdf",
            use_container_width=True
        )
