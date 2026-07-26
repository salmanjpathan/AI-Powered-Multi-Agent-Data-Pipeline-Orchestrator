from app.graph.state import PipelineState
from app.databricks.jobs import run_gold_job
from app.utils.logger import logger


class GoldAgent:

    def execute(self, state: PipelineState):

        try:
            logger.info("Starting Gold Databricks Job...")

            result = run_gold_job()

            state.gold_run_id = result["run_id"]
            state.gold_status = result["status"]

            if state.gold_status == "RunResultState.SUCCESS":
                logger.info("Gold Job completed successfully.")

                state.recommendations.append(
                    "Gold layer created successfully in Databricks."
                )
            else:
                logger.error("Gold Job failed.")

                state.errors.append("Gold Databricks Job Failed")

            return state

        except Exception as ex:

            logger.error(f"Gold Agent failed: {str(ex)}")

            state.gold_status = "FAILED"
            state.errors.append(str(ex))

            return state