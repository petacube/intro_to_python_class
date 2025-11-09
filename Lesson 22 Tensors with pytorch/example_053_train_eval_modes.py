import torch
import torch.nn as nn

# Example 53: Switch between train/eval
model = nn.Dropout(p=0.5)
x = torch.ones(5)

model.train()
print("train:", model(x))

model.eval()
print("eval:", model(x))
