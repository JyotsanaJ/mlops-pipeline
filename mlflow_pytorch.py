import numpy as np
import mlflow
from mlflow.models import infer_signature
import torch
from torch import nn

mlflow.set_tracking_uri(uri = "localhost:5000")

net = nn.Linear(6, 1)
loss_function = nn.L1Loss()
optimizer = torch.optim.Adam(net.parameters(), lr=1e-4)

X = torch.randn(6)
y = torch.randn(1)

epochs = 5
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = net(X)

    loss = loss_function(outputs, y)
    loss.backward()

    optimizer.step()

with mlflow.start_run() as run:
    signature = infer_signature(X.numpy(), net(X).detach().numpy())
    model_info = mlflow.pytorch.log_model(net, "model", signature=signature)

pytorch_pyfunc = mlflow.pyfunc.load_model(model_uri=model_info.model_uri)

predictions = pytorch_pyfunc.predict(torch.randn(6).numpy())
print(predictions)
