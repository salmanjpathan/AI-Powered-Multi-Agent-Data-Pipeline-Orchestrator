import time

from app.databricks.client import workspace_client

BRONZE_JOB_ID = 913826646441028
SILVER_JOB_ID = 734858437358560
GOLD_JOB_ID = 747976443992049


def run_job(job_id, job_name):

    run = workspace_client.jobs.run_now(job_id=job_id)

    run_id = run.run_id

    print(f"{job_name} Triggered | Run ID : {run_id}")

    while True:

        status = workspace_client.jobs.get_run(run_id)

        life_cycle = status.state.life_cycle_state
        result = status.state.result_state

        print(f"{job_name} Status : {life_cycle}")

        if str(life_cycle) == "RunLifeCycleState.TERMINATED":

            return {
                "run_id": str(run_id),
                "status": str(result)
            }

        time.sleep(5)


def run_bronze_job():
    return run_job(BRONZE_JOB_ID, "Bronze Job")


def run_silver_job():
    return run_job(SILVER_JOB_ID, "Silver Job")


def run_gold_job():
    return run_job(GOLD_JOB_ID, "Gold Job")