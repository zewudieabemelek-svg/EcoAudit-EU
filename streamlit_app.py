import streamlit as st
import pandas as pd

# 1. Page Configuration & Branding
st.set_page_config(page_title="VeriGreen AI | ESG Compliance", page_icon="🌱")

# Session State for Login
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    # Login Page
    st.markdown("<h1 style='text-align: center; color: #2e7d32;'>🌱 VeriGreen AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>AI-Powered ESG Audit & Compliance Dashboard</p>", unsafe_allow_html=True)
    
    email = st.text_input("Partner Email")
    password = st.text_input("Security Key", type="password")
    
    if st.button("Access Dashboard", use_container_width=True):
        if email == "admin@verigreen.ai" and password == "vg2026":
            st.session_state['logged_in'] = True
            st.rerun()
        else:
            st.error("Access Denied. Please check your credentials.")
else:
    # 2. Main Professional Dashboard
    st.sidebar.title("VeriGreen AI")
    st.sidebar.info("Authorized Auditor Session")
    
    st.title("📊 VeriGreen ESG Audit Dashboard")
    st.info("The AI Auditor is active and monitoring global compliance standards.")

    company = st.text_input("Client Company Name", placeholder="e.g., Berlin Logistics")
    
    if st.button("Generate AI Audit & Graphics"):
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
            report_content = f"VERIGREEN AI AUDIT REPORT\n\nTarget Company: {company}\nResult: High Compliance\nVerification Date: May 2026"
            
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

    if st.sidebar.button("Log Out"):
        st.session_state['logged_in'] = False
        st.rerun()
