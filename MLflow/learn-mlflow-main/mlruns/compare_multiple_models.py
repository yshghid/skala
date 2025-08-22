import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Load dataset
X, y = load_iris(return_X_y=True)
iris_feature_names = load_iris().feature_names  # Get feature names

# Convert to DataFrame
df = pd.DataFrame(X, columns=iris_feature_names)
df["target"] = y  # Include target inside the DataFrame

# Split dataset
train, test = train_test_split(df, test_size=0.2, random_state=42)

# Define models
models = {
    "Logistic Regression": LogisticRegression(max_iter=200),
    "Random Forest": RandomForestClassifier(n_estimators=100)
}

# Compare multiple models
results = {}

for model_name, model in models.items():
    with mlflow.start_run(run_name=model_name):
        # Train model
        model.fit(train[iris_feature_names], train["target"])

        # Save the model
        model_uri = f"models/{model_name.replace(' ', '_')}"
        mlflow.sklearn.save_model(model, model_uri)

        # Evaluate the model
        eval_result = mlflow.evaluate(
            model=model_uri,
            data=test,  # Features + target
            targets="target",  # Column name of labels
            model_type="classifier",
        )

        # Log evaluation metrics
        mlflow.log_metrics(eval_result.metrics)

        # Store results for comparison
        results[model_name] = eval_result.metrics

# Print comparison results
for model, metrics in results.items():
    print(f"\n📌 {model} Metrics:")
    for metric, value in metrics.items():
        print(f"   {metric}: {value}")
