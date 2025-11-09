import torch
import torch.nn as nn

# Example 96: Text-like token embeddings -> average
emb = nn.Embedding(50, 8)
tokens = torch.tensor([[1, 2, 3], [4, 5, 0]])
vecs = emb(tokens)
sentence_vec = vecs.mean(dim=1)
print(sentence_vec.shape)
