import torch

# Example 32: Multiple operations chain
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
z = 3 * y + 1
z.backward()
print("dz/dx:", x.grad.item())
