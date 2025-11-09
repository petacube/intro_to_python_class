import torch

# Example 42: Sigmoid for binary output
logits = torch.tensor([0.0, 1.0, -1.0])
probs = torch.sigmoid(logits)
print(probs)
