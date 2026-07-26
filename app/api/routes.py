from fastapi import APIRouter

from app.graph.workflow import graph
from app.graph.state import PipelineState
from app.schemas.pipeline_request import PipelineRequest

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "running"}


@router.post("/run-pipeline")
def run_pipeline(request: PipelineRequest):

    state = PipelineState(
        pipeline_id=request.pipeline_id,
        source_file=request.source_file,
        source_type=request.source_type,
    )

    result = graph.invoke(state)

    # If LangGraph returns a PipelineState object
    if isinstance(result, PipelineState):
        return result.model_dump()

    # If LangGraph returns a dictionary
    if isinstance(result, dict):

        # LangGraph often returns {"<node_name>": PipelineState}
        for value in result.values():
            if isinstance(value, PipelineState):
                return value.model_dump()

        return result

    # Fallback
    return {"result": str(result)}