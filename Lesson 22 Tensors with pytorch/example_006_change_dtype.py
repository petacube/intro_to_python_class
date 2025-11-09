import torch

# Example 6: Change dtype
x = torch.tensor([1, 2, 3])
x_float = x.float()
print("x dtype:", x.dtype)
print("x_float dtype:", x_float.dtype)
