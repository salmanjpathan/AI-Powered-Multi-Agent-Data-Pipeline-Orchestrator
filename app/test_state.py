from graph.state import PipelineState


state = PipelineState(
    pipeline_id="PIPELINE_001",
    source_file="sales.csv",
    source_type="csv"
)

print(state)