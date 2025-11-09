import torch
import torch.nn as nn

# Example 50: Using nn.Sequential
model = nn.Sequential(
    nn.Linear(4, 8),
    nn.ReLU(),
    nn.Linear(8, 3)
)
x = torch.rand(2, 4)
print(model(x))
