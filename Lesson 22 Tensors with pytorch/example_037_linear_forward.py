import torch
import torch.nn as nn

# Example 37: Forward pass through Linear
model = nn.Linear(1, 1)
x = torch.tensor([[1.0], [2.0], [3.0]])
y = model(x)
print(y)
