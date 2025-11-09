import torch
import torch.nn as nn
import torch.nn.functional as F

# Example 41: Two-layer network
class TwoLayerNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(2, 4)
        self.fc2 = nn.Linear(4, 1)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

net = TwoLayerNet()
out = net(torch.rand(1, 2))
print(out)
