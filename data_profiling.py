import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from PIL import Image

# Set page title and layout 
st.set_page_config(page_title='Data Analysis App', layout='wide')

st.title('Data Analysis App :chart_with_upwards_trend:')

# image = Image.open('image.jpg')
# st.image(image, caption='Data Analysis', width = 1110)

# Add a title and description
st.write('## Upload a CSV file to generate a data profiling report.')

# Create a file uploader widget
uploaded_file = st.file_uploader("### Upload a CSV file", type="csv")

# Initialize the download counter
counter = 0

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

        # Update the download counter
        counter += 1

# Display the download counter
st.write("## Download Count:", counter)

# Display the number of people who downloaded the report
st.write(f"{counter} {'person' if counter == 1 else 'people'} downloaded the report.")