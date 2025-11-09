from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset

# Example 60: Default collate
ds = ToyDataset()
loader = DataLoader(ds, batch_size=8)
xb, yb = next(iter(loader))
print(xb.shape, yb.shape)
