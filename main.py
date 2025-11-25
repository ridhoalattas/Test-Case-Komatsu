import logging
import sys

import typer

from config.config import Config
from executor.gemini import GeminiExecutor

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)



def main():
    try:
        # initialize the app instance
        app = typer.Typer()

        cfg = Config().load()

    except Exception:
        sys.exit(1)

    @app.command()
    def gemini(
        data_path: str = typer.Option(
            ...,
            help="Directory where the dataset is located in local path",
        ),
        data_definition_path: str = typer.Option(
            ...,
            help="Directory where the dataset of definition is located in local path",
        ),
        unit_name: str = typer.Option(
            ...,
            help="Name of the unit name",
        ),
    ):
        try:
            ## Run Gemini
            GeminiExecutor(cfg=cfg).run_gemini(
                data_path=data_path,
                data_definition_path=data_definition_path,
                unit_name=unit_name,
            )

        except Exception as e:
            logging.error(f"Failed to run Gemini. Reason: {e}")
            sys.exit(1)

    app()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Failed to run pipeline: {e}")
