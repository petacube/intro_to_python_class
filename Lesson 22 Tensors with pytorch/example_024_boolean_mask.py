import torch

# Example 24: Boolean mask
x = torch.tensor([1, 5, 2, 8, 3])
mask = x > 3
print("mask:", mask)
print("filtered:", x[mask])
