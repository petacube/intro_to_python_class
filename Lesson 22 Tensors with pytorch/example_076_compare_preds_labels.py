import torch
import torch.nn as nn

# Example 76: Compare predictions vs labels
model = nn.Linear(2, 1)
x = torch.randn(10, 2)
y = (torch.rand(10, 1) > 0.5).float()
with torch.no_grad():
    logits = model(x)
    preds = (torch.sigmoid(logits) > 0.5).long().squeeze()
print("Pred:", preds[:10])
print("True:", y.view(-1)[:10])
