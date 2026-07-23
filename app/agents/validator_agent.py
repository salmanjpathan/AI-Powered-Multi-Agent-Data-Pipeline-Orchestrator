import pandas as pd

from app.graph.state import PipelineState
from app.utils.logger import logger


class ValidatorAgent:

    def execute(self, state: PipelineState):

        try:
            logger.info("Validation started.")

            df = pd.read_csv(state.source_file)

            errors = []

            # Empty file check
            if df.empty:
                errors.append("Dataset is empty.")

            # Duplicate check
            duplicate_count = df.duplicated().sum()

            if duplicate_count > 0:
                errors.append(
                    f"Found {duplicate_count} duplicate records."
                )

            # Null check
            null_count = df.isnull().sum().sum()

            if null_count > 0:
                errors.append(
                    f"Found {null_count} null values."
                )

            # Age validation
            if "age" in df.columns:

                invalid_age = df[
                    (df["age"] < 0) |
                    (df["age"] > 120)
                ]

                if len(invalid_age) > 0:

                    errors.append(
                        f"Found {len(invalid_age)} records with invalid age."
                    )

            if errors:

                state.validation_status = "FAILED"
                state.errors.extend(errors)

                logger.warning(
                    f"Validation completed with {len(errors)} issue(s)."
                )

            else:

                state.validation_status = "SUCCESS"

                logger.info("Validation completed successfully.")

            return state

        except Exception as ex:

            logger.error(f"Validation failed: {str(ex)}")

            state.validation_status = "FAILED"
            state.errors.append(str(ex))

            return state