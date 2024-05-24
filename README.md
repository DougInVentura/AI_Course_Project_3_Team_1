# AI_Course_Project_3_Team_1

## AI Assisted Data Processing, EDA, and Graphing

## Introduction

Welcome to our project repository! This project aims to create a user-friendly, web-based application that facilitates automatic generation of custom graphs for any given tabular dataset through simple voice commands or text prompts. This technology will enable users to engage with data analysis in a more intuitive and efficient manner, significantly reducing the manual effort involved in data processing. Our focus has been on machine learning and natural language processing (NLP) to achieve seamless data visualization and interaction.

## Table of Contents

- [Project Setup](#project-setup)
- [Data Collection and Cleaning](#data-collection-and-cleaning)
- [Model Implementation and Optimization](#model-implementation-and-optimization)
- [Results](#results)
- [Future Work](#future-work)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Usage Instructions](#usage-instructions)

## Built With
- **Visual Studio Code** - Source code editor used for development.
- **GitHub Copilot** - AI assistant that helps in writing better code.
- **ChatGPT** - AI model for generating documentation and guidance.
- **Perplexity** - AI assistant that helps generate and write cleaner code.
- **Streamlit** - Web framework tailored for data science applications, allowing Python developers to easily build and deploy web applications. Streamlit serves as the foundation for our web-based interface, ensuring a seamless user experience.

## Location of the Code and Write Up

The main file is located in the root directory of the Git repository. The file name is `Main_Page_for_Plotly.py`.

## Getting Started

Follow the steps below to get this project up and running on your local machine.
```sh
$ streamlit run "Main_Page_for_Plotly.py"
```

### Prerequisites

The following are prerequisites for this project. Instructions for pip installation are provided for each package.

- **Python** - This project was created using Python version 3.11.5. Package compatibility has not been tested with other versions of Python. Refer to this [DigitalOcean tutorial](https://www.digitalocean.com/community/tutorials/install-python-windows-10) for Python installation.

- **Streamlit**
  ```sh
  pip install streamlit
  ```

- **Streamlit Mic Recorder**
  ```sh
  pip install streamlit-mic-recorder
  ```

- **Pandas**
  ```sh
  pip install pandas
  ```

- **TensorFlow**
  ```sh
  pip install tensorflow[and-cuda]  # if using a compatible GPU
  # or
  pip install tensorflow-cpu  # if using only your CPU
  ```

- **Scikit-learn**
  ```sh
  pip install -U scikit-learn
  # Note: Scikit-learn installation encourages the use of a virtual environment. See https://scikit-learn.org/stable/install.html
  ```

- **Numpy**
  ```sh
  pip install numpy
  ```

- **Keras**
  ```sh
  # Keras will be automatically installed when you install TensorFlow.
  ```

### Installation and Running

In addition to setting up Python and the required packages, perform the following steps.

1. Clone the repository on your local machine:
   ```sh
   git clone https://github.com/DougInVentura/AI_Course_Project_3_Team_1
   ```

2. Open the folder corresponding to the app where you installed it using the repo clone above.

3. Open the file `Main_Page_for_Plotly.py`.

4. Make the desired modifications. Run cell by cell or run the entire Jupyter notebook.

## Data Collection and Cleaning

Describe the sources of your data and the methodology used to clean and preprocess it. This section includes:
- Data sources
- Key steps in data cleaning and preprocessing
- Exporting the cleaned data for modeling

## Model Implementation and Optimization

### Application / Model Optimization
a. Per the accepted project proposal, we did not do a standard model that needed hyper tuning, etc. Instead, we did an application that used text (or voice if that comes together) to generate human graphing requests on any data set that is in “tall” form, like a normalized database table or (tall) CSV file.

b. Optimization of the application.
   - In the LangGraph workflow, both a system prompt and a user-generated prompt were passed to the LLM. The system message and the user prompt were used on a variety of data. The application takes the code generated by the LLM and parses it out from the returned LLM message. In turn, this is pushed into a graphing file, that Streamlit can then call to generate the graphs. The system message was continuously revised since many of the initial graphs would fail. This tuning was essential to improve performance.
   - The initial one-page implementation was too busy. Hence the “Select data...” page was made the initial request generation page and a “create_graphs...” page was added to process subsequent graphing requests.
   - The graphing page was improved by writing out the actual request before the generated graphs. To prevent Streamlit write functions from failing, the user request was stripped of leading and trailing spaces and line feeds.
   - Complex graphing requests can sometimes fail. So there is a ‘save graph file’ as well as a restore graph file button to undo changes (if the graph file was saved prior to processing the new request).
   - While originally envisioned for use by non-Python programmers, the occasional failures might be frustrating. For a Python programmer, they can go into the code and correct the usually simple mistakes made by the LLM.
   - 3D plotting was added using its own page. The user specifies 3 or more columns, as well as an optional ‘colorby’ variable and the application generates a rotatable and resizable 3D plot for all combinations of the columns specified. By all combinations, we mean that if three columns are specified, there is only one combination, so one 3D graph is produced. If the user specifies four columns, then three graphs are produced (if the four columns are A, B, C, and D, then the 3D plots would be {x,y,z} includes [{A, B, C}, {A, B, D}, {B, C, D}]. If five columns are selected, then six graphs would be produced. Limitation: The 3D graphing routine seems to stop generating images if too many columns are selected. However, the request can be broken down into smaller bites to avoid an issue.
   - Considerable debugging was needed since the Streamlit session state was not visible in the LangGraph workflow. Global variables were used to overcome these issues.
   - Management of the Streamlit session state between pages with the different options was probably the most challenging aspect of this project, requiring considerable optimization and debugging.
   - The application was updated to allow the user to specify alternative graphing files. The default file is over-written each time the application is used. However, if alternative graphing files are specified, these are persistent saving work.

### Application / Model Performance
a. The application’s performance in its final state was tested with four datasets. PDFs of some of the testing are saved in the data directory as PDFs. See the data directory. The file is called “Application Performance Score Card.xlsx”.
b. Overall, of 23 requests, 20 worked the first time. After adjustments, 2 of the 3 failures passed on subsequent testing after minor changes to the system prompt and other minor Python code changes.

## Usage Instructions

### Plotly Usage Instructions
**Project 3: ASU AI Course.**
**Team: Chris Alvarez, Geoff McDaniel, and Doug Francis**

1. **Run the Application**
   - In your terminal, navigate to the directory containing the file `main_page_for_plotly.py`.
   - Execute the following command and hit enter:
     ```sh
     streamlit run "Main_Page_for_plotly.py"
     ```
   - Your browser should open (tested in Chrome) and display the application interface.

2. **Select the Data File**
   - Click on the button labeled "Click Here to select...".
   - On the next screen, click the "Browse file" button.
   - Navigate to the directory containing your clean CSV file (note: only CSV files are supported, no XLSX files).
   - Select the file and click "Open".
     - Ensure the table format is "tall" (normalized database table or tall CSV format).

3. **View Dataframe**
   - After loading the data, a scrollable view of your dataframe will be displayed.
   - Below the dataframe, you will see two buttons:
     - **Left Button**: View dataframe info (equivalent to `df.info()` in Python).
     - **Right Button**: View the shape of the data or the value counts.

4. **Specify a Graphing File (Optional)**
   - If you do not want to use the default graphing page (`3_the_graphs.py`), you can specify a new graphing file name.
     - Requirements for the file name:
       - Must start with a number followed by an underscore.
       - Should end in `.py`.
       - Use only letters or digits after the digit-underscore and before the `.py` extension.
     - After typing the file name, hit `Control-Enter`.
     - You may need to click on the "Enter your graphing request" text input area for the action to start.

5. **Enter Your Graphing Request**
   - Enter your graphing request in the input area. Note: Prompt engineering is important. Use single quotes, but NO DOUBLE QUOTES.
   - Example requests:
     - Generate a stacked bar chart of counts of `payment_method`. The bottom part of the stacked bar should be for `churn=0` versus the top of the stacked bar should be for `churn=1`.
     - Create histograms for `tenure`, `number_customer_service_calls`, and `internet_charge_per_min`. For `internet_charge_per_min`, limit the x-axis to 0.03.
     - Create overlapping histograms for `number_customer_service_calls` for `churn=0` versus `churn=1`. Convert the data to relative frequency due to the larger number of rows where `churn=0`.
     - Generate overlapping histograms for the variable `fgp` for `Player = Jordan` versus `Player = Lebron`. Add an annotation for the average `fgp` for `Player = Jordan` versus average `fgp` for `Player = Lebron`.
     - Generate a scatter plot with two series. Series 1: `x= game_abs` and `y = pts` for `Player = Jordan` and Series 2: `x= game_abs` and `y = pts` for `Player = Lebron`. Use `sklearn` library to generate a regression line for both series. Annotate the regression lines with the Players.
   - After typing your request, hit `Control-Enter`.

6. **Generate the Graph**
   - After entering your request and hitting `Control-Enter`, a button labeled "Request Received... Click to Produce graph(s)" will appear.
   - Click on this button to generate your chart.

7. **View and Manage Graphs**
   - This will take you to the `create_graphs` page.
   - You have the option to:
     - Click on "Click to view the page with the graphs" to view the generated graphs.
     - Click on "Click to generate another graph" to create additional graphs.
   - If the default graphing file was used, you will see the `the_graphs` page with your requested graphs.
   - Use the buttons on the graphing page to view dataframe information, shape, and value counts.

8. **Iterate Graph Requests**
   - Use the gray sidebar on the left-hand side of the screen to select "Create graphs" for creating more graphs.
   - If the sidebar is hidden, click the arrow on the upper left corner to show it.
   - Enter a new graphing request and hit `Control-Enter`.
   - To view your new graph, select `the graphs` from the sidebar.

9. **Quit the Application**
   - When you are done, hit `Control-C` in your terminal to quit the application.
   - After executing `Control-C`, close the web page in the browser.

By following these steps, you will be able to effectively use the application to generate and view custom graphs based on your dataset.
## Visualizations

### 3D Plotting 

![3D Plot](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/168fb6df-ace1-4ece-9c68-793fab614450)

### Graphs

![Graph](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/c5c5dc4c-9741-4f9f-92d9-c8a9057752ae)

### Streamlit Automated Graphing

![Screenshot 2024-05-22 at 7 14 32 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/cc39a366-2042-444d-9eed-cf81c00da7a7)
![Screenshot 2024-05-22 at 7 14 47 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/56976753-fcc9-43ad-85d0-05e84d7a527c)
![Screenshot 2024-05-22 at 7 15 18 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/feb968fb-d651-49cb-a444-d6b90e534bcb)
![Screenshot 2024-05-22 at 7 15 37 PM](https://github.com/DougInVentura/AI_Course_Project_3_Team_1/assets/153215625/0d7264c7-1f3b-46a7-bb23-50e39ee2edff)


## Future Work

- Exploring additional data sources
- Trying different model architectures or algorithms


## Authors

- **Chris Alvarez** - Presentation visualization, data collection, preprocessing, and application deployment
- **Doug Francis** - Feature/data engineering, model evaluation, model deployment, and documentation
- **Geoff McDaniel** - Feature/data engineering, model evaluation, and voice capture widget deployment

## License

This project is not licensed and is available for educational and non-commercial use only.

## Acknowledgments

Big shoutout to our instructor Firas, and of course, Sean, for their awesome support with our project. Our professors laid down the basics, making sure we got the hang of what we needed for Project 3. All together, they've been the dream team behind our data analysis skills, and we couldn't be more grateful.
