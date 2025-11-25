# **Project Summary**
    I have developed a system for analyzing Komatsu HD785-7 mining sensor data with multiple components and capabilities:

## **Data Inputs :**
    - Data: Numerical sensor output data from Komatsu HD785-7
    - Data Definition: Metadata and definitions for the sensor data fields
    - Unit Name : for this case i used Komatsu-HD785-7

## **Methodology :**
    1. Used LangChain framework to build insights extraction pipelines
    2. Developed a custom PromptBuilder to generate targeted prompts based on mining operations context from the Komatsu HD785-7 case
    3. Used GeminiChatBot as the underlying language model interface, chosen for easy API key usage and model improvement potential

## **How to Run :**
    1. Install dependencies:
        ```shell
        pip install -r requirements.txt
        ```
    2. Jupyter Notebook (EDA + prediction):
        main.ipynb contains EDA on SMR and Fuel Rate, anomaly discussion, and prediction using GeminiChatBot with custom prompts
    3. Python CLI:
        main.py can be executed with Typer CLI arguments:
        ```python
        python3 main.py --data-path=data/data.csv --data-definition-path=data/data_definition.csv --unit-name=Komatsu-HD785-7
        ```
    4. Streamlit UI Demo:
        main_ui.py provides a simple UI to input data, data definition, and unit name, then retrieve insights:
        ```python
        streamlit run main_ui.py
        ```