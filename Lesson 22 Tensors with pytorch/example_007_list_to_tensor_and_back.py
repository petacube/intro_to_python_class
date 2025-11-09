import torch

# Example 7: From Python list and back
data = [1, 2, 3]
x = torch.tensor(data)
print("tensor:", x)
print("back to list:", x.tolist())
