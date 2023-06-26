# Data Profile Generation App

The Data Analysis App is a web application that allows users to upload a CSV/Excel file, generate a data profiling report, and download the report. It provides an interactive interface to explore and analyze data using the pandas-profiling library.

## Features

- ```Upload a CSV/Excel file```: Users can upload a CSV/Excel file containing their data to the app. The file uploader widget allows for easy selection and upload of the file.

- ```Generate a Data Profiling Report```: The app generates a data profiling report for the uploaded CSV file using the pandas-profiling library. This report provides comprehensive insights into the data, including summary statistics, data types, missing values, correlations, and more.

- ```View the Profiling Report```: The generated profiling report is displayed using interactive visualizations and summary tables. Users can explore the report to gain a deeper understanding of their data and identify patterns and anomalies.

- ```Export the Profiling Report```: Users have the option to export the generated profiling report as an HTML file. This allows for easy sharing and further analysis of the report outside the app.

- ```Download the Exported Report```: The app provides a download link for the exported report. Users can click on the link to download the report and access it offline.

- ```Track Download Count```: The app tracks the number of times the report has been downloaded. The download count is displayed on the app, providing insights into the popularity and usage of the generated reports.

## Requirements

To run the Data Analysis App, you need to have the following requirements installed:

- ```Python 3.8 or above```: The app is built using Python, so you need to have a compatible version installed on your system.

- ```Streamlit```: Streamlit is used as the web application framework for building the user interface and serving the app.

- ```pandas```: The pandas library is used for reading and manipulating the uploaded CSV file and generating the data profiling report.

- ```pandas-profiling```: This library is used to generate the data profiling report with detailed statistics and visualizations.

- ```base64```: The base64 library is used to encode the exported report file for download.

- For more check [requirements](https://github.com/soopertramp/data-analysis-app/blob/main/requirements.txt)

## Installation

To install and run the Data Analysis App locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/data-analysis-app.git
   cd data-analysis-app
   
2. Create a virtual environment (optional but recommended):

    ```shell
    python3 -m venv env
    source env/bin/activate

3. Install the required packages:

    ```shell
    pip install -r requirements.txt

## Usage

### [Checkout the App](https://shorturl.at/tORT2)

To start the Data Analysis App, execute the following command:

    streamlit run data_profiling.py
    
The app will open in your default web browser, and you can begin using its features.

1. Upload a CSV file by clicking on the file uploader widget. Select the desired CSV file from your local machine.

2. Once the file is uploaded, click the "Generate Report" button. The app will process the data and generate a comprehensive data profiling report.

3. Explore the generated report by interacting with the visualizations and summary tables. Gain insights into your data and identify patterns, outliers, and potential data quality issues.

4. If you wish to save the report for further analysis or sharing, click the "Export Report as HTML" button. The app will export the report as an HTML file.

5. The app will display a success message indicating that the report has been exported. Additionally, the download count will be incremented, reflecting the number of times the report has been downloaded.

6. To download the exported report, click on the provided download link. The report will be downloaded to your local machine, allowing you to access it offline.

## Showcase

[Check Out The Demo File](https://soopertramp.github.io/data-profile-generation/)

## Contributing
Contributions to the Data Analysis App project are welcome! 

If you find any issues or have suggestions for improvement, please open an issue or submit a pull request. 

Feel free to contribute new features, fix bugs, or improve the documentation.

Contact Me - [LinkedIn](https://www.linkedin.com/in/pradeepchandra-reddy-s-c/)

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute the code for personal and commercial purposes BUT CREDIT is a MUST  
