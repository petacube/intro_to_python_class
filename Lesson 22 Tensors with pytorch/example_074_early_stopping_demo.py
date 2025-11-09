# Example 74: Very simple early stopping pattern (synthetic, illustrative only)
best_acc = 0.8
patience = 3
wait = 0

for epoch in range(20):
    # fake accuracy that decreases after some epochs
    acc = 1.0 - 0.02 * epoch
    if acc > best_acc:
        best_acc = acc
        wait = 0
    else:
        wait += 1
    if wait >= patience:
        print("Stop early at epoch", epoch)
        break
