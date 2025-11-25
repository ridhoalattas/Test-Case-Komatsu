import logging
from abc import abstractmethod
from typing import Union

from langchain_core.messages.ai import AIMessage

from utilities.llm.abstract import AbstractLLM

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class AbstractGemini(AbstractLLM):
    def __init__(self, api_token: str, model: str, temperature: Union[float, int]):
        super().__init__(api_token=api_token, model=model, temperature=temperature)

    @abstractmethod
    def predict(self) -> AIMessage:
        pass
