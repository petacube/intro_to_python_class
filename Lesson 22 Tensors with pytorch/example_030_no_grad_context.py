import torch

# Example 30: torch.no_grad()
x = torch.randn(3, requires_grad=True)
with torch.no_grad():
    y = x * 2
print("requires_grad for y?", y.requires_grad)
