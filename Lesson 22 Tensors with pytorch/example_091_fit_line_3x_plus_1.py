import torch
import torch.nn as nn

# Example 91: Fit y = 3x + 1
x = torch.linspace(-1, 1, steps=20).unsqueeze(1)
y = 3 * x + 1

model = nn.Linear(1, 1)
opt = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.MSELoss()

for _ in range(100):
    opt.zero_grad()
    pred = model(x)
    loss = loss_fn(pred, y)
    loss.backward()
    opt.step()

print("Pred for x=3:", model(torch.tensor([[3.0]])).item())
