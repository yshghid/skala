import mlflow
from mlflow.models import ModelSignature
from mlflow.types.schema import Schema, ColSpec

import os
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)
iris_feature_names = datasets.load_iris().feature_names

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define the model hyperparameters
params = {
    "solver": "lbfgs",
    "max_iter": 1000,
    "multi_class": "auto",
    "random_state": 8888,
}

# Train the model
lr = LogisticRegression(**params)
lr.fit(X_train, y_train)

# Predict on the test set
y_pred = lr.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Set our tracking server URI for logging
mlflow.set_tracking_uri(uri=os.getenv("MLFLOW_TRACKING_URI", ""))

# Create a new MLflow Experiment
mlflow.set_experiment("MLflow Model Signature Quickstart")

# Define Column-based Signature
input_schema = Schema([
    ColSpec("double", name="sepal_length"),
    ColSpec("double", name="sepal_width"),
    ColSpec("double", name="petal_length"),
    ColSpec("double", name="petal_width"),
])

output_schema = Schema([ColSpec("long")])

signature = ModelSignature(inputs=input_schema, outputs=output_schema)

# Start an MLflow run
with mlflow.start_run():
    # Log the hyperparameters
    mlflow.log_params(params)

    # Log the accuracy metric
    mlflow.log_metric("accuracy", float(accuracy))

    # Set a tag for identification
    mlflow.set_tag("Training Info", "Basic LR model for iris data")

    # Log the model with manually defined signature
    model_info = mlflow.sklearn.log_model(
        sk_model=lr,
        artifact_path="iris_model",
        signature=signature,
        input_example=pd.DataFrame(X_train, columns=iris_feature_names),
        registered_model_name="model-signature-quickstart",
    )

    # Load the model back for predictions as a generic Python Function model
    loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
    X_test_df = pd.DataFrame(X_test, columns=["sepal_length", "sepal_width", "petal_length", "petal_width"])
    predictions = loaded_model.predict(X_test_df)

    # Store results in a DataFrame
    result = pd.DataFrame(X_test, columns=iris_feature_names)
    result["actual_class"] = y_test
    result["predicted_class"] = predictions

    print(result[:4])
