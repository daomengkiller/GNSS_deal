import matplotlib.pyplot as plt
import numpy as np
plt.ion()
x = 1
y = 1
t = 1
while True:
    if t % 10==0 and t<100:
        plt.scatter(x, y, c='r', marker='.')
        x=np.random.normal(0,1)
        y=np.random.normal(0,1)
    t=t+1
    plt.pause(0.000001)
print('tuichu')


