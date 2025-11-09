import torch
from torch.utils.data import random_split
from example_056_custom_dataset import ToyDataset

# Example 64: Train/val split
ds = ToyDataset()
n = len(ds)
train_size = int(0.8 * n)
val_size = n - train_size
train_ds, val_ds = random_split(ds, [train_size, val_size])
print("train:", len(train_ds), "val:", len(val_ds))
