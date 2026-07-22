import os
import pandas as pd

from graph.state import PipelineState
from config.settings import settings
from utils.logger import logger


class SilverAgent:

    def execute(self, state: PipelineState):

        try:
            logger.info("Silver layer started.")

            bronze_file = os.path.join(
                settings.bronze_path,
                os.path.basename(state.source_file)
            )

            df = pd.read_csv(bronze_file)

            # Remove duplicate rows
            df = df.drop_duplicates()

            # Remove rows with null values
            df = df.dropna()

            # Standardize column names
            df.columns = [
                col.strip().lower().replace(" ", "_")
                for col in df.columns
            ]

            os.makedirs(settings.silver_path, exist_ok=True)

            silver_file = os.path.join(
                settings.silver_path,
                "silver_" + os.path.basename(state.source_file)
            )

            df.to_csv(silver_file, index=False)

            state.transform_status = "SUCCESS"

            state.recommendations.append(
                f"Silver layer created: {silver_file}"
            )

            logger.info(f"Silver layer created successfully: {silver_file}")

            return state

        except Exception as ex:
            logger.error(f"Silver layer failed: {str(ex)}")
            state.errors.append(str(ex))
            state.transform_status = "FAILED"
            return state