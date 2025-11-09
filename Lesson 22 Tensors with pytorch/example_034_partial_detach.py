import torch

# Example 34: Stop gradient for part of expression
a = torch.randn(3, requires_grad=True)
b = torch.randn(3, requires_grad=True)
y = (a * b.detach()).sum()
y.backward()
print("a.grad:", a.grad)
print("b.grad:", b.grad)
