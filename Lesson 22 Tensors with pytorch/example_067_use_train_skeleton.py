import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset
from example_066_train_one_epoch_skeleton import train_one_epoch

# Example 67: Use skeleton with simple model
ds = ToyDataset()
loader = DataLoader(ds, batch_size=16, shuffle=True)
model = nn.Sequential(nn.Linear(2, 1))
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.BCEWithLogitsLoss()

for epoch in range(5):
    loss = train_one_epoch(model, loader, optimizer, loss_fn)
    print(f"Epoch {epoch}: {loss:.4f}")
