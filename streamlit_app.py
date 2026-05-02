import streamlit as st
import pandas as pd
import datetime

# Page Configuration
st.set_page_config(page_title="WealthFlow AI", page_icon="💰", layout="wide")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Go to", ["Dashboard", "Add Transaction", "Settings"])

st.title("WealthFlow AI: Strategic Finance Tracker")

# Initializing Data (In a real app, this would be a database)
if 'transactions' not in st.session_state:
    st.session_state.transactions = []

if page == "Dashboard":
    st.header("Financial Overview")
    
    # Summary Metrics
    if st.session_state.transactions:
        df = pd.DataFrame(st.session_state.transactions)
        total_income = df[df['Type'] == 'Income']['Amount'].sum()
        total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
        balance = total_income - total_expense
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Income", f"${total_income:,.2f}")
        col2.metric("Total Expenses", f"${total_expense:,.2f}")
        col3.metric("Net Balance", f"${balance:,.2f}", delta=balance)
        
        st.subheader("Transaction History")
        st.table(df)
    else:
        st.info("No transactions recorded yet. Go to 'Add Transaction' to start.")

elif page == "Add Transaction":
    st.header("Record New Transaction")
    
    with st.form("entry_form"):
        date = st.date_input("Date", datetime.date.today())
        description = st.text_input("Description (e.g., Sale, Rent, Supplies)")
        amount = st.number_input("Amount ($)", min_value=0.01, step=0.01)
        t_type = st.selectbox("Transaction Type", ["Income", "Expense"])
        
        submit = st.form_submit_button("Save Transaction")
        
        if submit:
            new_data = {"Date": date, "Description": description, "Amount": amount, "Type": t_type}
            st.session_state.transactions.append(new_data)
            st.success("Transaction saved successfully!")
