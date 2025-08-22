from mlflow.tracking import MlflowClient
from mlflow.entities import ViewType

# Initialize MLflowClient
client = MlflowClient()

# Search for experiments
search_results = client.search_experiments(filter_string="name LIKE '%_Experiment%'")
print("Found experiments:", [(exp.experiment_id, exp.name) for exp in search_results])

# List all experiments
experiments = client.search_experiments(view_type=ViewType.ALL, order_by=["experiment_id DESC"])
for exp in experiments:
    print(f"Experiment: {exp.name} (ID: {exp.experiment_id})")
    # Search for runs
    filtered_runs = client.search_runs(experiment_ids=[exp.experiment_id])

    for run in filtered_runs:
        print(f"Run ID: {run.info.run_id}, Run Name: {run.info.run_name}, MSE: {run.data.metrics['mse'] if 'mse' in run.data.metrics else 'N/A'}")

# # Delete an experiment(soft delete)
# client.delete_experiment(experiment_id="9")

# experiments = client.search_experiments(view_type=ViewType.ACTIVE_ONLY, order_by=["experiment_id DESC"])
# for exp in experiments:
#     print(f"Experiment: {exp.name} (ID: {exp.experiment_id})")

# # Restore an experiment
# client.restore_experiment(experiment_id="9")
# experiments = client.search_experiments(view_type=ViewType.ACTIVE_ONLY, order_by=["experiment_id DESC"])
# for exp in experiments:
#     print(f"Experiment: {exp.name} (ID: {exp.experiment_id})")

