""" CLEAN CODE """

import base64

import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

import streamlit as st

# Set page title and layout
st.set_page_config(page_title='Data Analysis App', layout='wide')

# Initialize download count
def initialize_download_count():
    download_count = 0

    # Read the download count from the file if it exists
    try:
        with open("download_count.txt", "r") as file:
            download_count = int(file.read())
    except FileNotFoundError:
        pass

    return download_count

# Increment download count
def increment_download_count():
    global download_count
    download_count += 1
    # Store the updated download count in the file
    with open("download_count.txt", "w") as file:
        file.write(str(download_count))

# Upload CSV file and generate report
def upload_and_generate_report():
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
            # Display the profiling report using pandas_profiling
            profile.to_widgets()
            st_profile_report(profile)

        st.write('## Export Report')

        # Export the profiling report as HTML
        export_button = st.button('Export Report as HTML')

        if export_button:
            profile.to_file("profiling_report.html")
            st.success("Report exported successfully as HTML!", icon="✅")
            
            # Increment the download count
            increment_download_count()

            # Provide a download link for the exported report
            with open("profiling_report.html", 'rb') as file:
                b64 = base64.b64encode(file.read()).decode()  # Encode the file content in base64
                href = f'<a href="data:text/html;base64,{b64}" download="data_analysis_report.html">Download The Report</a>'
                st.markdown(href, unsafe_allow_html=True)
                st.write(":arrow_up: Click Above To Download The Report, Thank You!:pray:", icon="✅")

# Display the download count
def display_download_count():
    st.write(f"Downloaders Count: {download_count}")

# Main app
def data_analysis_app():
    global download_count

    st.title('Data Analysis App :chart_with_upwards_trend:')

    # Initialize download count
    download_count = initialize_download_count()

    # Upload and generate report
    upload_and_generate_report()

    # Display the download count
    display_download_count()

data_analysis_app()




# Attempt - 1 

# import streamlit as st
# import pandas as pd
# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report
# import base64

# # Set page title and layout
# st.set_page_config(page_title='Data Analysis App', layout='wide')

# st.title('Data Analysis App :chart_with_upwards_trend:')

# # Initialize download count
# download_count = 0

# # Read the download count from the file if it exists
# try:
#     with open("download_count.txt", "r") as file:
#         download_count = int(file.read())
# except FileNotFoundError:
#     pass

# # Define function to increment download count
# def increment_download_count():
#     global download_count
#     download_count += 1
#     # Store the updated download count in the file
#     with open("download_count.txt", "w") as file:
#         file.write(str(download_count))

# # Add a title and description
# st.write('## Upload a CSV file to generate a data profiling report.')

# # Create a file uploader widget
# uploaded_file = st.file_uploader("### Upload a CSV file", type="csv")

# if uploaded_file is not None:
#     # Read the uploaded file as a pandas DataFrame
#     df = pd.read_csv(uploaded_file)

#     # Generate the pandas profiling report
#     profile = ProfileReport(df, title="Profiling Report")

#     # Add interactivity to the report
#     st.write('## Do you need to generate the report?')

#     submit_button = st.button('Yes')
    
#     if submit_button:
#         # Display the profiling report using pandas_profiling
#         profile.to_widgets()
#         st_profile_report(profile)

#     st.write('## Export Report')

#     # Export the profiling report as HTML
#     export_button = st.button('Export Report as HTML')

#     if export_button:
#         profile.to_file("profiling_report.html")
#         st.success("Report exported successfully as HTML!", icon="✅")
        
#         # Increment the download count
#         increment_download_count()

#         # Provide a download link for the exported report
#         with open("profiling_report.html", 'rb') as file:
#             b64 = base64.b64encode(file.read()).decode()  # Encode the file content in base64
#             href = f'<a href="data:text/html;base64,{b64}" download="data_analysis_report.html">Download The Report</a>'
#             st.markdown(href, unsafe_allow_html=True)
#             st.write(":arrow_up: Click Above To Download The Report, Thank You!:pray:", icon="✅")

# # Display the download count
# st.write(f"Downloaders Count: {download_count}")

# Attempt - 2 

# import streamlit as st
# import pandas as pd
# from pandas_profiling import ProfileReport
# from streamlit_pandas_profiling import st_profile_report
# import base64

# def data_analysis_app():
#     # Set page title and layout
#     st.set_page_config(page_title='Data Analysis App', layout='wide')

#     st.title('Data Analysis App :chart_with_upwards_trend:')

#     # Initialize download count
#     download_count = 0

#     # Read the download count from the file if it exists
#     try:
#         with open("download_count.txt", "r") as file:
#             download_count = int(file.read())
#     except FileNotFoundError:
#         pass

#     # Define function to increment download count
#     def increment_download_count():
#         nonlocal download_count
#         download_count += 1
#         # Store the updated download count in the file
#         with open("download_count.txt", "w") as file:
#             file.write(str(download_count))

#     # Add a title and description
#     st.write('## Upload a CSV file to generate a data profiling report.')

#     # Create a file uploader widget
#     uploaded_file = st.file_uploader("### Upload a CSV file", type="csv")

#     if uploaded_file is not None:
#         # Read the uploaded file as a pandas DataFrame
#         df = pd.read_csv(uploaded_file)

#         # Generate the pandas profiling report
#         profile = ProfileReport(df, title="Profiling Report")

#         # Add interactivity to the report
#         st.write('## Do you need to generate the report?')

#         submit_button = st.button('Yes')
        
#         if submit_button:
#             # Display the profiling report using pandas_profiling
#             profile.to_widgets()
#             st_profile_report(profile)

#         st.write('## Export Report')

#         # Export the profiling report as HTML
#         export_button = st.button('Export Report as HTML')

#         if export_button:
#             profile.to_file("profiling_report.html")
#             st.success("Report exported successfully as HTML!", icon="✅")
            
#             # Increment the download count
#             increment_download_count()

#             # Provide a download link for the exported report
#             with open("profiling_report.html", 'rb') as file:
#                 b64 = base64.b64encode(file.read()).decode()  # Encode the file content in base64
#                 href = f'<a href="data:text/html;base64,{b64}" download="data_analysis_report.html">Download The Report</a>'
#                 st.markdown(href, unsafe_allow_html=True)
#                 st.write(":arrow_up: Click Above To Download The Report, Thank You!:pray:", icon="✅")

#     # Display the download count
#     st.write(f"Downloaders Count: {download_count}")

# data_analysis_app()

########################################################################################
