import time

from app.databricks.client import workspace_client

JOB_ID = 913826646441028


def run_bronze_job():

    run = workspace_client.jobs.run_now(
        job_id=JOB_ID
    )

    run_id = run.run_id

    print(f"Bronze Job Triggered | Run ID : {run_id}")

    while True:

        status = workspace_client.jobs.get_run(run_id)

        life_cycle = status.state.life_cycle_state
        result = status.state.result_state

        print(f"Status : {life_cycle}")

        if life_cycle == "TERMINATED":

            return {
                "run_id": run_id,
                "status": result
            }

        time.sleep(5)