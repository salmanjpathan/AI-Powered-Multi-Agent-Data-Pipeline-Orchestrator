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

    return result.model_dump()