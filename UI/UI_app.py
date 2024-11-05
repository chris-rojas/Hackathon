import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    /* Sidebar styling */
    .sidebar-section {
        background-color: #e0e0e0;
        padding: 20px;
        border-radius: 10px;
    }
    /* Main content styling */
    .main-content {
        background-color: #1f3b75;
        color: white;
        padding: 20px;
        border-radius: 10px;
        height: 400px;
        text-align: center;
    }
    /* Download button styling */
    .download-btn {
        background-color: #00bfff;
        color: white;
        padding: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        text-align: center;
        width: 150px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown('<div class="sidebar-section">', unsafe_allow_html=True)

# Input box for "Company/Ticker"
company_ticker = st.sidebar.text_input("Company/ Ticker")

# Sidebar buttons
if st.sidebar.button("Profiler"):
    st.session_state['selected_button'] = "Profiler"
if st.sidebar.button("Chat Bot"):
    st.session_state['selected_button'] = "Chat Bot"
if st.sidebar.button("Valuation"):
    st.session_state['selected_button'] = "Valuation"
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Horizontal tabs using st.columns()
tabs = ["Overview", "Financials", "Geographic Mix", "Management", "Recent News"]
selected_tab = st.session_state.get("selected_tab", tabs[0])

# Create columns for tabs
columns = st.columns(len(tabs))
for idx, tab in enumerate(tabs):
    if columns[idx].button(tab):
        selected_tab = tab
        st.session_state["selected_tab"] = tab

# Display main content
st.markdown(f'<div class="main-content">{selected_tab} content goes here</div>', unsafe_allow_html=True)

# Download button
st.markdown('<button class="download-btn">Download PPT</button>', unsafe_allow_html=True)
