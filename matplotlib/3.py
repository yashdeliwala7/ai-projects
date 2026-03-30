import matplotlib.pyplot as plt

x = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
y = [10,20,30,40,10,20,70]   # users
clicks=[50,100,25,222,669,999,123]

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(x,y)
plt.title("users")
plt.subplot(2,2,2)
plt.bar(x,clicks)
plt.title("clicks")
plt.subplot(2,2,3)
plt.pie(y)
plt.title("users")
plt.subplot(2,2,4)
plt.scatter(x,y)
plt.title("users")
plt.show()

