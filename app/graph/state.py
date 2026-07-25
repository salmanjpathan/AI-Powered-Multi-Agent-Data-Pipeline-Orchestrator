from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class PipelineState(BaseModel):
    # ==========================
    # Pipeline Information
    # ==========================
    pipeline_id: str
    source_file: str
    source_type: str

    # ==========================
    # Pipeline Status
    # ==========================
    ingest_status: str = "PENDING"
    validation_status: str = "PENDING"
    transform_status: str = "PENDING"
    report_status: str = "PENDING"

    # ==========================
    # Databricks Job Details
    # ==========================
    bronze_run_id: Optional[str] = None
    silver_run_id: Optional[str] = None
    gold_run_id: Optional[str] = None

    bronze_status: Optional[str] = None
    silver_status: Optional[str] = None
    gold_status: Optional[str] = None

    # ==========================
    # Metadata
    # ==========================
    retry_count: int = 0
    row_count: int = 0
    file_hash: str = ""

    execution_start: datetime = Field(default_factory=datetime.utcnow)
    execution_end: Optional[datetime] = None

    # ==========================
    # AI Reporting
    # ==========================
    ai_summary: str = ""
    severity: str = ""
    business_impact: str = ""

    # ==========================
    # Logs
    # ==========================
    errors: List[str] = Field(default_factory=list)
    recommendations: List[str] = Field(default_factory=list)