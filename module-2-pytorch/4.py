import torch

x = torch.tensor([1.0, 2.0])   # input
w = torch.tensor([3.0, 4.0], requires_grad=True)  # weights
b = torch.tensor(1.0, requires_grad=True)  # bias

y = x.dot(w) + b

print(y)

target = torch.tensor(5.0)

loss = (y - target)**2
print(loss)
loss.backward()
print(w.grad)
print(b.grad)

learning_rate = 0.01

with torch.no_grad():
    w -= learning_rate * w.grad
    b -= learning_rate * b.grad

print(w)
print(b)

y = x.dot(w) + b
print(y)

for i in range(20):
    y = x.dot(w) + b
    loss = (y - target)**2
    
    loss.backward()

    print("grad w:", w.grad, "grad b:", b.grad)

    with torch.no_grad():
        w -= 0.01 * w.grad
        b -= 0.01 * b.grad

        w.grad.zero_()
        b.grad.zero_()

    print(f"Step {i}: y = {y.item()}, loss = {loss.item()}")

