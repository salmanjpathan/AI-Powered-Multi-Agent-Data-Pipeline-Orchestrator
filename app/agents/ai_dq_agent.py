import json

from graph.state import PipelineState
from llm.ollama_client import OllamaClient


class AIDataQualityAgent:

    def __init__(self):
        self.llm = OllamaClient()

    def execute(self, state: PipelineState):

        prompt = f"""
You are a Senior Data Quality Engineer.

Analyze the following data pipeline execution and return ONLY valid JSON.

Pipeline Details:
- Ingest Status: {state.ingest_status}
- Validation Status: {state.validation_status}
- Transform Status: {state.transform_status}
- Report Status: {state.report_status}

Rows Processed:
{state.row_count}

Errors:
{state.errors}

Previous Recommendations:
{state.recommendations}

Return ONLY this JSON format:

{{
    "summary": "Brief pipeline summary",
    "severity": "Low",
    "business_impact": "Business impact of this execution",
    "recommendation": "Single best recommendation"
}}

Do not include markdown.
Do not include explanation.
Return only valid JSON.
"""

        response = self.llm.generate(prompt)

        try:
            data = json.loads(response)

            state.ai_summary = data.get("summary", "")
            state.severity = data.get("severity", "")
            state.business_impact = data.get("business_impact", "")

            recommendation = data.get("recommendation", "")
            if recommendation:
                state.recommendations.append(recommendation)

        except Exception as e:
            state.errors.append(f"AI JSON Parse Error: {str(e)}")
            state.ai_summary = response

        return state