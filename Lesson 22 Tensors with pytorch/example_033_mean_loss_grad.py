import torch

# Example 33: Gradient of mean loss
w = torch.randn(4, requires_grad=True)
x = torch.ones(4)
y = (w * x).mean()
y.backward()
print("w:", w)
print("grad:", w.grad)
