import torch

# Example 35: Simple manual SGD step to fit w ≈ 2
w = torch.tensor(5.0, requires_grad=True)
lr = 0.1
for step in range(5):
    loss = (w - 2) ** 2
    loss.backward()
    with torch.no_grad():
        w -= lr * w.grad
        w.grad.zero_()
    print(f"step {step}, w = {w.item():.4f}")
