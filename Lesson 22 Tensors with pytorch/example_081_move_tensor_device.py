import torch

# Example 81: Move tensor to device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.rand(3, 3).to(device)
print("device:", x.device)
