import torch
from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset

# Example 61: Simple custom collate
def simple_collate(batch):
    xs, ys = zip(*batch)
    return torch.stack(xs), torch.tensor(ys)

ds = ToyDataset()
loader = DataLoader(ds, batch_size=8, collate_fn=simple_collate)
xb, yb = next(iter(loader))
print(xb.shape, yb.shape)
