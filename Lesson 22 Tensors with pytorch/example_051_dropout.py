import torch
import torch.nn as nn

# Example 51: Dropout example
drop = nn.Dropout(p=0.5)
x = torch.ones(10)
print(drop(x))
