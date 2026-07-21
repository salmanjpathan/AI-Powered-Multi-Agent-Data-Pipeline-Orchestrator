from langgraph.graph import StateGraph, START, END

from graph.state import PipelineState
from graph.nodes import (
    run_ingest,
    run_validate,
    run_transform,
    run_report,
    run_ai_report,
)

# Create the workflow
workflow = StateGraph(PipelineState)

# Register nodes
workflow.add_node("ingest", run_ingest)
workflow.add_node("validate", run_validate)
workflow.add_node("transform", run_transform)
workflow.add_node("report", run_report)
workflow.add_node("ai_report", run_ai_report)

# Define execution flow
workflow.add_edge(START, "ingest")
workflow.add_edge("ingest", "validate")
workflow.add_edge("validate", "transform")
workflow.add_edge("transform", "report")
workflow.add_edge("report", "ai_report")
workflow.add_edge("ai_report", END)

# Compile the workflow
graph = workflow.compile()