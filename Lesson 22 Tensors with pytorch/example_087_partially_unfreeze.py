import torch.nn as nn

# Example 87: Partially unfreeze
model = nn.Sequential(
    nn.Linear(10, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

for p in model.parameters():
    p.requires_grad = False

for name, p in model.named_parameters():
    if "weight" in name:
        p.requires_grad = True

for name, p in model.named_parameters():
    print(name, "requires_grad:", p.requires_grad)
