import torch

# Example 26: Enable gradient tracking
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()
print("dy/dx:", x.grad.item())
