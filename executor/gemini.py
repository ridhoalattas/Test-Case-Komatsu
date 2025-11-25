import logging

from config.config import Config
from utilities.llm.gemini.gemini import GeminiLLM
from utilities.prompt_builder.prompt_builder import PromptBuilder

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class GeminiExecutor:
    def __init__(self, cfg: Config):
        self.config = cfg

    def run_gemini(self, data_path: str, data_definition_path: str, unit_name: str):
        gemini_llm = GeminiLLM(config=self.config)
        response = gemini_llm.predict(
            prompt=PromptBuilder(
                unit_name=unit_name,
                data=data_path,
                data_definition=data_definition_path,
            ).build_prompt()
        )

        logging.info(f"Prediction Success, Insight : {response.text}")
        return response
