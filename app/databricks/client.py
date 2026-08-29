from databricks.sdk import WorkspaceClient
from app.databricks.config import DATABRICKS_HOST, DATABRICKS_TOKEN


def get_workspace_client():
    return WorkspaceClient(
        host=DATABRICKS_HOST,
        token=DATABRICKS_TOKEN
    )