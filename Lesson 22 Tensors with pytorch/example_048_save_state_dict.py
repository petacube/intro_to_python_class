import torch
import torch.nn as nn

# Example 48: Save model state dict
model = nn.Sequential(
    nn.Linear(10, 10),
    nn.ReLU(),
    nn.Linear(10, 2),
)
torch.save(model.state_dict(), "model_example_48.pth")
print("Saved to model_example_48.pth")
