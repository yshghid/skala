import requests
import json

# MLflow tracking server URL
MLFLOW_SERVER_URL = "http://0.0.0.0:5001/api/2.0/mlflow"

### 1️⃣ Create a new experiment ###
experiment_name = "REST_API_Experiment1"
create_exp_url = f"{MLFLOW_SERVER_URL}/experiments/create"
response = requests.post(create_exp_url, json={"name": experiment_name})

if response.status_code == 200:
    experiment_id = response.json()["experiment_id"]
    print(f"✅ Experiment Created: {experiment_name} (ID: {experiment_id})")
else:
    print(f"⚠️ Experiment creation failed: {response.text}")
    experiment_id = None  # Handle failure case

if experiment_id:
    ### 2️⃣ Create a new run ###
    create_run_url = f"{MLFLOW_SERVER_URL}/runs/create"
    response = requests.post(create_run_url, json={"experiment_id": experiment_id})

    if response.status_code == 200:
        run_id = response.json()["run"]["info"]["run_id"]
        print(f"✅ Run Created: {run_id}")
    else:
        print(f"⚠️ Run creation failed: {response.text}")
        run_id = None  # Handle failure case

    if run_id:
        ### 3️⃣ Log a parameter ###
        log_param_url = f"{MLFLOW_SERVER_URL}/runs/log-parameter"
        param_data = {"run_id": run_id, "key": "learning_rate", "value": "0.01"}
        requests.post(log_param_url, json=param_data)

        ### 4️⃣ Log a metric ###
        log_metric_url = f"{MLFLOW_SERVER_URL}/runs/log-metric"
        metric_data = {"run_id": run_id, "key": "accuracy", "value": 0.95, "timestamp": 1700000000}
        requests.post(log_metric_url, json=metric_data)

        ### 5️⃣ Retrieve run details ###
        get_run_url = f"{MLFLOW_SERVER_URL}/runs/get?run_id={run_id}"
        response = requests.get(get_run_url)

        if response.status_code == 200:
            run_info = response.json()["run"]
            print("\n✅ Run Details:")
            print(json.dumps(run_info, indent=4))
        else:
            print(f"⚠️ Failed to retrieve run details: {response.text}")
