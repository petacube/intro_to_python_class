import torch
import torch.nn as nn

# Example 49: Load model state dict
model = nn.Sequential(
    nn.Linear(10, 10),
    nn.ReLU(),
    nn.Linear(10, 2),
)
state = torch.load("model_example_48.pth")
model.load_state_dict(state)
print("Loaded weights from model_example_48.pth")
