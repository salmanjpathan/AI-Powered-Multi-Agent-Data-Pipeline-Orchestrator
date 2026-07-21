import os
import pandas as pd

from graph.state import PipelineState


class GoldAgent:

    def execute(self, state: PipelineState):

        silver_file = os.path.join(
            "data",
            "silver",
            "silver_" + os.path.basename(state.source_file)
        )

        df = pd.read_csv(silver_file)

        os.makedirs("data/gold", exist_ok=True)

        # Example business transformation:
        # Count records by first column
        first_column = df.columns[0]

        gold_df = (
            df.groupby(first_column)
              .size()
              .reset_index(name="record_count")
        )

        gold_file = os.path.join(
            "data",
            "gold",
            "gold_summary.csv"
        )

        gold_df.to_csv(gold_file, index=False)

        state.recommendations.append(
            f"Gold layer created: {gold_file}"
        )

        return state