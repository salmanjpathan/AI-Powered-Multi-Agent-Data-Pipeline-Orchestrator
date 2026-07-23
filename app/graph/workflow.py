from langgraph.graph import StateGraph, START, END

from app.graph.state import PipelineState

from app.graph.nodes import (
    run_ingest,
    run_bronze,
    run_validate,
    run_silver,
    run_transform,
    run_gold,
    run_report,
    run_ai_report,
)

workflow = StateGraph(PipelineState)

# Register nodes
workflow.add_node("ingest", run_ingest)
workflow.add_node("bronze", run_bronze)
workflow.add_node("validate", run_validate)
workflow.add_node("silver", run_silver)
workflow.add_node("transform", run_transform)
workflow.add_node("gold", run_gold)
workflow.add_node("report", run_report)
workflow.add_node("ai_report", run_ai_report)

# Workflow
workflow.add_edge(START, "ingest")
workflow.add_edge("ingest", "bronze")
workflow.add_edge("bronze", "validate")
workflow.add_edge("validate", "silver")
workflow.add_edge("silver", "transform")
workflow.add_edge("transform", "gold")
workflow.add_edge("gold", "report")
workflow.add_edge("report", "ai_report")
workflow.add_edge("ai_report", END)

graph = workflow.compile()