import torch

# Example 31: Detach from graph
x = torch.randn(3, requires_grad=True)
y = x * 3
z = y.detach()
print("y requires_grad:", y.requires_grad)
print("z requires_grad:", z.requires_grad)
