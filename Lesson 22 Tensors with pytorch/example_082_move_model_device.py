import torch
import torch.nn as nn

# Example 82: Move model to device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = nn.Linear(10, 1).to(device)
x = torch.rand(4, 10).to(device)
print(model(x).device)
