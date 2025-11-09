import torch
import torch.nn as nn

# Example 55: Max pooling
x = torch.rand(1, 1, 4, 4)
pool = nn.MaxPool2d(2)
print("input shape:", x.shape)
print("pooled shape:", pool(x).shape)
