import torch

# Example 19: Matrix multiplication
A = torch.rand(2, 3)
B = torch.rand(3, 4)
C = A @ B
print("A shape:", A.shape)
print("B shape:", B.shape)
print("C shape:", C.shape)
