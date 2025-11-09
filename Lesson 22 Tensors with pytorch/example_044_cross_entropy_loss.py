import torch
import torch.nn.functional as F

# Example 44: Cross-entropy loss
logits = torch.tensor([[2.0, 0.5, -1.0]])  # shape (N, C)
labels = torch.tensor([0])                 # class index
loss = F.cross_entropy(logits, labels)
print(loss.item())
