import matplotlib.pyplot as plt

OperatingSystem=['Windows','MacBook','Linux','Other device']
users=[70,60,55,43]

plt.bar('Windows',70,color='red')
plt.bar('MacBook',60,color='yellow')
plt.bar('Linux',65,color='green')
plt.bar('Other device',43,color='blue')

plt.xlabel("Operating System")
plt.ylabel("users")
plt.title("Operating system")
plt.show()