import torch
from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset

# Example 58: Shuffling effect
ds = ToyDataset()
loader1 = DataLoader(ds, batch_size=4, shuffle=False)
loader2 = DataLoader(ds, batch_size=4, shuffle=True)

print("No shuffle first batch x:")
print(next(iter(loader1))[0])
print("Shuffle first batch x:")
print(next(iter(loader2))[0])
