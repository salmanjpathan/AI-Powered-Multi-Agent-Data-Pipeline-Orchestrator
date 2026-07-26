from app.graph.state import PipelineState

from app.agents.ingest_agent import IngestAgent
from app.agents.bronze_agent import BronzeAgent
from app.agents.validator_agent import ValidatorAgent
from app.agents.silver_agent import SilverAgent
from app.agents.gold_agent import GoldAgent
from app.agents.reporter_agent import ReporterAgent
from app.agents.ai_dq_agent import AIDataQualityAgent


def run_ingest(state: PipelineState):
    return IngestAgent().execute(state)


def run_bronze(state: PipelineState):
    return BronzeAgent().execute(state)


def run_validate(state: PipelineState):
    return ValidatorAgent().execute(state)


def run_silver(state: PipelineState):
    return SilverAgent().execute(state)


def run_gold(state: PipelineState):
    return GoldAgent().execute(state)


def run_report(state: PipelineState):
    return ReporterAgent().execute(state)


def run_ai_report(state: PipelineState):
    return AIDataQualityAgent().execute(state)