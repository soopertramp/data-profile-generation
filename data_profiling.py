""" CLEAN CODE """

# Importing Necessary Libraries
import base64

import pandas as pd
#from pandas_profiling import
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

import streamlit as st

# Set page title and layout
st.set_page_config(page_title='Data Analysis App', layout='wide')

# Initialize download count
def initialize_download_count() -> int:
    """
    Initialize the download count.

    This function reads the download count from a file if it exists,
    otherwise, it sets the download count to 0.

    Returns:
        The initialized download count (integer).

    Raises:
        FileNotFoundError: If the file containing the download count does not exist.

    """
    download_count = 100

    # Read the download count from the file if it exists
    try:
        with open("download_count.txt", "r") as file:
            download_count = int(file.read())
    except FileNotFoundError:
        pass

    return download_count

# Increment download count
def increment_download_count() -> None:
    """
    Increment the download count by 1 and store the updated count in a file.

    This function increments the download count by 1, stores the updated count in a file called "download_count.txt".

    Returns:
        None.

    """
    global download_count
    download_count += 1
    # Store the updated download count in the file
    with open("download_count.txt", "w") as file:
        file.write(str(download_count))

# Upload CSV or Excel file and generate report
def upload_and_generate_report() -> None:
    """
    Upload a CSV or Excel file and generate a data profiling report.

    This function allows the user to upload a CSV or Excel file and generates a data profiling report using pandas-profiling.
    It provides options to display the report, export it as HTML, increment the download count, and provide a download link.

    Returns:
        None.

    """
    st.write('## Upload a CSV or Excel file to generate a data profiling report.')

    # Create a file uploader widget
    uploaded_file = st.file_uploader("### Upload a file", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the uploaded file as a pandas DataFrame
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Invalid file format. Please upload a CSV or Excel file.")
            return

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
                st.write(":arrow_up: Click Above To Download The Report, Thank You!:pray:")

# Display the download count
def display_download_count(download_count: int) -> None:
    """
    Display the download count.

    This function takes the download count as input and displays it using Streamlit.

    Parameters:
        download_count (int): The current download count.

    Returns:
        None.

    """
    st.write(f"Downloaders Count: {download_count}")

# Main app
def data_analysis_app() -> None:
    """
    Run the Data Analysis App.

    This function runs the data analysis app, including uploading and generating a report, and displaying the download count.

    Returns:
        None.

    """
    global download_count

    st.title('Data Analysis App :chart_with_upwards_trend:')

    # Initialize download count
    download_count = initialize_download_count()

    # Upload and generate report
    upload_and_generate_report()

    # Display the download count
    display_download_count(download_count)

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