from graph.state import PipelineState
from agents.ingest_agent import IngestAgent


state = PipelineState(
    pipeline_id="PIPELINE_001",
    source_file="data/raw/not_exists.csv",
    source_type="csv"
)

agent = IngestAgent()

updated_state = agent.execute(state)

print(updated_state)