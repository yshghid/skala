import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

# Load dataset
X, y = load_iris(return_X_y=True)
iris_feature_names = load_iris().feature_names  # Get feature names

# Convert to DataFrame
df = pd.DataFrame(X, columns=iris_feature_names)
df["target"] = y  # Include target inside the DataFrame

# Split dataset
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(train[iris_feature_names], train["target"])

# Save model
model_uri = "model_logistic_regression"
mlflow.sklearn.save_model(model, model_uri)

# Evaluate model (Ensure target is inside `data`)
eval_result = mlflow.evaluate(
    model=model_uri,
    data=test,  # `test` now includes features and target
    targets="target",  # Specify the target column name
    model_type="classifier",
)

# Print evaluation results
print(eval_result.metrics)