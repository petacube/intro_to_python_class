import torch
import torch.nn as nn

# Example 85: Check gradients exist
model = nn.Linear(2, 1)
x = torch.randn(4, 2)
y = torch.randn(4, 1)
loss = nn.MSELoss()(model(x), y)
loss.backward()

for name, p in model.named_parameters():
    print(name, "grad is not None:", p.grad is not None)
