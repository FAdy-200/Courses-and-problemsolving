import matplotlib.pyplot as plt
import numpy as np
a = np.arange(0.1, 100, 0.1)
b = lambda x : (x/2)*np.log2(x)**2
c = lambda x : (x/2)*np.log2(x)
y = b(a)
y2 = c(a)
plt.plot(a,y2)
plt.plot(a,y)
plt.plot(a,a**2)
plt.text(100,b(100),str(b(100)))
plt.text(100,c(100),str(c(100)))
plt.text(100,100**2,str(100**2))
plt.legend([r"$\frac{n}{2}log_2(n)$",r"$\frac{n}{2} log_2(n)^2$",r"$n^2$"],prop={'size':20})
plt.fill_between(a,y,y2,color="red",alpha=0.2)
plt.fill_between(a,y,a**2,color="#A796C1",alpha=0.2)
plt.box(False)
plt.tick_params("both",length = 0,labelsize=0)
plt.tick_params("x",labelsize=10)
plt.show()




