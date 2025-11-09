import torch.nn as nn

# Example 88: Count trainable params only
model = nn.Sequential(
    nn.Linear(10, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
print("Trainable:", trainable)
