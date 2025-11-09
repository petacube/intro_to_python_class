import torch
import torch.nn as nn

# Example 94: Embedding lookup
emb = nn.Embedding(num_embeddings=10, embedding_dim=4)
idx = torch.tensor([1, 3, 5])
print(emb(idx))
