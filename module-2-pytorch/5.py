# simple neural network (1 neuron) without PyTorch

# inputs
x1 = 1.0
x2 = 2.0

# weights (initial guess)
w1 = 3.0
w2 = 4.0
b = 1.0

target = 20.0
learning_rate = 0.01

for i in range(20):

    # 🔹 forward pass
    y = x1*w1 + x2*w2 + b

    # 🔹 loss
    loss = (y - target) ** 2

    # 🔹 error
    error = y - target

    # 🔹 BACKPROP (manual gradients)
    grad_w1 = 2 * error * x1
    grad_w2 = 2 * error * x2
    grad_b  = 2 * error

    # 🔹 update weights
    w1 = w1 - learning_rate * grad_w1
    w2 = w2 - learning_rate * grad_w2
    b  = b  - learning_rate * grad_b

    print(f"Step {i}: y={y:.2f}, loss={loss:.2f}")