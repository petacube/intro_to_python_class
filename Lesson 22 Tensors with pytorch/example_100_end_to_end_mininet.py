import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

# Example 100: End-to-end mini pipeline
class ToyDataset(Dataset):
    def __init__(self):
        self.x = torch.randn(200, 2)
        self.y = (self.x.sum(dim=1) > 0).float()

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

class MiniNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, 1),
        )

    def forward(self, x):
        return self.net(x)

def train_one_epoch(model, loader, optimizer, loss_fn):
    model.train()
    total_loss = 0.0
    for xb, yb in loader:
        optimizer.zero_grad()
        logits = model(xb)
        loss = loss_fn(logits.squeeze(), yb)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)

if __name__ == "__main__":
    ds = ToyDataset()
    loader = DataLoader(ds, batch_size=16, shuffle=True)
    model = MiniNet()
    opt = torch.optim.Adam(model.parameters(), lr=0.05)
    loss_fn = nn.BCEWithLogitsLoss()
    for epoch in range(5):
        loss = train_one_epoch(model, loader, opt, loss_fn)
        print(f"Epoch {epoch}: {loss:.4f}")
