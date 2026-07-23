import os
import shutil

from app.graph.state import PipelineState
from app.config.settings import settings
from app.utils.logger import logger


class BronzeAgent:

    def execute(self, state: PipelineState):

        try:
            logger.info("Bronze layer started.")

            os.makedirs(settings.bronze_path, exist_ok=True)

            destination = os.path.join(
                settings.bronze_path,
                os.path.basename(state.source_file)
            )

            shutil.copy2(state.source_file, destination)

            state.recommendations.append(
                f"Bronze layer created: {destination}"
            )

            logger.info(f"Bronze layer created successfully: {destination}")

            return state

        except Exception as ex:
            logger.error(f"Bronze layer failed: {str(ex)}")
            state.errors.append(str(ex))
            return state