import numpy as np
import mlflow
from mlflow.models import infer_signature

import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import make_classification
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score


mlflow.set_tracking_uri(uri = "http://127.0.0.1:5000")

X, y = make_classification(n_samples=500)
t_X, t_y = make_classification(n_samples=50)

params={"n_jobs": -1}

model = LogisticRegression(**params)
model.fit(X, y)
pred = model.predict(t_X)

accuracy = np.sum(pred==t_y)
accuracy = accuracy_score(pred, t_y)
precision = accuracy_score(pred, t_y)

mlflow.set_experiment("mlflow Quickstart Guide" )

with mlflow.start_run() as run:
    mlflow.log_params(params)

    mlflow.log_metric("accuracy ", accuracy)
    mlflow.log_metric("precision ", precision)

    # mlflow.set_tags("Training", "Logistic model training")

    signature = infer_signature(t_X, model.predict(t_X))

    model_info = mlflow.sklearn.log_model(model, "logistic_model", signature=signature)

pytorch_pyfunc = mlflow.pyfunc.load_model(model_uri=model_info.model_uri)

predictions = pytorch_pyfunc.predict(t_X)
print(predictions)
