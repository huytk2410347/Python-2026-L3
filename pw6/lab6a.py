import numpy as np
import matplotlib.pyplot as po

x = np.linspace(-5, 5, 200)
y = 2 * x + np.sin(x) ** 2 + 3

po.plot(x,y)
po.grid(True)
po.title("Hello, po!")
po.xlabel("x")
po.ylabel("y")
po.savefig("po.pdf")
po.show