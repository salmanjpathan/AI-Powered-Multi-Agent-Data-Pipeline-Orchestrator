from langgraph.graph import StateGraph, START, END

from graph.state import PipelineState
from graph.nodes import run_ingest


# Create the workflow
workflow = StateGraph(PipelineState)

# Register nodes
workflow.add_node("ingest", run_ingest)

# Define execution flow
workflow.add_edge(START, "ingest")
workflow.add_edge("ingest", END)

# Compile the workflow
graph = workflow.compile()