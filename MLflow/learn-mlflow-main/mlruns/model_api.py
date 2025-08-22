import mlflow
import mlflow.sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

# Load data
X, y = load_iris(return_X_y=True)

# Train a model
model = LogisticRegression()
model.fit(X, y)

# Save model locally
mlflow.sklearn.save_model(model, path="model_api")

# # Log model to MLflow Tracking Server
# with mlflow.start_run():
#     mlflow.sklearn.log_model(model, artifact_path="sklearn_model")