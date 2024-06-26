# AI_Course_Project_3_Team_1

## AI Assisted Data Processing, EDA, and Graphing

## Introduction

Welcome to our project repository! This project aims to create a user-friendly, web-based application that facilitates automatic generation of custom graphs for any given tabular dataset through simple voice commands or text prompts. This technology will enable users to engage with data analysis in a more intuitive and efficient manner, significantly reducing the manual effort involved in data processing. Our focus has been on machine learning and natural language processing (NLP) to achieve seamless data visualization and interaction.

## Table of Contents

- [Project Setup](#project-setup)
- [Data Collection and Cleaning](#data-collection-and-cleaning)
- [Model Implementation and Optimization](#model-implementation-and-optimization)
- [Usage Instructions](#usage-instructions)
- [Future Work](#future-work)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Built With
- **Visual Studio Code** - Source code editor used for development.
- **GitHub Copilot** - AI assistant that helps in writing better code.
- **ChatGPT** - AI model for generating documentation and guidance.
- **Perplexity** - AI assistant that helps generate and write cleaner code.
- **Streamlit** - Web framework tailored for data science applications, allowing Python developers to easily build and deploy web applications. Streamlit serves as the foundation for our web-based interface, ensuring a seamless user experience.
- **Canva** - Used for live slideshow presentation.

- PowerPoint link (https://www.canva.com/design/DAGFWfztwLY/PEkUNIX4wwan-Fl_UReDIQ/view?utm_content=DAGFWfztwLY&utm_campaign=designshare&utm_medium=link&utm_source=editor)

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

3. Follow the Usage Instructions in the app/data directory titled "Plotly Usage Instructions.docx"

## Data Collection

- Data sources
Various data sources were used in this process. However, this project was more about developing a automated graphing application rather than a model.

Data sources used for development include
- churn_clean.csv
- jordan vs Lebron.csv
- jordan vs leborn2.csv
- labtops.csv
- winequality-red fixed.csv

All data sources are in the main repo app/data directory

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

Add a Streamlit page to generate data tables such as pivot tables and summaries. This would make the application more generally useful. Additional work would be to add a conditional edge in the LangGraph workflow to check the code generated by the LLM. If the check did not pass, the application could loop back to re-generate code in the LLM.


## Authors

- **Chris Alvarez** - Presentation visualization, data collection, preprocessing, and application deployment
- **Doug Francis** - Feature/data engineering, model evaluation, model deployment, and documentation
- **Geoff McDaniel** - Feature/data engineering, model evaluation, and voice capture widget deployment

## License

This project is not licensed and is available for educational and non-commercial use only.

## Acknowledgments

Big shoutout to our instructor Firas, and of course, Sean, for their awesome support with our project. Our professors laid down the basics, making sure we got the hang of what we needed for Project 3. All together, they've been the dream team behind our data analysis skills, and we couldn't be more grateful.
