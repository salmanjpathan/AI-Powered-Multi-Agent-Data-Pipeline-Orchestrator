import json

from app.graph.state import PipelineState
from app.llm.ollama_client import OllamaClient
from app.utils.logger import logger


class AIDataQualityAgent:

    def __init__(self):
        self.llm = OllamaClient()

    def execute(self, state: PipelineState):

        try:
            logger.info("Generating AI Data Quality Report.")

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

            data = json.loads(response)

            state.ai_summary = data.get("summary", "")
            state.severity = data.get("severity", "")
            state.business_impact = data.get("business_impact", "")

            recommendation = data.get("recommendation", "")

            if recommendation:
                state.recommendations.append(recommendation)

            logger.info("AI Data Quality Report generated successfully.")

            return state

        except json.JSONDecodeError as ex:
            logger.error(f"AI JSON Parse Error: {str(ex)}")
            state.errors.append(f"AI JSON Parse Error: {str(ex)}")
            state.ai_summary = response
            return state

        except Exception as ex:
            logger.error(f"AI Data Quality Agent failed: {str(ex)}")
            state.errors.append(str(ex))
            return state