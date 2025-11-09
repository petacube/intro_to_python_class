import random

# Example 75: Logging loss values
train_losses = []
for epoch in range(5):
    loss = random.random()
    train_losses.append(loss)
print(train_losses)
