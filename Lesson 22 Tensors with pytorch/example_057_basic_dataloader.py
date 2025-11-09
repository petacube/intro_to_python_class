import torch
from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset

# Example 57: Basic DataLoader
ds = ToyDataset()
loader = DataLoader(ds, batch_size=16, shuffle=True)
xb, yb = next(iter(loader))
print(xb.shape, yb.shape)
