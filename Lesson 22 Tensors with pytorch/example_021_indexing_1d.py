import torch

# Example 21: Indexing elements
x = torch.tensor([10., 20., 30., 40.])
print("first:", x[0].item())
print("last:", x[-1].item())
