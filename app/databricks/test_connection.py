import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from app.databricks.client import get_workspace_client


def test_connection():
    try:
        workspace_client = get_workspace_client()
        current_user = workspace_client.current_user.me()

        print("=" * 60)
        print("✅ Databricks Connection Successful")
        print("=" * 60)
        print(f"User Name : {current_user.user_name}")
        print("=" * 60)

    except Exception as e:
        print("=" * 60)
        print("❌ Databricks Connection Failed")
        print("=" * 60)
        print(e)
        print("=" * 60)


if __name__ == "__main__":
    test_connection()