# inputs
x1 = 1.0
x2 = 2.0

# weights
w1, w2 = 0.5, -1.0
w3, w4 = 1.5, 2.0
w5, w6 = -1.0, 1.0

# biases
b1, b2, b3 = 0.0, 0.0, 0.0

target = 10.0
lr = 0.01

for i in range(20):

    # 🔹 forward pass
    h1 = x1*w1 + x2*w2 + b1
    h2 = x1*w3 + x2*w4 + b2

    y = h1*w5 + h2*w6 + b3

    # 🔹 loss
    loss = (y - target)**2

    # 🔹 error
    error = y - target

    # 🔹 BACKPROP

    # output layer gradients
    grad_w5 = 2 * error * h1
    grad_w6 = 2 * error * h2
    grad_b3 = 2 * error

    # hidden layer gradients
    grad_h1 = 2 * error * w5
    grad_h2 = 2 * error * w6

    grad_w1 = grad_h1 * x1
    grad_w2 = grad_h1 * x2
    grad_b1 = grad_h1

    grad_w3 = grad_h2 * x1
    grad_w4 = grad_h2 * x2
    grad_b2 = grad_h2

    # 🔹 update
    w1 -= lr * grad_w1
    w2 -= lr * grad_w2
    w3 -= lr * grad_w3
    w4 -= lr * grad_w4
    w5 -= lr * grad_w5
    w6 -= lr * grad_w6

    b1 -= lr * grad_b1
    b2 -= lr * grad_b2
    b3 -= lr * grad_b3

    print(f"Step {i}: y={y:.2f}, loss={loss:.2f}")