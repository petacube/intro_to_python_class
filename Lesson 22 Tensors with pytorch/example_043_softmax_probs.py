import torch
import torch.nn.functional as F

# Example 43: Softmax for multi-class
logits = torch.tensor([[2.0, 1.0, 0.1]])
probs = F.softmax(logits, dim=1)
print(probs)
print("sum:", probs.sum().item())
