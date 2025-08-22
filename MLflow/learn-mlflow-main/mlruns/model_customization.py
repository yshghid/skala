import mlflow.pyfunc
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import os
import pickle
import shutil

# Define a custom model with preprocessing and load_context
class CustomModel(mlflow.pyfunc.PythonModel):
    def __init__(self, sklearn_model=None):
        self.sklearn_model = sklearn_model
        self.scaler = StandardScaler()  # Example of a preprocessing step

    def load_context(self, context):
        with open(context.artifacts["model"], "rb") as f:
            self.sklearn_model = pickle.load(f)

    def fit(self, X_train, y_train):
        X_scaled = self.scaler.fit_transform(X_train)
        self.sklearn_model.fit(X_scaled, y_train)

    def predict(self, context, model_input):
        # Apply preprocessing
        model_input_scaled = self.scaler.transform(model_input)
        raw_predictions = self.sklearn_model.predict(model_input_scaled)
        class_labels = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        return [class_labels[pred] for pred in raw_predictions]

# Load sample data
X = np.array([[5.1, 3.5, 1.4, 0.2], [6.2, 2.8, 4.8, 1.8], [5.9, 3.0, 5.1, 1.8]])
y = np.array([0, 1, 2])

# Train model
model = LogisticRegression(max_iter=200)
custom_model = CustomModel(model)
custom_model.fit(X, y)

# Save the model artifact
os.makedirs("artifacts", exist_ok=True)
with open("artifacts/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Define Conda environment
conda_env = {
    "name": "mlflow-env",
    "channels": ["defaults"],
    "dependencies": [
        "python=3.8",
        "scikit-learn",
        "mlflow",
        "pandas",
        "numpy"
    ]
}

# Save as an MLflow model
# Check if the artifacts directory exists, if it does, remove it
if os.path.exists("custom_mlflow_model"):
    shutil.rmtree("custom_mlflow_model")

mlflow.pyfunc.save_model(
    path="custom_mlflow_model",
    python_model=custom_model,
    artifacts={"model": "artifacts/model.pkl"},
    conda_env=conda_env
)

with mlflow.start_run():
    mlflow.pyfunc.log_model(
        artifact_path="custom_model",
        python_model=custom_model,
        registered_model_name="custom_sklearn_model"
    )

# Load and predict
loaded_model = mlflow.pyfunc.load_model("custom_mlflow_model")
predictions = loaded_model.predict(pd.DataFrame(X))
print(predictions)
