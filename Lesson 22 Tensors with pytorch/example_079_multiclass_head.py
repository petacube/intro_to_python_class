import torch
import torch.nn as nn
import torch.nn.functional as F

# Example 79: Multiclass head
model = nn.Linear(4, 3)
x = torch.rand(5, 4)
y = torch.randint(0, 3, (5,))
loss = F.cross_entropy(model(x), y)
loss.backward()
print("loss:", loss.item())
