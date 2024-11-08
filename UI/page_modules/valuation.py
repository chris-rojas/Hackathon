import streamlit as st

def show_valuation():
    # Load custom CSS
    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    valuation_tabs = st.tabs(["DFC", "LBO"])

    # Content for each sub-tab within the Valuation section
    with valuation_tabs[0]:
        st.write("### Discounted Cash Flow (DFC) Analysis")
        st.write("Sample DFC analysis content and calculations.")

    with valuation_tabs[1]:
        st.write("### Leveraged Buyout (LBO) Analysis")
        st.write("Sample LBO analysis content and calculations.")

    ## Button to generate and download the PowerPoint file
    if st.button("Download PPT"):
        save_content_to_ppt(content, chart_path)  # Save the content to a PowerPoint file
#         with open("result/Profiler_Report.pptx", "rb") as file:
#             btn = st.download_button(
#                 label="Download PowerPoint",
#                 data=file,
#                 file_name="Profiler_Report.pptx",
#                 mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
#             )