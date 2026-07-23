from app.graph.state import PipelineState

from app.agents.ingest_agent import IngestAgent
from app.agents.bronze_agent import BronzeAgent
from app.agents.validator_agent import ValidatorAgent
from app.agents.silver_agent import SilverAgent
from app.agents.transform_agent import TransformAgent
from app.agents.gold_agent import GoldAgent
from app.agents.reporter_agent import ReporterAgent
from app.agents.ai_dq_agent import AIDataQualityAgent


def run_ingest(state: PipelineState):
    agent = IngestAgent()
    return agent.execute(state)


def run_bronze(state: PipelineState):
    agent = BronzeAgent()
    return agent.execute(state)


def run_validate(state: PipelineState):
    agent = ValidatorAgent()
    return agent.execute(state)


def run_silver(state: PipelineState):
    agent = SilverAgent()
    return agent.execute(state)


def run_transform(state: PipelineState):
    agent = TransformAgent()
    return agent.execute(state)


def run_gold(state: PipelineState):
    agent = GoldAgent()
    return agent.execute(state)


def run_report(state: PipelineState):
    agent = ReporterAgent()
    return agent.execute(state)


def run_ai_report(state: PipelineState):
    agent = AIDataQualityAgent()
    return agent.execute(state)