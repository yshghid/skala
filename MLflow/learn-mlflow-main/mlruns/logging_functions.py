import os
import mlflow

# Set our tracking server uri for logging
mlflow.set_tracking_uri(uri=os.getenv("MLFLOW_TRACKING_URI", ""))

# Retrieve the current tracking URI
current_uri = mlflow.get_tracking_uri()
print(f"Current Tracking URI: {current_uri}")
# Current Tracking URI: http://0.0.0.0:5000

# Create a new MLflow Experiment
experiment = mlflow.set_experiment("new_experiment")

# Access metadata about the experiment
print(f"Experiment ID: {experiment.experiment_id}")
print(f"Experiment Name: {experiment.name}")
print(f"Artifact Location: {experiment.artifact_location}")
print(f"Lifecycle Stage: {experiment.lifecycle_stage}")
"""
Experiment ID: 2
Experiment Name: new_experiment
Artifact Location: /mlflow/mlruns/2
Lifecycle Stage: active
"""

_experiment = mlflow.get_experiment(experiment_id=experiment.experiment_id)
# Access metadata about the experiment
print(f"_Experiment ID: {_experiment.experiment_id}")
print(f"_Experiment Name: {_experiment.name}")
print(f"_Artifact Location: {_experiment.artifact_location}")
print(f"_Lifecycle Stage: {_experiment.lifecycle_stage}")

# Log runs under the same experiment
for i in range(3):
    with mlflow.start_run():
        mlflow.log_param("iteration", i)
        mlflow.log_metric("accuracy", 0.8 + i * 0.05)
        print(f"Logged run under experiment '{experiment.name}'")

        # Log an artifact (e.g., a text file)
        with open("example.txt", "w") as f:
            f.write("This is an example artifact.")
        mlflow.log_artifact("example.txt")



