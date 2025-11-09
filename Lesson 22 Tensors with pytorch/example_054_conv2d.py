import torch
import torch.nn as nn

# Example 54: Simple convolution
conv = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, padding=1)
img = torch.rand(1, 1, 5, 5)
out = conv(img)
print("output shape:", out.shape)
