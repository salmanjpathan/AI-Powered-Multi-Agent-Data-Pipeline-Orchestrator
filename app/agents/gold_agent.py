import os
import pandas as pd

from app.graph.state import PipelineState
from app.config.settings import settings
from app.utils.logger import logger


class GoldAgent:

    def execute(self, state: PipelineState):

        try:
            logger.info("Gold layer started.")

            silver_file = os.path.join(
                settings.silver_path,
                "silver_" + os.path.basename(state.source_file)
            )

            df = pd.read_csv(silver_file)

            os.makedirs(settings.gold_path, exist_ok=True)

            # Example business aggregation
            first_column = df.columns[0]

            gold_df = (
                df.groupby(first_column)
                .size()
                .reset_index(name="record_count")
            )

            gold_file = os.path.join(
                settings.gold_path,
                "gold_summary.csv"
            )

            gold_df.to_csv(gold_file, index=False)

            state.recommendations.append(
                f"Gold layer created: {gold_file}"
            )

            logger.info(f"Gold layer created successfully: {gold_file}")

            return state

        except Exception as ex:
            logger.error(f"Gold layer failed: {str(ex)}")
            state.errors.append(str(ex))
            return state