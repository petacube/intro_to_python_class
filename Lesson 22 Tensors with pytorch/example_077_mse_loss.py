import torch
import torch.nn as nn

# Example 77: MSELoss example
loss_fn = nn.MSELoss()
pred = torch.tensor([2.5, 0.0])
target = torch.tensor([3.0, -1.0])
print(loss_fn(pred, target))
