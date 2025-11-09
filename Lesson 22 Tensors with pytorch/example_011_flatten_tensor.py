import torch

# Example 11: Flatten tensor
x = torch.rand(2, 3)
flat = x.view(-1)
print("x:", x)
print("flat:", flat)
