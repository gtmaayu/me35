import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(xlim =[-20,20], ylim=[-20,20])

l1 = 7.0 #base link
l2 = 13.0
def fk(theta_1,theta_2):
    '''
    t1,t2 radians -> x,y
    '''
    X = l1*np.cos(theta_1) + l2*np.cos(theta_1 + theta_2)
    Y = l1*np.sin(theta_1) + l2*np.sin(theta_1 + theta_2)
    return (X,Y)

def animate(i):
    print("here")
    graph_data = open('/Users/ngimahyolmo/Desktop/me35/angles.txt','r').read()
    lines = graph_data.split('\n')
    t11 = []
    t22 = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x, y = line.split(',')
            x, y = line.split(',')
            xs = float(x)
            ys = float(y)
            theta1,theta2 = fk(np.deg2rad(xs),np.deg2rad(ys))
            print(theta1)
            print(theta2)
            t11.append((-1*theta1))
            t22.append((theta2))
    ax1.scatter(t22, t11,marker='o', color='r')

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
