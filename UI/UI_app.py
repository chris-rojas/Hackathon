import streamlit as st

# Initialize session state for selected tab if not set
if "selected_tab" not in st.session_state:
    st.session_state["selected_tab"] = "Overview"  # Default tab for "Profiler"
if "selected_valuation_tab" not in st.session_state:
    st.session_state["selected_valuation_tab"] = "DFC"  # Default tab for "Valuation"

# Custom CSS for styling
st.markdown("""
    <style>
    /* Main content styling */
    .main-content {
        background-color: #1f3b75;
        color: white;
        padding: 20px;
        border-radius: 10px;
        height: 300px;
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
    /* Selected and unselected tab button styling */
    .tab-button {
        background-color: #003366;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 10px;
        cursor: pointer;
        font-size: 16px;
        text-align: center;
        width: 100%;
    }
    .tab-button-selected {
        background-color: #00bfff;
        color: white;
        border-radius: 10px;
        font-size: 16px;
        text-align: center;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown('<div class="sidebar-section">', unsafe_allow_html=True)

# Input box for "Company/Ticker"
company_ticker = st.sidebar.text_input("Company/ Ticker")

# Track selected button in sidebar
selected_option = st.session_state.get("selected_option", "Profiler")

# Sidebar buttons
if st.sidebar.button("Profiler"):
    st.session_state["selected_option"] = "Profiler"
if st.sidebar.button("Chat Bot"):
    st.session_state["selected_option"] = "Chat Bot"
if st.sidebar.button("Valuation"):
    st.session_state["selected_option"] = "Valuation"
st.sidebar.markdown('</div>', unsafe_allow_html=True)

# Display content based on selected sidebar button
if st.session_state["selected_option"] == "Chat Bot":
    # Chat Bot Layout
    chat_input = st.text_input('Enter Question/Prompt here')
    st.markdown('<div class="main-content">This is the company financials</div>', unsafe_allow_html=True)
elif st.session_state["selected_option"] == "Profiler":
    # Horizontal Tabs for Profiler
    tabs = ["Overview", "Financials", "Geographic Mix", "Management", "Recent News"]
    selected_tab = st.session_state["selected_tab"]

    # Display buttons as tabs
    columns = st.columns(len(tabs))
    for idx, tab in enumerate(tabs):
        button_style = "tab-button-selected" if tab == selected_tab else "tab-button"
        with columns[idx]:
            if st.button(tab, key=f"profiler_{tab}", help=f"{tab} content", use_container_width=True):
                st.session_state["selected_tab"] = tab

    # Display main content based on selected tab
    st.markdown(f'<div class="main-content">{st.session_state["selected_tab"]} content goes here</div>', unsafe_allow_html=True)
elif st.session_state["selected_option"] == "Valuation":
    # Horizontal Tabs for Valuation
    tabs = ["DFC", "LBO"]
    selected_tab = st.session_state["selected_valuation_tab"]

    # Display buttons as tabs
    columns = st.columns(len(tabs))
    for idx, tab in enumerate(tabs):
        button_style = "tab-button-selected" if tab == selected_tab else "tab-button"
        with columns[idx]:
            if st.button(tab, key=f"valuation_{tab}", help=f"{tab} content", use_container_width=True):
                st.session_state["selected_valuation_tab"] = tab

    # Display main content based on selected tab
    st.markdown(f'<div class="main-content">{st.session_state["selected_valuation_tab"]} content goes here</div>', unsafe_allow_html=True)
else:
    st.markdown(f'<div class="main-content">Pitch deck tool overview</div>', unsafe_allow_html=True)

# Download button
st.markdown('<button class="download-btn">Download PPT</button>', unsafe_allow_html=True)
