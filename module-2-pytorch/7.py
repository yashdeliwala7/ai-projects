# -------- MLP FROM SCRATCH (NO PYTORCH) --------

# inputs
x1 = 1.0
x2 = 2.0

# weights (random start)
w1, w2 = 0.5, -1.0
w3, w4 = 1.5, 2.0

w5, w6 = -1.0, 1.0

# biases
b1, b2, b3 = 0.0, 0.0, 0.0

target = 10.0
lr = 0.01

def relu(x):
    return max(0, x)

def relu_derivative(x):
    return 1 if x > 0 else 0

data = [
    (1.0, 2.0, 10.0),
    (2.0, 3.0, 15.0),
    (3.0, 4.0, 20.0),
    (4.0, 5.0, 25.0)
]

for i in range(50):

    # 🔹 FORWARD PASS

    z1 = x1*w1 + x2*w2 + b1
    z2 = x1*w3 + x2*w4 + b2

    h1 = relu(z1)
    h2 = relu(z2)

    y = h1*w5 + h2*w6 + b3

    # 🔹 LOSS
    loss = (y - target) ** 2

    # 🔹 ERROR
    error = y - target

    # 🔹 BACKPROP

    # output layer
    grad_w5 = 2 * error * h1
    grad_w6 = 2 * error * h2
    grad_b3 = 2 * error

    # gradients wrt hidden outputs
    grad_h1 = 2 * error * w5
    grad_h2 = 2 * error * w6

    # apply ReLU derivative
    grad_z1 = grad_h1 * relu_derivative(z1)
    grad_z2 = grad_h2 * relu_derivative(z2)

    # hidden layer weights
    grad_w1 = grad_z1 * x1
    grad_w2 = grad_z1 * x2
    grad_b1 = grad_z1

    grad_w3 = grad_z2 * x1
    grad_w4 = grad_z2 * x2
    grad_b2 = grad_z2

    # 🔹 UPDATE

    w1 -= lr * grad_w1
    w2 -= lr * grad_w2
    w3 -= lr * grad_w3
    w4 -= lr * grad_w4

    w5 -= lr * grad_w5
    w6 -= lr * grad_w6

    b1 -= lr * grad_b1
    b2 -= lr * grad_b2
    b3 -= lr * grad_b3

    print(f"Step {i}: y={y:.2f}, loss={loss:.4f}")