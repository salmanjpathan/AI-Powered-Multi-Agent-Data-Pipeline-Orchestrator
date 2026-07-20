import os
import pandas as pd

from graph.state import PipelineState


class TransformAgent:

    def execute(self, state: PipelineState):

        try:
            df = pd.read_csv(state.source_file)

            # Remove duplicates
            df = df.drop_duplicates()

            # Remove rows with nulls
            df = df.dropna()

            # Standardize column names
            df.columns = [col.lower().strip() for col in df.columns]

            output_path = "data/silver/clean_sales.csv"

            os.makedirs("data/silver", exist_ok=True)

            df.to_csv(output_path, index=False)

            state.transform_status = "SUCCESS"

            return state

        except Exception as ex:
            state.transform_status = "FAILED"
            state.errors.append(str(ex))
            return state