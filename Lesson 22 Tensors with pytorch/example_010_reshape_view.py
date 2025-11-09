import torch

# Example 10: Reshape tensor with view
x = torch.arange(12)
y = x.view(3, 4)
print("x:", x)
print("y:", y)
