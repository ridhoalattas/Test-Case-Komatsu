from pathlib import Path

import pandas as pd
import streamlit as st

from config.config import Config
from utilities.llm.gemini.gemini import GeminiLLM
from utilities.prompt_builder.prompt_builder import PromptBuilder


def load_file(path):
    p = Path(path)
    if p.exists():
        data = pd.read_csv(path)
        return data
    else:
        return None


def main():
    st.title("Test Case Komatsu HD785-7")

    # Input paths
    data = st.text_input("Enter Data Path")
    data_definition = st.text_input("Enter Data Definition Path")
    unit_name = st.text_input("Enter Unit Name")

    if st.button("Get Insight"):
        if not data or not data_definition:
            st.error("Please provide both file paths")
            return

        content1 = load_file(data)
        content2 = load_file(data_definition)

        if content1 is None:
            st.error(f"Data not found: {data}")
        else:
            st.success(f"Data: {data}")

        if content2 is None:
            st.error(f"Data Definition not found: {data_definition}")
        else:
            st.success(f"Loaded Data Definition: {data_definition}")

        st.success(f"Loaded Unit Name : {unit_name}")

        config = Config().load()
        gemini_llm = GeminiLLM(config=config)
        response = gemini_llm.predict(
            prompt=PromptBuilder(
                unit_name=unit_name, data=data, data_definition=data_definition
            ).build_prompt()
        )
        st.success(f"Success get Insight: {response.text}")


if __name__ == "__main__":
    main()
