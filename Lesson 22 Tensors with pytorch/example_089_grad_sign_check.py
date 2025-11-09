import torch

# Example 89: Simple gradient check (sign)
w = torch.nn.Parameter(torch.tensor(1.0))
opt = torch.optim.SGD([w], lr=0.1)
x = torch.tensor(2.0)
y_true = torch.tensor(4.0)

for step in range(3):
    opt.zero_grad()
    y_pred = w * x
    loss = (y_pred - y_true) ** 2
    loss.backward()
    print("step", step, "grad:", w.grad.item())
    opt.step()
