from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset

# Example 62: Iterate over all batches
ds = ToyDataset()
loader = DataLoader(ds, batch_size=16)
for i, (xb, yb) in enumerate(loader):
    print(f"Batch {i}, size {len(xb)}")
