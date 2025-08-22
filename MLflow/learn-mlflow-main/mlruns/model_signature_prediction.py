import mlflow
import pandas as pd

# Specify the logged model path (Replace this with your actual run ID)
logged_model = 'runs:/bf0b5813b6c84918a3fec0598a4a1225/iris_model'

# Load model as a PyFuncModel
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Example input data (Ensure the column names match the model signature)
example_data = pd.DataFrame([
    {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2},
    {"sepal_length": 6.2, "sepal_width": 2.8, "petal_length": 4.8, "petal_width": 1.8},
    {"sepal_length": 5.9, "sepal_width": 3.0, "petal_length": 5.1, "petal_width": 1.8}
])

# incorrect_example_data = pd.DataFrame([
#     {"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4},
#     {"sepal_length": 6.2, "sepal_width": 2.8, "petal_width": 1.8},
#     {"sepal_width": 3.0, "petal_length": 5.1, "petal_width": 1.8}
# ])
# validation error
#   File "/usr/local/lib/python3.10/site-packages/sklearn/utils/validation.py", line 146, in _assert_all_finite
#     raise ValueError(msg_err)
# ValueError: Input X contains NaN.
# LogisticRegression does not accept missing values encoded as NaN natively

# Predict on the example data
predictions = loaded_model.predict(example_data)

# Display results
example_data["predicted_class"] = predictions
print(example_data)
