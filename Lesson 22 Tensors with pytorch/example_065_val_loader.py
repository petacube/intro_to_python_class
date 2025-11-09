from torch.utils.data import DataLoader, random_split
from example_056_custom_dataset import ToyDataset

# Example 65: Iterate over val set
ds = ToyDataset()
n = len(ds)
train_size = int(0.8 * n)
val_size = n - train_size
_, val_ds = random_split(ds, [train_size, val_size])
val_loader = DataLoader(val_ds, batch_size=16)
for xb, yb in val_loader:
    print("batch", xb.shape)
    break
