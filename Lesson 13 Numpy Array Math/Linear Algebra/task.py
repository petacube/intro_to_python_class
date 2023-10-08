import numpy as np

csv = np.genfromtxt('data.csv', delimiter=',')
values, labels = # TODO

weights_layer1 = np.array([[-1.6418692, 0.12774534, -0.24612784, -0.25524955, 0.12560976],
                           [-0.19347666, -1.666441, 1.55708214, 1.59235961, -1.66955242]])
weights_layer2 = np.array([[-0.07468147],
                           [15.38341971],
                           [-1.7278774],
                           [-1.87559364],
                           [15.84439259]])


# The sigmoid activation function.
def activation(x):
    return 1.0 / (1.0 + np.exp(-x))


def predict(data):
    result_layer1 = # TODO
    result_layer2 = # TODO
    return (result_layer2 > 0.5).astype(np.int64)  # This converts the resulting
    # floats to ints, which can be compared with actual data labels.


if __name__ == '__main__':
    result = predict(values)
    labels = labels.reshape(labels.shape[0], 1)
    print('Predicted\tActual')
    for i in range(result.shape[0]):
        print(result[i], '\t', labels[i])
    #  Estimate prediction accuracy as a fraction of
    #  correctly predicted labels from all labels.
    print('\nPrediction accuracy: ', (result == labels).sum() / len(labels))
