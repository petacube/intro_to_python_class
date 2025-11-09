import torch

# Example 15: Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print("Using device:", device)
