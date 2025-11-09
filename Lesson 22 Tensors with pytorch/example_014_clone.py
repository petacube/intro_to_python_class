import torch

# Example 14: Clone (safe copy)
x = torch.tensor([1., 2., 3.])
y = x.clone()
y[0] = 99.
print("x:", x)
print("y:", y)
