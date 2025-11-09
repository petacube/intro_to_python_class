import torch

# Example 83: Ensure data + model on same device
def to_device(data, device):
    if isinstance(data, (list, tuple)):
        return [to_device(d, device) for d in data]
    return data.to(device)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.rand(2, 3)
y = torch.rand(2, 1)
x_d, y_d = to_device([x, y], device)
print(x_d.device, y_d.device)
