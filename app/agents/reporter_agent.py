from datetime import datetime, timezone

from app.graph.state import PipelineState
from app.utils.logger import logger


class ReporterAgent:

    def execute(self, state: PipelineState):

        try:
            logger.info("Pipeline reporting started.")

            state.execution_end = datetime.now(timezone.utc)

            if (
                state.bronze_status == "RunResultState.SUCCESS"
                and state.silver_status == "RunResultState.SUCCESS"
                and state.gold_status == "RunResultState.SUCCESS"
            ):

                state.report_status = "SUCCESS"

                state.recommendations.append(
                    "Pipeline executed successfully."
                )

                logger.info("Pipeline executed successfully.")

            else:

                state.report_status = "FAILED"

                state.recommendations.append(
                    "One or more Databricks jobs failed."
                )

                logger.warning("Pipeline execution failed.")

            return state

        except Exception as ex:

            logger.error(f"Reporter Agent failed: {str(ex)}")

            state.report_status = "FAILED"
            state.errors.append(str(ex))

            return state