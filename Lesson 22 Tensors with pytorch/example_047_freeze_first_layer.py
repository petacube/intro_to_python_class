import torch.nn as nn

# Example 47: Disable gradients for first layer
model = nn.Sequential(
    nn.Linear(10, 10),
    nn.ReLU(),
    nn.Linear(10, 2),
)

for param in model[0].parameters():
    param.requires_grad = False

for name, p in model.named_parameters():
    print(name, "requires_grad:", p.requires_grad)
