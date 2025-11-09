import torch

# Example 25: In-place vs out-of-place
x = torch.tensor([1., 2., 3.])
y = x + 1        # out-of-place
x.add_(1)        # in-place
print("x (after in-place):", x)
print("y (separate tensor):", y)
