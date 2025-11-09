import torch

# Example 27: Simple scalar function gradient
x = torch.tensor(3.0, requires_grad=True)
y = 3 * x + 2
y.backward()
print("dy/dx:", x.grad.item())
