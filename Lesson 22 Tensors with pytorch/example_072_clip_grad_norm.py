import torch
import torch.nn as nn

# Example 72: Clip gradients
model = nn.Sequential(nn.Linear(2, 10), nn.ReLU(), nn.Linear(10, 1))
x = torch.randn(8, 2)
y = torch.randn(8, 1)
opt = torch.optim.SGD(model.parameters(), lr=0.1)
loss = nn.MSELoss()(model(x), y)
loss.backward()
torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
opt.step()
print("Clipped and stepped.")
