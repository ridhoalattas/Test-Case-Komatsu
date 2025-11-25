from langchain_core.messages.ai import AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from config.config_model import Config
from utilities.llm.gemini.abstract import AbstractGemini


class GeminiLLM(AbstractGemini):
    """
    GeminiLLM wraps the Google Gemini (ChatGoogleGenerativeAI) large language model interface.

    It initializes with configuration parameters, including the API token, model name,
    and temperature for sampling. Provides a predict method to generate responses
    given a textual prompt.

    Args:
        config (Config): Configuration object containing Gemini API credentials and model parameters.
    """

    def __init__(self, config: Config):
        super().__init__(
            api_token=config.gemini.api_token,
            model=config.gemini.model,
            temperature=config.gemini.temperature,
        )

    def predict(self, prompt: str) -> AIMessage:
        try:
            llm = ChatGoogleGenerativeAI(
                model=self.model,
                temperature=self.temperature,
                api_key=self.api_token,
            )
            response = llm.invoke(prompt)
            return response

        except Exception as e:
            raise Exception(e)
