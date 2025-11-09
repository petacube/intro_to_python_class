import torch
import torch.nn as nn

# Example 95: Tiny RNN demo
rnn = nn.RNN(input_size=5, hidden_size=3, batch_first=True)
x = torch.rand(2, 4, 5)  # (batch, seq, features)
out, h = rnn(x)
print("out shape:", out.shape)
print("h shape:", h.shape)
