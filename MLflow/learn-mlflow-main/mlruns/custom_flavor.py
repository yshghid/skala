import mlflow.pyfunc
import json
import os
import pickle

class CustomMLModel:
    """Example custom model that squares an input number."""
    
    def predict(self, input_data):
        return input_data ** 2  # Simple transformation

# Train a simple model
model = CustomMLModel()

class CustomMLflowFlavor(mlflow.pyfunc.PythonModel):
    def __init__(self, model=None):
        self.model = model

    def load_context(self, context):
        """Load model from MLflow storage."""
        with open(context.artifacts["model"], "rb") as f:
            self.model = pickle.load(f)

    def predict(self, model_input):
        """MLflow calls this method directly with one argument (model_input)."""
        return self.model.predict(model_input)

# Define `_load_pyfunc()` for MLflow
def _load_pyfunc(model_path):
    with open(os.path.join(model_path, "model.pkl"), "rb") as f:
        model = pickle.load(f)
    return CustomMLflowFlavor(model)

def save_model(path, model):
    os.makedirs(path, exist_ok=True)

    # Save model as a pickle file
    model_path = os.path.join(path, "model.pkl")
    with open(model_path, "wb") as f:
        pickle.dump(model, f)

    # Define MLmodel metadata
    mlmodel_data = {
        "flavors": {
            "python_function": {
                "loader_module": __name__,  # This file will be used to load the model
                "python_version": "3.10"
            }
        }
    }

    with open(os.path.join(path, "MLmodel"), "w") as f:
        json.dump(mlmodel_data, f, indent=4)

# Save the model as a custom flavor
save_model("custom_flavor_model", model)

# Load the custom model
loaded_model = mlflow.pyfunc.load_model("custom_flavor_model")

# Make a prediction
import pandas as pd
data = pd.DataFrame([2, 3, 4])  # Input values
predictions = loaded_model.predict(data)
print(predictions)  # Expected output: [4, 9, 16]
