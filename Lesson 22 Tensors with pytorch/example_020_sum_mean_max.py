import torch

# Example 20: Sum, mean, max
x = torch.tensor([1., 2., 3., 4.])
print("sum:", x.sum().item())
print("mean:", x.mean().item())
print("max:", x.max().item())
