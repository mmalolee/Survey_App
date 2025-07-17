# Survey Analysis App

### A small data project that cleans, translates, and explores answers from a welcome survey. The final results are shown in an interactive web app built with `Streamlit`.

### Files:

* data.csv - original dataset.
* data_prepared.csv - prepared dataset for visualization.
* research.ipynb - notebook containing all data preparation steps.
* app.py - final streamlit application code.

## Goal:

Explore answers from a welcome survey and show patterns in:
- gender,
- age,
- education level,
- favorite animal,
- favorite places,
- taste preferences (sweet or salty).

## Technologies:

- pandas - data cleaning and manipulation,
- matplotlib, seaborn - charts,
- faker - generating random names,
- streamlit - web application.

## Project Structure: 

- survey_app_project
    - app.py
    - data_prepared.csv
    - data.csv
    - readme.md
    - requirements.txt
    - research.ipynb

## Running the Application (local environment)

- Open `app.py` and project's folder in VSCode.
- Open the terminal with *CTRL + Shift + `*
- Create a Conda environment using Python version 3.11.11.
- Activate the Conda environment: `conda activate env_name`.
- Install required packages from the requirements.txt file:
    - `cd path_to_project_folder`
    - `pip install -r requirements.txt`
- In the terminal, run the command: `streamlit run app.py`.
- Save code using *Ctrl + S*

## Running the Application (Streamlit Community Cloud)

- The app has been deployed using Streamlit Community Cloud: [Streamlit Survey App](https://surveyapp.streamlit.app/)

## Analysis Steps

- Translated answers from Polish to English.
- Filled missing values with `"No data"`.
- Made sure all answers look good (capital letters).
- Generated and assigned fake names to the `"name"` column.
- Saved data to new `.csv` file. 

To see full process click [here](research.ipynb)

## App

The app has two tabs: one for metrics and one for charts. The sidebar includes several filters (gender, age range, education level, favorite animal, preferred taste, favorite place) that let you change the data dynamically.

You can:
- see which animals are liked most,
- compare answers by gender,
- see how people of different ages answered.