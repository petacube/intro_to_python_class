import torch
import torch.nn as nn

# Example 69: Adam optimizer
model = nn.Linear(2, 1)
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
print(optimizer)
