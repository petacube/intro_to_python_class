import torch.nn as nn

# Example 86: Freeze entire model
model = nn.Linear(2, 1)
for p in model.parameters():
    p.requires_grad = False

for name, p in model.named_parameters():
    print(name, "requires_grad:", p.requires_grad)
