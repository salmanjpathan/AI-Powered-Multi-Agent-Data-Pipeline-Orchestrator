from datetime import datetime

from graph.state import PipelineState
from utils.logger import logger


class ReporterAgent:

    def execute(self, state: PipelineState):

        try:
            logger.info("Pipeline reporting started.")

            state.execution_end = datetime.now()

            if (
                state.ingest_status == "SUCCESS"
                and state.validation_status == "SUCCESS"
                and state.transform_status == "SUCCESS"
            ):
                state.report_status = "SUCCESS"

                state.recommendations.append(
                    "Pipeline executed successfully."
                )

                logger.info("Pipeline executed successfully.")

            else:
                state.report_status = "FAILED"

                state.recommendations.append(
                    "Review pipeline errors before rerunning."
                )

                logger.warning("Pipeline execution failed.")

            return state

        except Exception as ex:
            logger.error(f"Reporter Agent failed: {str(ex)}")
            state.errors.append(str(ex))
            state.report_status = "FAILED"
            return state