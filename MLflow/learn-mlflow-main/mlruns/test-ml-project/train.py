import argparse
import mlflow
import mlflow.sklearn
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, default=0.5, help="Alpha value for ElasticNet")
parser.add_argument("--l1_ratio", type=float, default=0.1, help="L1 ratio for ElasticNet")
args = parser.parse_args()

# Generate synthetic dataset
np.random.seed(42)
X = np.random.rand(100, 5)
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ensure an MLflow experiment is set
mlflow.set_experiment("ElasticNet_Regression")

# Start the MLflow run (ensure no nested runs error)
if mlflow.active_run():
    mlflow.end_run()  # Close any existing runs

with mlflow.start_run():
    model = ElasticNet(alpha=args.alpha, l1_ratio=args.l1_ratio, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)

    mlflow.log_param("alpha", args.alpha)
    mlflow.log_param("l1_ratio", args.l1_ratio)
    mlflow.log_metric("mse", mse)
    
    mlflow.sklearn.log_model(model, "model")

    print(f"Run completed: MSE = {mse}")
