import logging
from abc import ABC, abstractmethod
from typing import Union

import pandas as pd

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class AbstractPromptBuilder(ABC):
    def __init__(
        self,
        unit_name: str,
        data: Union[str, pd.DataFrame],
        data_definition: Union[str, pd.DataFrame],
    ):
        if isinstance(data, str):
            try:
                if data.split(".")[-1] != "csv":
                    logging.error("Data should be CSV data type!")
                    raise

                self.data = pd.read_csv(data)
            except Exception as e:
                logging.error(e)
        else:
            self.data = data

        if isinstance(data_definition, str):
            try:
                if data_definition.split(".")[-1] != "csv":
                    logging.error("Data Definition should be CSV data type!")
                    raise

                self.data_definition = pd.read_csv(data_definition)
            except Exception as e:
                logging.error(e)
        else:
            self.data_definition = data_definition
        self.unit_name = unit_name

    @abstractmethod
    def build_prompt(self) -> str:
        pass
