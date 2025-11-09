import torch

# Example 12: Unsqueeze (add dimension)
x = torch.tensor([1., 2., 3.])
x2 = x.unsqueeze(0)
print("original shape:", x.shape)
print("unsqueezed shape:", x2.shape)
