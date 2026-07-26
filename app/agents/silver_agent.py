from app.graph.state import PipelineState
from app.databricks.jobs import run_silver_job
from app.utils.logger import logger


class SilverAgent:

    def execute(self, state: PipelineState):

        try:

            logger.info("Starting Silver Databricks Job...")

            result = run_silver_job()

            state.silver_run_id = result["run_id"]
            state.silver_status = result["status"]

            logger.info("Silver Job Completed Successfully")

            return state

        except Exception as ex:

            logger.error(str(ex))

            state.errors.append(str(ex))
            state.silver_status = "FAILED"

            return state