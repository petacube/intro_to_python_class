import torch

# Example 29: Zero gradients
x = torch.tensor(1.0, requires_grad=True)
for step in range(3):
    y = x * 2
    y.backward()
    print(f"step {step}, grad:", x.grad.item())
    x.grad.zero_()
