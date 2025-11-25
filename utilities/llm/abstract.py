import logging
from abc import ABC, abstractmethod
from typing import Union

from langchain_core.messages.ai import AIMessage

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class AbstractLLM(ABC):
    def __init__(self, api_token: str, model: str, temperature: Union[float, int]):
        self.api_token = api_token
        self.model = model
        self.temperature = temperature

    @abstractmethod
    def predict(self) -> AIMessage:
        pass
