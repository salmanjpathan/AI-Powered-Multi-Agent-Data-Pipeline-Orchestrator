from app.graph.state import PipelineState
from app.utils.logger import logger
from app.databricks.jobs import run_bronze_job


class BronzeAgent:

    def execute(self, state: PipelineState):

        try:

            logger.info("Starting Bronze Layer...")

            result = run_bronze_job()

            state.ingest_status = "SUCCESS"

            state.bronze_run_id = str(result["run_id"])
            state.bronze_status = result["status"]

            state.recommendations.append(
                f"Bronze Databricks Job Completed | Run ID : {state.bronze_run_id}"
            )

            logger.info(
                f"Bronze Job Completed Successfully | Run ID : {state.bronze_run_id}"
            )

            return state

        except Exception as ex:

            logger.error(str(ex))

            state.ingest_status = "FAILED"

            state.errors.append(str(ex))

            return state