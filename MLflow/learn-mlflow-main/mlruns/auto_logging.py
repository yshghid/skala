import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Enable autologging
mlflow.autolog(log_input_examples=True)

# Load dataset
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
                                    iris.data,
                                    iris.target,
                                    test_size=0.2,
                                    random_state=42)

# Train a model
with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
    model.fit(X_train, y_train)  # Autologging automatically logs parameters & metrics

    # Log additional artifacts if needed
    mlflow.sklearn.log_model(model, "random_forest_model")

print("Training complete. Run 'mlflow ui' to view logs.")
