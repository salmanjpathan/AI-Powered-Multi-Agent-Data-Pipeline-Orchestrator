from typing import List
from pydantic import BaseModel, Field
from datetime import datetime


class PipelineState(BaseModel):
    pipeline_id: str

    source_file: str
    source_type: str

    ingest_status: str = "PENDING"
    validation_status: str = "PENDING"
    transform_status: str = "PENDING"
    report_status: str = "PENDING"

    retry_count: int = 0

    row_count: int = 0

    file_hash: str = ""

    execution_start: datetime = Field(
        default_factory=datetime.utcnow
    )

    execution_end: datetime | None = None

    errors: List[str] = []

    recommendations: List[str] = []