import torch
import torch.nn as nn

# Example 46: Count model parameters
model = nn.Sequential(
    nn.Linear(10, 20),
    nn.ReLU(),
    nn.Linear(20, 2),
)
total = sum(p.numel() for p in model.parameters())
print("Parameters:", total)
