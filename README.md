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
    <pre>
    pip install -r requirements.txt
    </pre>
2. Jupyter Notebook (EDA + prediction):
    main.ipynb contains EDA on SMR and Fuel Rate, anomaly discussion, and prediction using GeminiChatBot with custom prompts
3. Python CLI:
    main.py can be executed with Typer CLI arguments:
    <pre>
    python3 main.py --data-path=data/data.csv --data-definition-path=data/data_definition.csv --unit-name=Komatsu-HD785-7
    </pre>
4. Streamlit UI Demo:
    main_ui.py provides a simple UI to input data, data definition, and unit name, then retrieve insights:
    <pre>
    streamlit run main_ui.py
    </pre>

## **Architecture :**
1. Data Sources
    - Data (CSV)
    - Data Definition (CSV)
    - Unit Name
2. Preprocessing & EDA (main.ipynb)
    - Data loading, cleaning, and exploration
    - Anomaly detection on SMR & Fuel Rate
    - Visualization & summary statistics
    - Get insight from data
3. Prompt Building (PromptBuilder module)
    - Constructs domain-specific prompts for mining operation insights based on Komatsu case context
    - Uses Data Definition to enrich prompts with proper terminology
4. Language Model Interface (GeminiChatBot)
    - Connects to Gemini Chat API with provided API key
    - Sends generated prompts
    - Receives predicted insights
5. Application Interfaces
    - CLI Tool (main.py): Runs analysis end-to-end with parameters to get insights
    - Jupyter Notebook (main.ipynb): For step-by-step EDA and prediction experiments
    - Streamlit UI (main_ui.py): Interactive frontend for non-technical users to get insights