import torch

# Example 28: Vector gradient (sum of squares)
x = torch.randn(3, requires_grad=True)
y = (x ** 2).sum()
y.backward()
print("x:", x)
print("grad (2x):", x.grad)
