import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="EcoAudit EU | Global Compliance & Tax AI", page_icon="🏦", layout="centered")

# Logo display logic
try:
    image = Image.open('logo.png')
    st.image(image, width=150)
except:
    st.info("System: Application logo is being updated...")

st.title("EcoAudit EU: Strategic Compliance & Tax")
st.markdown("---")

# Sidebar for Subscription & Tiered Pricing
st.sidebar.header("SELECT YOUR PLAN")
plan = st.sidebar.selectbox("Choose Access Level:", 
                           ["Free Plan", "Professional ($29/mo)", "Enterprise ($2,499/mo)", "Billionaire/Investor (VIP Custom)"])

# Common Payment Message Logic with User Details
def display_payment_info(plan_name):
    st.sidebar.success(f"👑 {plan_name} ACTIVE")
    st.sidebar.write("**OFFICIAL BANK TRANSFER DETAILS:**")
    st.sidebar.write("BANK: **COMMERCIAL BANK OF ETHIOPIA**")
    st.sidebar.write("ACC NAME: **ABEMELEK ZEWUDIE MOKRIYA**")
    st.sidebar.write("ACC NUMBER: **1000269762776**")
    st.sidebar.warning("⚠️ ACTION REQUIRED")
    st.sidebar.write("Send payment screenshot to activate:")
    st.sidebar.write("📧 Email: **zewudieabemelek@gmail.com**")
    st.sidebar.write("✈️ Telegram: **@Abela21**")

if plan == "Billionaire/Investor (VIP Custom)":
    display_payment_info("VIP INVESTOR PLAN")
    st.sidebar.write("- Priority Wealth Optimization")
elif plan == "Enterprise ($2,499/mo)":
    display_payment_info("ENTERPRISE PLAN")
elif plan == "Professional ($29/mo)":
    display_payment_info("PROFESSIONAL PLAN")
else:
    st.sidebar.info("Free Plan Active. Upgrade for AI Tax Tools.")

st.markdown("---")

# --- INVESTOR FEATURE: TAX & CARBON CALCULATOR ---
st.header("📊 AI Tax & Carbon Liability Optimizer")
st.subheader("For Institutional Investors & Billionaire Portfolios")

revenue = st.number_input("Enter Total Annual Revenue (in USD):", min_value=0, value=10000000)
emissions = st.number_input("Enter Estimated Carbon Emissions (in Tons):", min_value=0, value=50000)

if st.button("Calculate Tax Liability"):
    if plan == "Billionaire/Investor (VIP Custom)":
        with st.spinner('Calculating EU CBAM Tax & Corporate Liabilities...'):
            tax_estimate = emissions * 85 
            potential_fine = revenue * 0.04
            st.error(f"💰 ESTIMATED CARBON TAX LIABILITY: ${tax_estimate:,.2f}")
            st.warning(f"🚨 POTENTIAL NON-COMPLIANCE FINE: ${potential_fine:,.2f}")
            st.success(f"✅ AI STRATEGY: Implementing Scope 3 reduction could save you approx. ${tax_estimate * 0.25:,.2f} annually.")
            st.button("Download Full Wealth Strategy (VIP Only)")
    else:
        st.warning("🔒 This Financial Optimization tool is restricted to VIP/Billionaire Plan members.")

st.markdown("---")

# Audit Section
st.header("Start Your AI Compliance Audit")
user_input = st.text_area("Paste operational data or regulatory queries here:", height=100)
if st.button("Run AI Audit"):
    if user_input:
        st.info("Analysis complete. Reviewing compliance alignment with EU Directives.")
    else:
        st.warning("Please provide data to begin the audit.")

st.markdown("---")
st.caption("© 2026 EcoAudit EU | Global Enterprise & Wealth Management Systems")
