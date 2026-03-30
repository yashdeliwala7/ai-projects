import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,20,30,40,50]

plt.figure(figsize=(10,10))
plt.plot(x,y)
plt.show()
plt.figure(figsize=(10,10))
plt.scatter(x,y)
plt.show()
plt.figure(figsize=(10,10))
plt.bar(x,y)
plt.show()
plt.figure(figsize=(10,10))
plt.pie(y)
plt.show()