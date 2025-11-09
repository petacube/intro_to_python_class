import torch
import torch.nn as nn

# Example 36: Define a linear model
model = nn.Linear(1, 1)
for p in model.parameters():
    print(p.shape, p)
