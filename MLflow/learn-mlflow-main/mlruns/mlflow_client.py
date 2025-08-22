import os
import mlflow
from mlflow.tracking import MlflowClient

# Initialize MLflowClient
client = MlflowClient()

# Step 1: Create a new experiment (if not exists)
experiment_name = "My_New_Experiment"
existing_experiments = client.search_experiments()

# Check if experiment already exists
experiment = next((exp for exp in existing_experiments if exp.name == experiment_name), None)

if experiment:
    experiment_id = experiment.experiment_id
    print(f"Using existing experiment: {experiment_name} (ID: {experiment_id})")
else:
    experiment_id = client.create_experiment(experiment_name)
    print(f"Created new experiment: {experiment_name} (ID: {experiment_id})")

# Step 2: Start a new run and log parameters, metrics
with mlflow.start_run(experiment_id=experiment_id) as run:
    run_id = run.info.run_id
    print(f"Started Run ID: {run_id}")

    # Log parameters and metrics
    client.log_param(run_id, "learning_rate", 0.01)
    client.log_metric(run_id, "accuracy", 0.95)

    # Step 3: Log an artifact
    artifact_path = "output.txt"
    with open(artifact_path, "w") as f:
        f.write("Sample artifact content")

    client.log_artifact(run_id, artifact_path)
    print(f"Logged artifact: {artifact_path}")

    # Step 4: Retrieve and print run details
    retrieved_run = client.get_run(run_id)
    print(f"Run ID: {retrieved_run.info.run_id}, Metrics: {retrieved_run.data.metrics}")

# Step 5: List artifacts
artifacts = client.list_artifacts(run_id)
print(f"Artifacts in run: {[a.path for a in artifacts]}")

# Step 6: Download artifact
downloaded_path = client.download_artifacts(run_id, artifact_path)
print(f"Artifact downloaded to: {downloaded_path}")

# Step 7: Register a model
model_name = "my_model"
model_uri = f"runs:/{run_id}/model"

try:
    client.create_registered_model(
        model_name, 
        tags={"source": "MLflow"}, 
        description="My model description")
except Exception as e:
    print(f"Model {model_name} already registered.")

model_version = client.create_model_version(name=model_name, source=model_uri, run_id=run_id)

# Step 8: Transition model to "Production"
client.transition_model_version_stage(
    name=model_name,
    version=model_version.version,
    stage="Production"
)

# Step 9: Retrieve model details
registered_model = client.get_registered_model(model_name)
print(f"Registered Model: {registered_model.name}, Version: {model_version.version}")

