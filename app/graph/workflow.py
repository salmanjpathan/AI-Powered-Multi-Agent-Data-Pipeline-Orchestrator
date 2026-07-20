from langgraph.graph import StateGraph, START, END

from graph.state import PipelineState
from graph.nodes import run_ingest, run_validate

# Create the workflow
workflow = StateGraph(PipelineState)

# Register nodes
workflow.add_node("ingest", run_ingest)
workflow.add_node("validate", run_validate)

# Define execution flow
workflow.add_edge(START, "ingest")
workflow.add_edge("ingest", "validate")
workflow.add_edge("validate", END)

# Compile the workflow
graph = workflow.compile()