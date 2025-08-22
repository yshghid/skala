# Essential MLflow CLI Examples

## Start the MLflow Tracking Server
```
mlflow server --backend-store-uri mysql+pymysql://root:rootpassword@db/mlflow --default-artifact-root /mlflow/mlruns --host 0.0.0.0 --port 5000"
```

## Run an MLflow Project
```
mlflow run . --env-manager=local --experiment-name "xxx" -P learning_rate=0.01 -P epochs=10
```

## Log and List Experiments
```
mlflow experiments search
Experiment Id    Name                   Artifact Location
---------------  ---------------------  -------------------
0                Default                /mlflow/mlruns/0
2                model-registry         /mlflow/mlruns/2
3                ElasticNet_Regression  /mlflow/mlruns/3
4                ElasticNet_Experiment  /mlflow/mlruns/4
9                My_New_Experiment      /mlflow/mlruns/9
```

```
mlflow runs list --experiment-id 9 --view 'all'
# --view FINISHED, RUNNING, FAILED, DELETED
Date                     Name           ID
-----------------------  -------------  --------------------------------
2025-02-16 16:44:25 UTC  able-swan-847  9f6a259899534355902d572c326e4ff4
```

```
mlflow runs describe --run-id 9f6a259899534355902d572c326e4ff4
{
    "info": {
        "artifact_uri": "/mlflow/mlruns/9/9f6a259899534355902d572c326e4ff4/artifacts",
        "end_time": 1739724265674,
        "experiment_id": "9",
        "lifecycle_stage": "active",
        "run_id": "9f6a259899534355902d572c326e4ff4",
        "run_name": "able-swan-847",
        "run_uuid": "9f6a259899534355902d572c326e4ff4",
        "start_time": 1739724265613,
        "status": "FINISHED",
        "user_id": "root"
    },
    "data": {
        "metrics": {
            "accuracy": 0.95
        },
        "params": {
            "learning_rate": "0.01"
        },
        "tags": {
            "mlflow.runName": "able-swan-847",
            "mlflow.source.name": "mlflow_client.py",
            "mlflow.source.type": "LOCAL",
            "mlflow.user": "root"
        }
    },
    "inputs": {
        "dataset_inputs": []
    }
}
```

## Save and Serve a Model
```
# used model_signature.py to build a model
mlflow models predict --env-manager local --model-uri runs:/bf0b5813b6c84918a3fec0598a4a1225/iris_model --input-path input.json
{"predictions": [0]}

# where input.json
{"dataframe_records": [{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}]}


mlflow models serve --env-manager local --model-uri runs:/bf0b5813b6c84918a3fec0598a4a1225/iris_model --port 5002
python model_serve_run.py
"""
import requests
import json

url = "http://127.0.0.1:5002/invocations"

# Load input JSON
with open("input.json", "r") as f:
    data = json.load(f)

# Send POST request
response = requests.post(url, json=data, headers={"Content-Type": "application/json"})

# Print prediction result
print(response.json())
"""
```

## Environment Debugging
```
mlflow doctor

System information: Linux #1 SMP PREEMPT Tue Sep 13 07:51:32 UTC 2022
Python version: 3.10.16
MLflow version: 2.20.2
MLflow module location: /usr/local/lib/python3.10/site-packages/mlflow/__init__.py
Tracking URI: http://0.0.0.0:5000
Registry URI: http://0.0.0.0:5000
MLflow environment variables:
  MLFLOW_TRACKING_URI: http://0.0.0.0:5000
MLflow dependencies:
  Flask: 3.1.0
  Jinja2: 3.1.5
  alembic: 1.14.1
  docker: 7.1.0
  graphene: 3.4.3
  gunicorn: 23.0.0
  markdown: 3.7
  matplotlib: 3.10.0
  mlflow-skinny: 2.20.2
  numpy: 2.2.2
  pandas: 2.2.3
  pyarrow: 18.1.0
  scikit-learn: 1.6.1
  scipy: 1.15.1
  sqlalchemy: 2.0.38
```
