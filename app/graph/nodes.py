from graph.state import PipelineState

from agents.ingest_agent import IngestAgent
from agents.validator_agent import ValidatorAgent
from agents.transform_agent import TransformAgent
from agents.reporter_agent import ReporterAgent

def run_ingest(state: PipelineState):
    agent = IngestAgent()
    return agent.execute(state)


def run_validate(state: PipelineState):
    agent = ValidatorAgent()
    return agent.execute(state)


def run_transform(state: PipelineState):
    agent = TransformAgent()
    return agent.execute(state)

def run_report(state: PipelineState):
    agent = ReporterAgent()
    return agent.execute(state)