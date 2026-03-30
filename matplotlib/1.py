import matplotlib.pyplot as plt
x=["mon","tue","wed","thus","fri","sat","sun"]
y=[10,20,30,40,10,20,70]
plt.bar(x,y,color="green")
plt.ylabel("users")
plt.xlabel("days")
plt.title("weekly report")
plt.show()
plt.pie(y,labels=x)
plt.show()