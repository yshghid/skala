import mlflow

# Start and end a run
with mlflow.start_run():
    mlflow.log_param("param1", 42)
    # The run is active within this block
    print(f"Active run ID inside the block: {mlflow.active_run().info.run_id}")

# Now the run is ended
print(f"Active run after block: {mlflow.active_run()}")        # None
print(f"Last active run after block: {mlflow.last_active_run()}")  # Should not be None

# We can still access the last run’s ID:
last_run = mlflow.last_active_run()
if last_run:
    print(f"Last run ID: {last_run.info.run_id}")
