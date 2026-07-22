from graph.state import PipelineState
from services.metadata_service import MetadataService
from utils.logger import logger


class IngestAgent:

    def execute(self, state: PipelineState) -> PipelineState:

        try:
            logger.info("Ingestion started.")

            file_hash = MetadataService.generate_file_hash(
                state.source_file
            )

            row_count = MetadataService.get_row_count(
                state.source_file
            )

            state.file_hash = file_hash
            state.row_count = row_count

            state.ingest_status = "SUCCESS"

            logger.info(
                f"Ingestion completed successfully. Rows: {row_count}"
            )

        except Exception as ex:

            logger.error(f"Ingestion failed: {str(ex)}")

            state.ingest_status = "FAILED"
            state.errors.append(str(ex))

        return state