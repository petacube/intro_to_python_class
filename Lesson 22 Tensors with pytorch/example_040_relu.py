import torch
import torch.nn.functional as F

# Example 40: ReLU activation
x = torch.tensor([[-1.0, 0.5, 2.0]])
y = F.relu(x)
print(y)
