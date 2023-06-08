import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Set page title and layout
st.set_page_config(page_title='Data Profiling App', layout='wide')

# Add a title and description
st.title('Data Profiling App')
st.write('Upload a CSV file to generate a data profiling report.')

# Create a file uploader widget
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

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
        st.success("Report exported successfully as HTML!")