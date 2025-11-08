import streamlit as st

st.title("💊 Pharma AI Assistant")
st.write("Welcome to the Pharma AI Assistant!")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose Agent", [
    "Dashboard",
    "Vision QC Agent", 
    "Predictive Maintenance",
    "Compliance Agent", 
    "Inventory Agent"
])

if page == "Dashboard":
    st.header("Dashboard")
    st.write("Select an AI agent from the sidebar")
    
elif page == "Vision QC Agent":
    st.header("Vision QC Agent")
    st.write("Upload product images for quality check")
    
elif page == "Predictive Maintenance":
    st.header("Predictive Maintenance")
    st.write("Monitor equipment health and predict failures")
    
elif page == "Compliance Agent":
    st.header("Compliance Agent")
    st.write("Check batch records for regulatory compliance")
    
elif page == "Inventory Agent":
    st.header("Inventory Agent")
    st.write("Manage API inventory and supplier sourcing")
