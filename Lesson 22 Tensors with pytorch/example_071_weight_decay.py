import torch
import torch.nn as nn

# Example 71: L2 weight decay
model = nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, weight_decay=1e-3)
print(optimizer)
