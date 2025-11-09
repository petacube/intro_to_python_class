import torch
import torch.nn as nn

# Example 99: Inference-only helper
def predict(model, x):
    model.eval()
    with torch.no_grad():
        return model(x)

model = nn.Linear(10, 1)
x = torch.rand(2, 10)
print(predict(model, x))
