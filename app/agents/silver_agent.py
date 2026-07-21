import os
import pandas as pd

from graph.state import PipelineState


class SilverAgent:

    def execute(self, state: PipelineState):

        bronze_file = os.path.join(
            "data",
            "bronze",
            os.path.basename(state.source_file)
        )

        df = pd.read_csv(bronze_file)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove rows with null values
        df = df.dropna()

        # Standardize column names
        df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

        os.makedirs("data/silver", exist_ok=True)

        silver_file = os.path.join(
            "data",
            "silver",
            "silver_" + os.path.basename(state.source_file)
        )

        df.to_csv(silver_file, index=False)

        state.recommendations.append(
            f"Silver layer created: {silver_file}"
        )

        return state