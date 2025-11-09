import torch
import torch.nn as nn

# Example 38: Tiny training loop (1D regression)
model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.MSELoss()

x = torch.tensor([[0.0], [1.0], [2.0]])
y_true = torch.tensor([[0.0], [2.0], [4.0]])

for epoch in range(50):
    y_pred = model(x)
    loss = loss_fn(y_pred, y_true)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print("Pred for 3:", model(torch.tensor([[3.0]])).item())
