#Python supply curve by matplotlib
import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

QuantityS = np.arange(10,30,5)
price = np.arange(250,450,50)

fig ,ax = plt.subplots()
ax.plot(QuantityS,price,"g--")
ax.grid()

ax.set(xlabel="Quantity supplied",ylabel="Price (kshs)",title="Supply curve")

fig.savefig("supply.png")
plt.show()

