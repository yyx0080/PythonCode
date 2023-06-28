import numpy as np
from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(sparse_output=False)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_input_hidden = np.random.randn(self.input_size, self.hidden_size)
        self.weights_hidden_output = np.random.randn(self.hidden_size, self.output_size)

    def forward(self, X):
        self.hidden = sigmoid(np.dot(X, self.weights_input_hidden))
        self.output = sigmoid(np.dot(self.hidden, self.weights_hidden_output))
        return self.output

    def backward(self, X, y, learning_rate):
        output_error = y - self.output
        output_delta = output_error * sigmoid_derivative(self.output)

        hidden_error = np.dot(output_delta, self.weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden)

        self.weights_hidden_output += learning_rate * np.dot(self.hidden.T, output_delta)
        self.weights_input_hidden += learning_rate * np.dot(X.T, hidden_delta)

    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)

    def predict(self, X):
        return np.argmax(self.forward(X), axis=1) + 1

def load_data(file_path):
    data = np.genfromtxt(file_path, delimiter=',', dtype=str)
    X = data[:, :-1].astype(float)
    class_labels = np.unique(data[:, -1])
    y = np.zeros(data.shape[0])
    for i, label in enumerate(class_labels):
        y[data[:, -1] == label] = i + 1
    y = y.reshape(-1, 1)
    encoder = OneHotEncoder(sparse=False)
    y = encoder.fit_transform(y)
    return X, y


def calculate_accuracy(predictions, targets):
    correct = np.sum(predictions == targets)
    total = targets.shape[0]
    accuracy = correct / total
    return accuracy

def main():
    train_file = 'Iris.txt.txt'
    test_file = 'Iris.test.txt'

    X_train, y_train = load_data(train_file)
    X_test, y_test = load_data(test_file)

    input_size = X_train.shape[1]
    hidden_size = 10
    output_size = 3

    epochs = 1000
    learning_rate = 0.1
    num_runs = 10

    accuracies = []
    for run in range(num_runs):
        nn = NeuralNetwork(input_size, hidden_size, output_size)
        nn.train(X_train, y_train, epochs, learning_rate)
        predictions = nn.predict(X_test)
        accuracy = calculate_accuracy(predictions, y_test)
        accuracies.append(accuracy)

    mean_accuracy = np.mean(accuracies)
    std_accuracy = np.std(accuracies)
    print("Accuracy for each run:", accuracies)
    print("Mean Accuracy:", mean_accuracy)
    print("Standard Deviation:", std_accuracy)

if __name__ == '__main__':
    main()
