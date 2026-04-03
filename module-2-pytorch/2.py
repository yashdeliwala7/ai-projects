import torch
a=torch.tensor([1,2,3])
b=torch.tensor([4,5,6])

print(a+b)
print(a*b)
print(torch.dot(a,b))

import torch

x = torch.tensor(3.0,requires_grad=True)
y = x * x + 3*x

y.backward()

print(x.grad)
