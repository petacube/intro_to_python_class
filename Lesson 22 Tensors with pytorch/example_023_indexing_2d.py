import torch

# Example 23: 2D indexing
x = torch.arange(16).view(4, 4)
print(x)
print("row 1:", x[1])
print("element (2,3):", x[2, 3].item())
