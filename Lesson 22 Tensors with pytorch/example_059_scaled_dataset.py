import torch
from torch.utils.data import Dataset, DataLoader
from example_056_custom_dataset import ToyDataset

# Example 59: Custom transform in __getitem__
class ScaledDataset(Dataset):
    def __init__(self, base_ds):
        self.base = base_ds

    def __len__(self):
        return len(self.base)

    def __getitem__(self, idx):
        x, y = self.base[idx]
        return x * 2, y

base = ToyDataset()
scaled = ScaledDataset(base)
print(scaled[0])
