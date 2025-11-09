import torch
import torch.nn as nn
import torch.nn.functional as F

# Example 80: One-epoch image-like training stub
cnn = nn.Sequential(
    nn.Conv2d(1, 4, 3, padding=1),
    nn.ReLU(),
    nn.Flatten(),
    nn.Linear(4*8*8, 10),
)

images = torch.rand(16, 1, 8, 8)
labels = torch.randint(0, 10, (16,))

opt = torch.optim.SGD(cnn.parameters(), lr=0.1)
opt.zero_grad()
loss = F.cross_entropy(cnn(images), labels)
loss.backward()
opt.step()
print("loss:", loss.item())
