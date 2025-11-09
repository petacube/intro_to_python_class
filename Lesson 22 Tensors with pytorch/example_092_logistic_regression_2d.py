import torch
import torch.nn as nn

# Example 92: Simple logistic regression (2D -> binary)
N = 100
x = torch.randn(N, 2)
y = (x[:, 0] + x[:, 1] > 0).float().unsqueeze(1)

model = nn.Linear(2, 1)
opt = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.BCEWithLogitsLoss()

for _ in range(200):
    opt.zero_grad()
    logits = model(x)
    loss = loss_fn(logits, y)
    loss.backward()
    opt.step()

print("Final loss:", loss.item())
