from typing import Union

import pandas as pd

from utilities.prompt_builder.abstract import AbstractPromptBuilder
from utilities.prompt_builder.template.template import TemplatePromptBuilder


class PromptBuilder(AbstractPromptBuilder, TemplatePromptBuilder):
    """
    A class to build a formatted prompt for mining operations analysis using sensor output data.

    This class takes a unit name, sensor data, and data definitions, then processes the data to
    create a summary prompt. The prompt includes descriptive statistics (mean, min, max) for each
    indicator along with its definition. It is designed to generate insights regarding engine
    performance, fuel efficiency, and potential operational concerns or anomalies.

    Attributes:
        unit_name (str): The name of the mining unit.
        data (Union[str, pd.DataFrame]): The sensor output data, either as a CSV file path or a DataFrame.
        data_definition (Union[str, pd.DataFrame]): Data definitions providing descriptions of each column,
            either as a CSV file path or a DataFrame.

    Methods:
        build_prompt():
            Constructs and returns the formatted prompt string including the unit name and summarized data.

    Raises:
        ValueError: If there is an error generating descriptive statistics from the data.
    """

    def __init__(
        self,
        unit_name: str,
        data: Union[str, pd.DataFrame],
        data_definition: Union[str, pd.DataFrame],
    ):
        super().__init__(
            unit_name=unit_name, data=data, data_definition=data_definition
        )

    def build_prompt(self) -> str:
        return self.template_mining_operation.format(
            unit_name=self.unit_name, all_data=self._get_text_from_value()
        )

    def _get_text_from_value(self) -> str:
        try:
            df_describe = (
                self.data.describe()
                .transpose()[["mean", "min", "max"]]
                .reset_index(names=["indicator"])
            )
        except Exception as e:
            raise ValueError(e)

        indicator_data = []
        for indicator in df_describe["indicator"].unique():
            ## Get value
            _df_describe = df_describe[df_describe["indicator"] == indicator]
            mean_agg = _df_describe["mean"].to_numpy()[0]
            min_agg = _df_describe["min"].to_numpy()[0]
            max_agg = _df_describe["max"].to_numpy()[0]

            ## Get definition
            _df_definition = self.data_definition[
                self.data_definition["Column"] == indicator
            ]
            definition = _df_definition["Definition"].to_numpy()[0]

            indicator_data.append(
                f"{indicator} ({definition}), min={min_agg};max={max_agg};average={mean_agg}"
            )

        return "\n".join(indicator_data)
