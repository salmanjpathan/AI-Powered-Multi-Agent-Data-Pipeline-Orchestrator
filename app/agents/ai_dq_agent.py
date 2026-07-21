from graph.state import PipelineState
from llm.ollama_client import OllamaClient


class AIDataQualityAgent:

    def __init__(self):
        self.llm = OllamaClient()

    def execute(self, state: PipelineState):

        prompt = f"""
You are a Senior Data Quality Engineer.

Analyze the following pipeline execution.

Pipeline Status:
- Ingest: {state.ingest_status}
- Validation: {state.validation_status}
- Transform: {state.transform_status}

Rows Processed:
{state.row_count}

Errors:
{state.errors}

Recommendations:
{state.recommendations}

Return your response in the following format exactly:

Summary:
<summary>

Severity:
<Low/Medium/High>

Business Impact:
<impact>

Recommendation:
<recommendation>
"""

        response = self.llm.generate(prompt)

        state.ai_summary = response

        return state