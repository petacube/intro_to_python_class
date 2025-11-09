import torch
import torch.nn as nn

# Example 39: Custom nn.Module
class SimpleRegressor(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

model = SimpleRegressor()
print(model)
