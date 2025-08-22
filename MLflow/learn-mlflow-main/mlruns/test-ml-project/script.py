import mlflow

# Define the MLflow project directory (local or remote Git repo)
project_uri = "."

# Run the MLflow project
run = mlflow.projects.run(
    uri=project_uri,  # Path to the MLflow project
    entry_point="main",  # Entry point defined in MLproject file
    parameters={"alpha": 0.6, "l1_ratio": 0.2},  # Hyperparameters
    experiment_name="ElasticNet_Regression",  # Assign experiment name
    run_name="Test_Run",  # Assign a custom run name
    synchronous=True,  # Wait for completion (default=True)
    env_manager="local"  # Use local to manage dependencies
)

# Print run details
print(f"Run ID: {run.run_id}")
