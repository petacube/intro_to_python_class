import torch
import numpy as np

# Example 90: detach().cpu().numpy()
x = torch.rand(3, 3, requires_grad=True)
y = (x * 2).sum()
y.backward()
arr = x.detach().cpu().numpy()
print(type(arr), arr.shape)
