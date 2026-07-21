from datetime import datetime

from graph.state import PipelineState


class ReporterAgent:

    def execute(self, state: PipelineState):

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
        else:
            state.report_status = "FAILED"
            state.recommendations.append(
                "Review pipeline errors before rerunning."
            )

        return state