from pydantic import BaseModel


class PipelineRequest(BaseModel):
    pipeline_id: str
    source_file: str
    source_type: str