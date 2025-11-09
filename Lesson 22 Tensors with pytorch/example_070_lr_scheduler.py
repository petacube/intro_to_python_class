import torch
import torch.nn as nn

# Example 70: Learning rate schedule
model = nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=2, gamma=0.1)

for epoch in range(3):
    # pretend training here
    scheduler.step()
    print("Epoch", epoch, "LR:", scheduler.get_last_lr())
