import mlflow
import time

# --- Step 1: Create a brand-new run and log something ---
with mlflow.start_run() as run:
    run_id = run.info.run_id
    mlflow.log_param("initial_param", 123)
    mlflow.log_metric("initial_metric", 0.5)
    print(f"Initial run created with run_id: {run_id}")

# Simulate a pause in your process (e.g., job interruption)
time.sleep(2)

# --- Step 2: Resume the existing run by run_id ---
with mlflow.start_run(run_id=run_id):
    mlflow.log_param("resumed_param", 999)
    mlflow.log_metric("resumed_metric", 0.95)
    print(f"Resumed run with run_id: {run_id}")

print("Done logging to the same run.")

# mlflow runs describe --run-id <run-id>
