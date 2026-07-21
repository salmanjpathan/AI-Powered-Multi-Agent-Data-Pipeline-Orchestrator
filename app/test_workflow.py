from graph.workflow import graph
from graph.state import PipelineState

state = PipelineState(
    pipeline_id="001",
    source_file="data/raw/sales.csv",
    source_type="csv"
)

result = graph.invoke(state)

print(result)

print("\n================ AI REPORT ================\n")
print(result["ai_summary"])