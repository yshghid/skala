import mlflow
from mlflow.models import infer_signature

import os
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

loaded_model = mlflow.pyfunc.load_model(f"models:/super-model/Staging")

# # using alias
# loaded_model = mlflow.pyfunc.load_model(f"models:/super-model@champion")

predictions = loaded_model.predict(X_test)

iris_feature_names = datasets.load_iris().feature_names

result = pd.DataFrame(X_test, columns=iris_feature_names)
result["actual_class"] = y_test
result["predicted_class"] = predictions

print(result[:4])
