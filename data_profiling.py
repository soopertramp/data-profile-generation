""" CLEAN CODE """

# Importing Necessary Libraries
import base64

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport


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
    download_count = 123

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
    st.subheader('Upload a CSV or Excel file to generate a data profiling report.')

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
        
        st.subheader('Basic Investigation Of The Dataset Before Cleaning The Data')
        
        # Display the entire dataset
        if st.button('Show Dataset'):
            st.subheader('Your Dataset')
            st.write(df)

        # Display the top 5 rows of the dataset
        if st.button('Show Top 5 Rows'):
            st.subheader('Top 5 Rows')
            st.write(df.head(5))

        # Display the bottom 5 rows of the dataset
        if st.button('Show Bottom 5 Rows'):
            st.subheader('Bottom 5 Rows')
            st.write(df.tail(5))

        # Display the shape of the dataset
        if st.button('Show Shape of the Dataset'):
            st.subheader('Shape of the dataset')
            st.write(f'The shape of your dataset is {df.shape[0]} rows and {df.shape[1]} columns')

        # Display the types of columns
        if st.button('Show Types of Columns'):
            st.subheader('The types of your columns')
            st.write(df.dtypes)

        # Display missing values and duplicate values
        if st.button('Show Missing Values and Duplicate Values'):
            st.subheader('Missing Values and Duplicate Values In Your Dataset')
            missing_values = df.isnull().sum()
            missing_values_formatted = ', '.join(f"{column} - {count}" for column, count in missing_values.items())
            st.write(f"The DataFrame contains missing values:\n\n{missing_values_formatted}\n")
            st.write(f'The number of duplicated rows in your dataset is {df.duplicated().sum()}')

        # Display descriptive statistics
        if st.button('Show Descriptive Statistics'):
            st.subheader('Descriptive Statistics of Your Dataset')
            st.write(df.describe())
        
        # Ask the user for data cleaning inputs
        st.subheader('Data Cleaning Inputs')

        # Example: Remove missing values
        remove_missing_values = st.checkbox('Remove missing values')
        if remove_missing_values:
            df = df.dropna()

        # Example: Convert string columns to lowercase
        lowercase_columns = st.multiselect('Columns to convert to lowercase', df.select_dtypes(include=['object']).columns)
        for column in lowercase_columns:
            df[column] = df[column].str.lower()

        # Example: Remove duplicates
        remove_duplicates = st.checkbox('Remove duplicates')
        if remove_duplicates:
            df = df.drop_duplicates()

        # Example: Convert date columns to datetime
        date_columns = st.multiselect('Columns to convert to datetime', df.select_dtypes(include=['object']).columns)
        for column in date_columns:
            df[column] = pd.to_datetime(df[column])

        # Example: Remove outliers
        remove_outliers = st.checkbox('Remove outliers')
        if remove_outliers:
            num_columns = df.select_dtypes(include=['number']).columns
            for column in num_columns:
                q1 = df[column].quantile(0.25)
                q3 = df[column].quantile(0.75)
                iqr = q3 - q1
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

        # Example: Standardize numerical columns
        standardize_columns = st.multiselect('Numerical columns to standardize', df.select_dtypes(include=['number']).columns)
        for column in standardize_columns:
            df[column] = (df[column] - df[column].mean()) / df[column].std()

        # Example: One-hot encode categorical columns
        categorical_columns = st.multiselect('Categorical columns to one-hot encode', df.select_dtypes(include=['object']).columns)
        df = pd.get_dummies(df, columns=categorical_columns)

        # Example: Convert boolean columns to binary
        boolean_columns = st.multiselect('Boolean columns to convert to binary', df.select_dtypes(include=['bool']).columns)
        for column in boolean_columns:
            df[column] = df[column].astype(int)
            
        logo_string = 'https://github.com/soopertramp/data-analysis-app/blob/main/logo.png'    

        # Generate the pandas profiling report
        profile = ProfileReport(df, 
                                title="Profiling Report", 
                                explorative = True, 
                                dark_mode = True,
                                dataset={
                                "description": "This app is created by - Pradeepchandra Reddy S C (a.k.a soopertramp07)",
                                "copyright_holder": "soopertramp07",
                                "copyright_year": "2023",
                                "url": "https://www.linkedin.com/in/pradeepchandra-reddy-s-c/"},
                                html={"style": {"logo": logo_string}})
        
        st.subheader('Basic Investigation Of The Dataset After Cleaning')
        
        # Display the entire dataset
        if st.button('Show Dataset', key='show_dataset'):
            st.subheader('Your Dataset')
            st.write(df)

        # Display the top 5 rows of the dataset
        if st.button('Show Top 5 Rows', key='show_top_rows'):
            st.subheader('Top 5 Rows')
            st.write(df.head(5))

        # Display the bottom 5 rows of the dataset
        if st.button('Show Bottom 5 Rows', key='show_bottom_rows'):
            st.subheader('Bottom 5 Rows')
            st.write(df.tail(5))

        # Display the shape of the dataset
        if st.button('Show Shape of the Dataset', key='show_dataset_shape'):
            st.subheader('Shape of the dataset')
            st.write(f'The shape of your dataset is {df.shape[0]} rows and {df.shape[1]} columns')

        # Display the types of columns
        if st.button('Show Types of Columns', key='show_dataset_columns'):
            st.subheader('The types of your columns')
            st.write(df.dtypes)

        # Display missing values and duplicate values
        if st.button('Show Missing Values and Duplicate Values', key='show_dataset_missing'):
            st.subheader('Missing Values and Duplicate Values In Your Dataset')
            missing_values = df.isnull().sum()
            missing_values_formatted = ', '.join(f"{column} - {count}" for column, count in missing_values.items())
            st.write(f"The DataFrame contains missing values:\n\n{missing_values_formatted}\n")
            st.write(f'The number of duplicated rows in your dataset is {df.duplicated().sum()}')

        # Display descriptive statistics
        if st.button('Show Descriptive Statistics', key='show_dataset_statistics'):
            st.subheader('Descriptive Statistics of Your Dataset')
            st.write(df.describe())
            
        if st.button('Download Cleaned Dataset'):
            # Convert DataFrame to CSV file
            csv = df.to_csv(index=False)
            
            # Generate download link
            b64 = base64.b64encode(csv.encode()).decode()
            href = f'<a href="data:file/csv;base64,{b64}" download="cleaned_dataset.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        
        st.set_option('deprecation.showPyplotGlobalUse', False)
        
        # Create plots
        #generate_plots = st.button("Do You Want To Generate Plots")
        #if generate_plots:
        st.subheader('Plots')
        plot_types = ['scatter', 'line', 'bar', 'histogram', 'box', 'pie']
        aggregation_levels = ['Yearly', 'Monthly', 'Daily']

        # Select plot type
        selected_plot = st.selectbox('Select plot type', plot_types)

        # Select aggregation level
        selected_aggregation = st.selectbox('Select aggregation level', aggregation_levels)

        if selected_plot == 'scatter':
            st.subheader('Scatter Plot')
            x_variable = st.selectbox('Select x-axis variable', df.columns)
            y_variable = st.selectbox('Select y-axis variable', df.columns)

            # Check if x_variable is a date column
            if df[x_variable].dtype == 'datetime64[ns]':
                if selected_aggregation == 'Yearly':
                    df['Year'] = df[x_variable].dt.year
                    df_grouped = df.groupby('Year')[y_variable].mean()  # Aggregate by yearly mean
                    x_values = df_grouped.index
                    y_values = df_grouped.values
                elif selected_aggregation == 'Monthly':
                    df['Month'] = df[x_variable].dt.to_period('M')
                    df_grouped = df.groupby('Month')[y_variable].mean()  # Aggregate by monthly mean
                    x_values = df_grouped.index.to_timestamp()  # Convert period index back to timestamp
                    y_values = df_grouped.values
                elif selected_aggregation == 'Daily':
                    df['Date'] = df[x_variable].dt.date
                    df_grouped = df.groupby('Date')[y_variable].mean()  # Aggregate by daily mean
                    x_values = df_grouped.index
                    y_values = df_grouped.values
            else:
                # Check if x_variable is a numerical column
                if np.issubdtype(df[x_variable].dtype, np.number):
                    bin_values = np.histogram(df[x_variable], bins='auto')[1]
                    x_values = pd.cut(df[x_variable], bins=bin_values, labels=False)
                    y_values = df[y_variable]
                else:
                    # Assign numerical values to categories
                    categories = df[x_variable].unique()
                    category_dict = {category: i for i, category in enumerate(categories)}
                    x_values = df[x_variable].map(category_dict)
                    y_values = df[y_variable]

            plt.figure(figsize=(8, 6))
            plt.scatter(x_values, y_values)
            plt.xlabel(x_variable)
            plt.ylabel(y_variable)
            plt.title('Scatter Plot')
            plt.tight_layout()
            plt.xticks(rotation=45)
            if df[x_variable].dtype == 'datetime64[ns]':
                if selected_aggregation == 'Yearly':
                    plt.xticks(x_values, x_values.astype(str))  # Format x-axis ticks as desired
                elif selected_aggregation == 'Monthly':
                    plt.xticks(x_values, x_values.strftime('%Y-%m'))  # Format x-axis ticks as desired
                elif selected_aggregation == 'Daily':
                    plt.xticks(x_values, x_values.astype(str))  # Format x-axis ticks as desired
            st.pyplot()

        elif selected_plot == 'line':
            st.subheader('Line Plot')
            x_variable = st.selectbox('Select x-axis variable', df.columns)
            y_variable = st.selectbox('Select y-axis variable', df.columns)

            # Check if x_variable is a date column
            if df[x_variable].dtype == 'datetime64[ns]':
                if selected_aggregation == 'Yearly':
                    df_grouped = df.groupby(df[x_variable].dt.year).mean()
                    x_values = df_grouped.index
                    y_values = df_grouped[y_variable].values
                elif selected_aggregation == 'Monthly':
                    df_grouped = df.groupby(pd.Grouper(key=x_variable, freq='M')).mean()
                    x_values = df_grouped.index
                    y_values = df_grouped[y_variable].values
                elif selected_aggregation == 'Daily':
                    df_grouped = df.groupby(df[x_variable].dt.date).mean()  # Aggregate by daily mean
                    x_values = df_grouped.index
                    y_values = df_grouped[y_variable].values
            else:
                # Check if x_variable is a numerical column
                if np.issubdtype(df[x_variable].dtype, np.number):
                    x_values = df[x_variable]
                    y_values = df[y_variable]
                else:
                    # Assign numerical values to categories
                    categories = df[x_variable].unique()
                    category_dict = {category: i for i, category in enumerate(categories)}
                    x_values = df[x_variable].map(category_dict)
                    y_values = df[y_variable]

            plt.figure(figsize=(12, 6))
            plt.plot(x_values, y_values)
            plt.xlabel(x_variable)
            plt.ylabel(y_variable)
            plt.title('Line Plot')
            plt.tight_layout()
            plt.xticks(rotation=45)
            if df[x_variable].dtype == 'datetime64[ns]':
                if selected_aggregation == 'Yearly':
                    plt.xticks(x_values, x_values.astype(str))  # Format x-axis ticks as desired
                elif selected_aggregation == 'Monthly':
                    plt.xticks(x_values, x_values.strftime('%Y-%m'))  # Format x-axis ticks as desired
                elif selected_aggregation == 'Daily':
                    plt.xticks(x_values, x_values.astype(str))  # Format x-axis ticks as desired
            st.pyplot()

        elif selected_plot == 'bar':
            st.subheader('Bar Plot')
            x_variable = st.selectbox('Select x-axis variable', df.columns)
            y_variable = st.selectbox('Select y-axis variable', df.columns)

            # Check if x_variable is a date column
            if df[x_variable].dtype == 'datetime64[ns]':
                if selected_aggregation == 'Yearly':
                    df['Year'] = df[x_variable].dt.year
                    df_grouped = df.groupby('Year')[y_variable].sum()  # Aggregate by yearly sum
                    x_values = df_grouped.index
                    y_values = df_grouped.values
                elif selected_aggregation == 'Monthly':
                    df['Month'] = df[x_variable].dt.to_period('M')
                    df_grouped = df.groupby('Month')[y_variable].sum()  # Aggregate by monthly sum
                    x_values = df_grouped.index.to_timestamp()  # Convert period index back to timestamp
                    y_values = df_grouped.values
                elif selected_aggregation == 'Daily':
                    df['Date'] = df[x_variable].dt.date
                    df_grouped = df.groupby('Date')[y_variable].sum()  # Aggregate by daily sum
                    x_values = df_grouped.index
                    y_values = df_grouped.values
            else:
                # Check if x_variable is a numerical column
                if np.issubdtype(df[x_variable].dtype, np.number):
                    x_values = df[x_variable]
                    y_values = df[y_variable]
                else:
                    # Assign numerical values to categories
                    categories = df[x_variable].unique()
                    category_dict = {category: i for i, category in enumerate(categories)}
                    x_values = df[x_variable].map(category_dict)
                    y_values = df[y_variable]

            plt.figure(figsize=(8, 6))
            plt.bar(x_values, y_values)
            plt.xlabel(x_variable)
            plt.ylabel(y_variable)
            plt.title('Bar Plot')
            plt.tight_layout()
            plt.xticks(rotation=45)
            if df[x_variable].dtype == 'datetime64[ns]':
                if selected_aggregation == 'Yearly':
                    plt.xticks(x_values, x_values.astype(str))  # Format x-axis ticks as desired
                elif selected_aggregation == 'Monthly':
                    plt.xticks(x_values, x_values.strftime('%Y-%m'))  # Format x-axis ticks as desired
                elif selected_aggregation == 'Daily':
                    plt.xticks(x_values, x_values.astype(str))  # Format x-axis ticks as desired
            st.pyplot()

        elif selected_plot == 'histogram':
            st.subheader('Histogram')
            variable = st.selectbox('Select variable', df.columns)

            # Check if variable is a numerical column
            if np.issubdtype(df[variable].dtype, np.number):
                plt.figure(figsize=(8, 6))
                plt.hist(df[variable], bins='auto')
                plt.xlabel(variable)
                plt.ylabel('Frequency')
                plt.title('Histogram')
                plt.tight_layout()
                plt.xticks(rotation=45)
                st.pyplot()
            else:
                st.write('Selected variable is not numerical.')

        elif selected_plot == 'box':
            st.subheader('Box Plot')
            x_variable = st.selectbox('Select x-axis variable', df.columns)
            y_variable = st.selectbox('Select y-axis variable', df.columns)

            plt.figure(figsize=(8, 6))
            sns.boxplot(x=x_variable, y=y_variable, data=df)
            plt.xlabel(x_variable)
            plt.ylabel(y_variable)
            plt.title('Box Plot')
            plt.tight_layout()
            plt.xticks(rotation=45)
            st.pyplot()

        elif selected_plot == 'pie':
            st.subheader('Pie Chart')
            variable = st.selectbox('Select variable', df.columns)

            # Check if variable is a categorical column
            if df[variable].dtype == 'object':
                plt.figure(figsize=(8, 6))
                plt.pie(df[variable].value_counts(), labels=df[variable].unique())
                plt.title('Pie Chart')
                plt.tight_layout()
                plt.xticks(rotation=45)
                st.pyplot()
            else:
                st.write('Selected variable is not categorical.')

        # Add interactivity to the report
        st.subheader('Do you need to generate the report?')

        submit_button = st.button('Yes')
        
        if submit_button:
            # Display the profiling report using pandas_profiling
            st_profile_report(profile)

        st.subheader('Export Report')

        # Export the profiling report as HTML
        export_button = st.button('Export Report as HTML')

        if export_button:
            profile.to_file("profiling_report.html")
            st.success("Report exported successfully as HTML!, ", icon="✅")
            
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

if __name__ == '__main__':
    data_analysis_app()