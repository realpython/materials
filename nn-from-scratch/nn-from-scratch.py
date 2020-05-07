import numpy as np
import pandas as pd

class ActivationFunctions:
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @classmethod
    def sigmoid_prime(cls, x):
        return cls.sigmoid(x) * (1 - cls.sigmoid(x))

    @staticmethod
    def tanh(x):
        return math.tanh(x)

    @staticmethod
    def relu(x):
        if x < 0:
            return 0
        return x
        

class Layer:
    def __init__(self, node_count, layer_number, previous_layer, activation_function=None, a_prime=None):
        self.node_count = node_count
        self.layer_number = layer_number
        self.actf = ActivationFunctions.sigmoid
        self.actf_prime = ActivationFunctions.sigmoid_prime

        # Used to navigate the network
        self.prev_layer = previous_layer
        self.next_layer = None

        # Used by backprop
        self.activations = []
        self.zs = []
        self.backprop_delta_w = []
        self.backprop_delta_b = []
        self.delta = []

        # The input layer doesn't have a previous layer; handle that case
        if previous_layer is not None:
            num_inputs = previous_layer.node_count
            self.prev_layer.next_layer = self
        else:
            num_inputs = 1

        # Create a matrix to hold the weights and biases, initialized to random numbers
        self.weights = np.random.randn(self.node_count, num_inputs)
        print(f"Making Weights Matrix for layer {layer_number} {self.node_count}x{num_inputs}")
        self.biases = np.random.randn(self.node_count, 1)
        print(f"Making Bias Vector for layer {layer_number} {self.node_count}x1")

    def debug_print(self):
        print(f"Layer {self.layer_number}")
        print(f"\tWeights dim: f{self.weights.shape}")
        print(f"\tBiases dim: f{self.biases.shape}")
        print(f"\tActivations dim: f{self.activations.shape}")


class Network:
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes

        self.layer_count = len(layer_sizes)

        self.layers = []

        # Create the input layer first
        self.input_layer = Layer(node_count=layer_sizes[0], layer_number=0,
                                 previous_layer=None)
        self.layers.append(self.input_layer)

        # Now create all the other layers
        previous_layer = self.input_layer
        for i, node_count in enumerate(layer_sizes[1:]):
            layer = Layer(node_count, layer_number=i+1,
                          previous_layer=previous_layer
                          )
            self.layers.append(layer)

            previous_layer = layer

        # let's grab a reference to the output layer to make it more clear when
        # we're using it
        self.output_layer = self.layers[-1]

    def calc_cost(self, actuals, predictions):

        cost = 0.0
        for actual, prediction in zip(actuals, predictions):
            cost += (prediction - actual) ** 2

        cost = cost * .5 * (1 / len(actuals))

        return float(cost)

    def feedforward(self, input):

        # The input is the value of the first layer, no computation necessary
        # (We reshape it so it's a column vector)
        self.input_layer.activations = input.reshape(-1, 1)

        # Now process each layer, skipping the first layer (this is the input layer)
        for layer in self.layers[1:]:
            prev_layer = layer.prev_layer
            activation_function = layer.actf

            z_vec = np.dot(layer.weights, prev_layer.activations) + layer.biases
            a_vec = activation_function(z_vec)

            # These will be used by backprop
            layer.zs = z_vec
            layer.activations = a_vec

        # The output is just the last a_vec
        return a_vec

    def evaluate(self, xs, ys):
        total_cost = 0.0
        num_correct = 0

        ys = ys.reshape(-1, 1)

        for x, y in zip(xs, ys):
            x = x.reshape(-1, 1)
            a = self.feedforward(x)
            prediction = int(round(a[0][0]))
            total_cost += self.calc_cost(y, a)
            if prediction == y:
                num_correct += 1

        percent_correct = num_correct / len(xs)

        return total_cost, num_correct, percent_correct

    def train(self, train_x, train_y, test_x, test_y, iterations=500, learning_rate=3.0):
        """
        While we only need the training data to train the network, we bas in testing_data so we can
            determine if we're overfitting.

        :param training_data:
        :param testing_data:
        :param iterations
        :param learning_rate:
        :return:
        """

        train_costs = []
        train_percent_correct = []

        test_costs = []
        test_percent_correct = []

        for i in range(iterations):
            print(f"Iteration {i}")
            # Go through every training sample and preform backprop.
            # Then average the "nudges" and apply them to the weights and biases

            # Initialize a data structure to hold the results of back prop.
            # It just creates a list for each layer
            all_dws = [[] for l in range(self.layer_count - 1)]
            all_dbs = [[] for l in range(self.layer_count - 1)]

            for x, y in zip(train_x, train_y):
                # Run backprop and get the changes
                # Note the input layer doesn't have any dws or dbs
                dws, dbs = self.backprop(x, y)

                # The dws and dbs come back by layer. Let's save them off appropriately.
                for i, dws_for_layer in enumerate(dws):
                    all_dws[i].append(dws_for_layer)

                for i, dbs_for_layer in enumerate(dbs):
                    all_dbs[i].append(dbs_for_layer)

            # Now we have a list of all the changes we'd make in each example. We can only make
            # one change though, so we add them all together
            final_dbs, final_dws = self.combine_dws_and_dbs(all_dbs, all_dws)

            # Now subtract the updates (scaled by the learning rate) to the weights and biases
            for layer, nws, nbs in zip(self.layers[1:], final_dws, final_dbs):
                updated_weights = layer.weights - (learning_rate * nws)
                layer.weights = updated_weights

                updated_biases = layer.biases - (learning_rate * nbs)
                layer.biases = updated_biases

            # Now we can evaluate how well it did
            train_cost, train_correct, train_percent = self.evaluate(train_x, train_y)
            test_cost, test_correct, test_percent = self.evaluate(test_x, test_y)

            print(f"Training\n"
                  f"\tCost: {train_cost:.2f}\n "
                  f"\tCorrect: ({train_correct}/{len(train_x)}) {train_percent * 100:.1f}%")

            print(f"Test\n"
                  f"\tCost: {test_cost:.2f}\n"
                  f"\tCorrect: ({test_correct}/{len(test_x)}) {test_percent * 100:.1f}%")
            print("-"*40)
            train_costs.append(train_cost)
            train_percent_correct.append(train_percent)

            test_costs.append(test_cost)
            test_percent_correct.append(test_percent)

        df = pd.DataFrame({"Training Cost": train_costs,
                           "Training % Correct": train_percent_correct,
                           "Test Cost": test_costs,
                           "Test % Correct": test_percent_correct
                           })

        # Write out the results for later analysis
        df.to_csv("../training_results.csv", index=False)

        # Return the accuracy of the final iteration
        return test_percent

    def combine_dws_and_dbs(self, all_dbs, all_dws):
        # This iterate through each layer
        final_dws = []
        for adw in all_dws:
            sum_dw = adw[0]
            for dw in adw:
                sum_dw += dw

            # We end up with one set of values for each later
            final_dws.append(sum_dw)
        final_dbs = []
        for adb in all_dbs:
            sum_db = adb[0]
            for db in adb:
                sum_db += db

            final_dbs.append(sum_db)
        return final_dbs, final_dws

    def backprop(self, train_x, train_y):
        # Step 1: Feed forward
        # We don't care about the return value here. We can recover it from the state we saved
        # during the feedforward step.
        _ = self.feedforward(train_x)

        # Step 2: "Seed" the backprop. The output layer is computed a little differently,
        #       so we do it first. After this, a loop can take care of the rest of the layers
        output_layer = self.output_layer
        prev_layer = self.output_layer.prev_layer

        # These activations are just the output of the NN
        output_diff = output_layer.activations - train_y    # This is actually the derivative of the cost function
        delta = output_diff * output_layer.actf_prime(output_layer.zs)

        output_layer.backprop_delta_b = delta
        output_layer.delta = delta
        output_layer.backprop_delta_w = np.dot(delta, prev_layer.activations.transpose())

        # Step 3: Using the above step as the start, propagate the error backward through
        #           the layers
        #         We skip the output layer because we already did that above.
        #         We also skip the input layer because it doesn't have any weights or biases

        for layer in reversed(self.layers[1:-1]):
            forward_layer = layer.next_layer
            prev_layer = layer.prev_layer

            sp = layer.actf_prime(layer.zs)
            delta = np.dot(forward_layer.weights.transpose(), forward_layer.delta) * sp
            layer.backprop_delta_b = delta
            layer.delta = delta

            layer.backprop_delta_w = np.dot(delta, prev_layer.activations.transpose())

        # Step 4, pass back what we computed the changes should be for each layer
        dws = []
        dbs = []
        for layer in self.layers[1:]:
            dws.append(layer.backprop_delta_w)
            dbs.append(layer.backprop_delta_b)

        return dws, dbs


if __name__ == "__main__":

    
    from sklearn.datasets import load_breast_cancer
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    
    # load the dataset
    dataset = load_breast_cancer()
    
    X = dataset.data
    Y = dataset.target
    
    # Normalize the data
    scaler = StandardScaler()
    
    scaler.fit(X)
    X = scaler.transform(X)
    
    # Create a Training and Testing Set
    train_x, test_x, train_y, test_y = train_test_split(X, Y)
    train_y = train_y.reshape(-1, 1)
    test_y = test_y.reshape(-1, 1)
    
    # Setup the network
    network = Network([30, 30, 10, 1])
    
    # Train our network!
    # (Note that his automatically prints out training data)
    accuracy = network.train(train_x, train_y, test_x, test_y, iterations=200, learning_rate=.01)
    
    print(f"Accuracy: {accuracy * 100:.1f}%")
