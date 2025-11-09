import torch
import torch.nn as nn

# Example 45: Tiny binary classifier
class TinyBin(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(2, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))

model = TinyBin()
print(model(torch.rand(1, 2)))
