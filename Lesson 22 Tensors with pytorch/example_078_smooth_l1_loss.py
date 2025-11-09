import torch
import torch.nn as nn

# Example 78: Smooth L1 / Huber loss
loss_fn = nn.SmoothL1Loss()
pred = torch.tensor([2.5, 0.0])
target = torch.tensor([3.0, -1.0])
print(loss_fn(pred, target))
