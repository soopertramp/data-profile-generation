import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
import streamlit_analytics
import base64

streamlit_analytics.start_tracking()

# Set page title and layout
st.set_page_config(page_title='Data Analysis App', layout='wide')

st.title('Data Analysis App :chart_with_upwards_trend:')

# Initialize download count
@st.cache_data(ttl=None)
def init_download_count():
    return 0

download_count = init_download_count()

# Add a title and description
st.write('## Upload a CSV file to generate a data profiling report.')

# Create a file uploader widget
uploaded_file = st.file_uploader("### Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Read the uploaded file as a pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Generate the pandas profiling report
    profile = ProfileReport(df, title="Profiling Report")

    # Add interactivity to the report
    st.write('## Do you need to generate the report?')
    submit_button = st.button('Yes')
    
    if submit_button:
        # Display the profiling report using streamlit_pandas_profiling
        st_profile_report(profile)

    st.write('## Export Report')

    # Export the profiling report as HTML
    export_button = st.button('Export Report as HTML')

    if export_button:
        profile.to_file("profiling_report.html")
        st.success("Report exported successfully as HTML!", icon="✅")

        # Provide a download link for the exported report
        with open("profiling_report.html", 'rb') as file:
            b64 = base64.b64encode(file.read()).decode()  # Encode the file content in base64
            href = f'<a href="data:text/html;base64,{b64}" download="profiling_report.html">Download The Report</a>'
            st.markdown(href, unsafe_allow_html=True)
            st.write(":arrow_up: Click Above To Download The Report, Thank You!:pray:", icon="✅")
            
        # Increment the download count
        download_count += 1

# Display the download count
st.write(f"Download Count: {download_count}")

streamlit_analytics.stop_tracking()