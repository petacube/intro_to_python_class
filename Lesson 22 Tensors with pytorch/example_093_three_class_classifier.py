import torch
import torch.nn as nn
import torch.nn.functional as F

# Example 93: Simple 3-class classifier
x = torch.randn(120, 2)
y = torch.randint(0, 3, (120,))

model = nn.Sequential(
    nn.Linear(2, 8),
    nn.ReLU(),
    nn.Linear(8, 3)
)
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(100):
    opt.zero_grad()
    logits = model(x)
    loss = F.cross_entropy(logits, y)
    loss.backward()
    opt.step()

print("Final loss:", loss.item())
