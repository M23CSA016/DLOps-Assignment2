from activation import sigmoid_func, relu_func, leaky_relu, tanh_func

input_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

print(f"Sigmoid Values: {[sigmoid_func(x) for x in input_values]}")
print(f"ReLU Values: {[relu_func(x) for x in input_values]}")
print(f"Leaky ReLU Values: {[leaky_relu(x) for x in input_values]}")
print(f"Tanh Values: {[tanh_func(x) for x in input_values]}")

# Bug of wrong tanh function 