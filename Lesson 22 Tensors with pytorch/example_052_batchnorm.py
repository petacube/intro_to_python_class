import torch
import torch.nn as nn

# Example 52: BatchNorm1d example
bn = nn.BatchNorm1d(3)
x = torch.rand(4, 3)
print(bn(x))
