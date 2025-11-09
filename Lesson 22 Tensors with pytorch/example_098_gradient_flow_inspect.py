import torch
import torch.nn as nn
import torch.nn.functional as F

# Example 98: Gradient flow sanity check
model = nn.Sequential(
    nn.Linear(10, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)
x = torch.rand(4, 10)
y = torch.rand(4, 1)

opt = torch.optim.SGD(model.parameters(), lr=0.1)
opt.zero_grad()
loss = F.mse_loss(model(x), y)
loss.backward()

for name, p in model.named_parameters():
    print(name, p.grad.abs().mean().item())
