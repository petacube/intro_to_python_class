import torch

# Example 13: Squeeze (remove size-1 dimensions)
x = torch.zeros(1, 3, 1)
print("before:", x.shape)
print("after:", x.squeeze().shape)
