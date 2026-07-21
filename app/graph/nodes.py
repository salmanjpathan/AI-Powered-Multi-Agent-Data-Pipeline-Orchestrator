from graph.state import PipelineState

from agents.ingest_agent import IngestAgent
from agents.bronze_agent import BronzeAgent
from agents.validator_agent import ValidatorAgent
from agents.silver_agent import SilverAgent
from agents.reporter_agent import ReporterAgent
from agents.ai_dq_agent import AIDataQualityAgent
from agents.gold_agent import GoldAgent


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


def run_report(state: PipelineState):
    agent = ReporterAgent()
    return agent.execute(state)


def run_ai_report(state: PipelineState):
    agent = AIDataQualityAgent()
    return agent.execute(state)

def run_gold(state: PipelineState):
    agent = GoldAgent()
    return agent.execute(state)