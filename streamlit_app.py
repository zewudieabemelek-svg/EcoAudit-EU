import streamlit as st
from supabase import create_client, Client

# 1. Supabase Connection Setup
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# 2. Page Configuration
st.set_page_config(page_title="VeriGreen AI - Official Audit", page_icon="🌿")

# 3. Professional Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3.5em; background-color: #1b5e20; color: white; font-weight: bold; }
    .status-card { padding: 20px; border-radius: 10px; background-color: white; border-left: 5px solid #1b5e20; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# 4. Sidebar Admin Authentication
with st.sidebar:
    st.title("🛡️ Admin Control")
    admin_email = st.text_input("Admin Email")
    admin_password = st.text_input("Admin Password", type="password")
    is_admin = (admin_email == st.secrets["ADMIN_EMAIL"] and admin_password == st.secrets["ADMIN_PASSWORD"])

# 5. Main Header
st.title("🌿 VeriGreen AI")
st.subheader("Environmental Audit & Sustainability Certification")
st.write("Submit your payment details below to unlock your professional audit report.")

# 6. Payment Instructions ($10 USD)
with st.expander("💳 Official Payment Methods", expanded=True):
    st.markdown("""
    **To process your report, please pay $10 USD via:**
    *   **Payment Method:** [Your Payment Link/Details Here]
    *   **Amount:** $10.00 USD per audit
    
    *Important: Each Transaction ID can only be used once. For a new project, a new payment is required.*
    """)

# 7. Secure Submission Form
st.markdown("### 📝 Submit Payment for Verification")
with st.form("secure_payment_form"):
    company_name = st.text_input("Registered Company Name")
    transaction_id = st.text_input("Transaction ID (Unique Reference)")
    
    submit_req = st.form_submit_button("Submit for Audit Clearance")

    if submit_req:
        if company_name and transaction_id:
            try:
                # Check if Transaction ID already exists
                existing = supabase.table("payment_records").select("transaction_id").eq("transaction_id", transaction_id).execute()
                
                if len(existing.data) > 0:
                    st.error("❌ This Transaction ID has already been used for another project. Please provide a new payment reference.")
                else:
                    # Save new unique record
                    supabase.table("payment_records").insert({
                        "client_name": company_name,
                        "transaction_id": transaction_id,
                        "payment_status": "pending"
                    }).execute()
                    st.success("✅ Submission received! We are verifying your $10 payment. Check back soon.")
            except Exception as e:
                st.error("Connection Error: Make sure your Database is ready.")
        else:
            st.warning("Please fill all required fields.")

st.divider()

# 8. Admin Management View
if is_admin:
    st.header("📂 Pending Verifications")
    pending_list = supabase.table("payment_records").select("*").eq("payment_status", "pending").execute()
    if pending_list.data:
        for row in pending_list.data:
            c1, c2, c3 = st.columns([2, 2, 1])
            c1.write(f"**Company:** {row['client_name']}")
            c2.write(f"**ID:** {row['transaction_id']}")
            if c3.button("Approve", key=f"approve_{row['id']}"):
                supabase.table("payment_records").update({"payment_status": "approved"}).eq("id", row['id']).execute()
                st.rerun()
    else:
        st.info("No pending requests.")

# 9. Report Access Section
st.header("📥 Access Your Audit Report")
search_ref = st.text_input("Enter your unique Transaction ID to download")

if search_ref:
    verify_res = supabase.table("payment_records").select("*").eq("transaction_id", search_ref).eq("payment_status", "approved").execute()
    if verify_res.data:
        st.balloons()
        st.markdown(f'<div class="status-card">✔️ **Verified!** Access granted.</div>', unsafe_allow_html=True)
        with open("report.pdf", "rb") as pdf_file:
            st.download_button(label="📄 Download Official PDF Report", data=pdf_file, file_name=f"Audit_{search_ref}.pdf")
    else:
        st.warning("Verification Pending or Invalid ID.")
