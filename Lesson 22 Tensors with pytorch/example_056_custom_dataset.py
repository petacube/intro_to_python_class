import torch
from torch.utils.data import Dataset

# Example 56: Custom dataset from tensors
class ToyDataset(Dataset):
    def __init__(self):
        self.x = torch.randn(100, 2)
        self.y = (self.x.sum(dim=1) > 0).long()

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

ds = ToyDataset()
print("len:", len(ds))
print("first sample:", ds[0])
