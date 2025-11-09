import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from example_056_custom_dataset import ToyDataset

# Example 66: Generic training loop skeleton
def train_one_epoch(model, loader, optimizer, loss_fn):
    model.train()
    total_loss = 0.0
    for xb, yb in loader:
        optimizer.zero_grad()
        preds = model(xb.float())
        loss = loss_fn(preds.squeeze(), yb.float())
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)

if __name__ == "__main__":
    ds = ToyDataset()
    loader = DataLoader(ds, batch_size=16, shuffle=True)
    model = nn.Sequential(nn.Linear(2, 1))
    opt = torch.optim.SGD(model.parameters(), lr=0.1)
    loss_fn = nn.BCEWithLogitsLoss()
    print("loss:", train_one_epoch(model, loader, opt, loss_fn))
