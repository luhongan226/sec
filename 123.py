import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t)

def g(t):
    return np.exp(t)

def h(t):
    return np.exp(0*t)

def a(t):
    return 2*np.cos(t+0.4)

def b(t):
    return 0.5*c(t)*np.cos(t+0.4)

def c(t):
    return np.exp(0.05*t)

def d(t):
    return np.exp(0.05*-t)
def e(t):
    return 0.5*d(t)*np.cos(t+0.4)


t1 = np.arange(-5.0, 5.0, 0.1)
t2 = np.arange(-5.0, 5.0, 0.1)
t3 = np.arange(-50, 50, 0.1)

plt.figure(2)            # Called implicitly but can use# for multiple figures
plt.subplot(222)      # 2 rows, 1 column, 1stplot
plt.plot(t1, a(t1), 'b-')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-5,5))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("X(t)=2cos(t+0.4)")

plt.subplot(223)      # 2 rows, 1 column, 2ndplot

ax = plt.gca()
plt.plot(t3, b(t3), 'r-')
#设置坐标轴范围
plt.xlim((-20, 50))
plt.ylim((-5, 5))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("0.5*e^(t)*cos(t+0.4)")

plt.subplot(224)      # 2 rows, 1 column, 2ndplot

ax = plt.gca()
plt.plot(t3, e(t3), 'g-')
#设置坐标轴范围
plt.xlim((-50, 20))
plt.ylim((-5, 5))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
#设置坐标轴刻度
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("0.5*e^(t)*cos(t+0.4)")

plt.subplot(221)      # 2 rows, 2 column, 3ndplot

plt.plot(t1, f(t1), '-b',label='X(t)=e^-t')
plt.plot(t2, g(t2), '-r',label='X(t)=e^t')
plt.plot(t2, h(t2), 'g-',label='X(t)=e^0=1')
plt.legend(loc='best')
#设置坐标轴范围
plt.xlim((-5, 5))
plt.ylim((-1,10))
#设置坐标轴名称
plt.xlabel('t/s')
plt.ylabel('X(t)')
ax = plt.gca()                                            # get current axis 获得坐标轴对象
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')         # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')          # 指定下边的边作为 x 轴   指定左边的边为 y 轴
ax.spines['bottom'].set_position(('data', 0))   #指定 data  设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))
plt.title("Functional Equation:")


plt.show()