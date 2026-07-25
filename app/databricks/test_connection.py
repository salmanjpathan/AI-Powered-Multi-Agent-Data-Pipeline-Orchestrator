from app.databricks.client import workspace_client


def test_connection():
    try:
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