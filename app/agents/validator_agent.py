import pandas as pd

from graph.state import PipelineState


class ValidatorAgent:

    def execute(self, state: PipelineState):

        try:
            df = pd.read_csv(state.source_file)

            errors = []

            # Empty file check
            if df.empty:
                errors.append("Dataset is empty.")

            # Duplicate check
            duplicate_count = df.duplicated().sum()
            if duplicate_count > 0:
                errors.append(f"Found {duplicate_count} duplicate records.")

            # Null check
            null_count = df.isnull().sum().sum()
            if null_count > 0:
                errors.append(f"Found {null_count} null values.")

            # Age validation (if column exists)
            if "age" in df.columns:
                invalid_age = df[(df["age"] < 0) | (df["age"] > 120)]

                if len(invalid_age) > 0:
                    errors.append(
                        f"Found {len(invalid_age)} records with invalid age."
                    )

            if errors:
                state.validation_status = "FAILED"
                state.errors.extend(errors)
            else:
                state.validation_status = "SUCCESS"

            return state

        except Exception as ex:
            state.validation_status = "FAILED"
            state.errors.append(str(ex))
            return state