import torch
import torch.nn as nn

# Example 73: Log loss every batch (small)
model = nn.Linear(2, 1)
opt = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.MSELoss()

x = torch.randn(20, 2)
y = torch.randn(20, 1)

for i in range(4):
    xb = x[i*5:(i+1)*5]
    yb = y[i*5:(i+1)*5]
    opt.zero_grad()
    logits = model(xb)
    loss = loss_fn(logits, yb)
    loss.backward()
    opt.step()
    print("Batch", i, "Loss", loss.item())
