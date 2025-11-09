from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset

# Example 63: Using num_workers (may behave differently on some platforms)
ds = ToyDataset()
loader = DataLoader(ds, batch_size=16, num_workers=2)
xb, yb = next(iter(loader))
print(xb.shape, yb.shape)
