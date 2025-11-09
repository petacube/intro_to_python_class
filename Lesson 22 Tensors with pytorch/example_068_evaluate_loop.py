import torch
from torch.utils.data import DataLoader, random_split
import torch.nn as nn
from example_056_custom_dataset import ToyDataset

# Example 68: Evaluation loop
def evaluate(model, loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for xb, yb in loader:
            logits = model(xb.float())
            preds = (torch.sigmoid(logits) > 0.5).long().squeeze()
            correct += (preds == yb).sum().item()
            total += len(yb)
    return correct / total

ds = ToyDataset()
n = len(ds)
train_size = int(0.8 * n)
val_size = n - train_size
train_ds, val_ds = random_split(ds, [train_size, val_size])
train_loader = DataLoader(train_ds, batch_size=16, shuffle=True)
val_loader = DataLoader(val_ds, batch_size=16)

model = nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.BCEWithLogitsLoss()

# quick one-epoch train
for xb, yb in train_loader:
    optimizer.zero_grad()
    loss = loss_fn(model(xb.float()), yb.float().unsqueeze(1))
    loss.backward()
    optimizer.step()
    break

print("Accuracy:", evaluate(model, val_loader))
