from databricks.sdk import WorkspaceClient
from app.databricks.config import DATABRICKS_HOST, DATABRICKS_TOKEN

workspace_client = WorkspaceClient(
    host=DATABRICKS_HOST,
    token=DATABRICKS_TOKEN
)