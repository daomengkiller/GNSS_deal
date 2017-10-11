import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import math
n=100
X=np.random.normal(0,1,n)
Y=np.random.normal(0,1,n)
# T=np.arctan2(Y,X)
N=28.22747458
E=113.09026568
plt.xlim(28.22747450,28.22747499)
plt.ylim(113.09026550,113.09026599)
plt.gca().xaxis.set_major_formatter(ticker.FormatStrFormatter('%.8f'))
plt.gca().yaxis.set_major_formatter(ticker.FormatStrFormatter('%.8f'))
plt.annotate("A", xy=(113.09026568, 28.22747458), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))
for t in range(n):
    x=N+X[t]*0.00000001
    y=E+Y[t]*0.00000001
    plt.scatter(x,y,c='r',marker='.')
    plt.pause(0.1)
plt.show()


