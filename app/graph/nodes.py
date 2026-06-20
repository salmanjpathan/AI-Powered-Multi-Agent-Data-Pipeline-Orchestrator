from graph.state import PipelineState
from agents.ingest_agent import IngestAgent


def run_ingest(state: PipelineState):

    agent = IngestAgent()

    return agent.execute(state)