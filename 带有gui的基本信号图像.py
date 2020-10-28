import tkinter
def f1():
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.arange(-10.0, 10.0, 0.01)
    y1 = np.sin(x)

    plt.xlim((-5, 5))
    plt.ylim((-1, 10))

    plt.figure(1)
    plt.subplot(211)
    plt.plot(x, y1)

    plt.title("x(t)=Acos(wt+ψ)")

    plt.show()

def f2():
    import numpy as np
    import matplotlib.pyplot as plt

    def f(t):
        return np.exp(-t)

    def g(t):
        return np.exp(t)

    def h(t):
        return np.exp(0 * t)

    t1 = np.arange(-5.0, 5.0, 0.1)
    t2 = np.arange(-5.0, 5.0, 0.1)

    plt.plot(t1, f(t1), '-b', label='X(t)=e^-t')
    plt.plot(t2, g(t2), '-r', label='X(t)=e^t')
    plt.plot(t2, h(t2), 'g-', label='X(t)=e^0=1')
    plt.legend(loc='best')

    plt.xlim((-5, 5))
    plt.ylim((-1, 10))

    plt.xlabel('t/s')
    plt.ylabel('X(t)')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    plt.title("x(t)")

    plt.show()

def f3():
    import numpy as np
    import matplotlib.pyplot as plt

    def a(t):
        return 2 * np.cos(t + 0.4)

    def b(t):
        return 0.5 * c(t) * np.cos(t + 0.4)

    def d(t):
        return np.exp(0.05 * -t)

    def e(t):
        return 0.5 * d(t) * np.cos(t + 0.4)

    t1 = np.arange(-5.0, 5.0, 0.1)
    t2 = np.arange(-5.0, 5.0, 0.1)
    t3 = np.arange(-50, 50, 0.1)
    ax = plt.gca()
    plt.plot(t3, e(t3), 'g-')

    plt.xlim((-50, 20))
    plt.ylim((-5, 5))

    plt.xlabel('t/s')
    plt.ylabel('X(t)')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    plt.title("0.5*e^(t)*cos(t+0.4)")
    plt.show()

def f4():
    import numpy as np
    import matplotlib.pyplot as plt

    def f(t):
        return np.exp(-t)

    def g(t):
        return np.exp(t)

    def h(t):
        return np.exp(0 * t)

    def a(t):
        return 2 * np.cos(t + 0.4)

    def b(t):
        return 0.5 * c(t) * np.cos(t + 0.4)

    def c(t):
        return np.exp(0.05 * t)

    def d(t):
        return np.exp(0.05 * -t)

    def e(t):
        return 0.5 * d(t) * np.cos(t + 0.4)

    t1 = np.arange(-5.0, 5.0, 0.1)
    t2 = np.arange(-5.0, 5.0, 0.1)
    t3 = np.arange(-50, 50, 0.1)

    ax = plt.gca()
    plt.plot(t3, b(t3), 'r-')

    plt.xlim((-20, 50))
    plt.ylim((-5, 5))

    plt.xlabel('t/s')
    plt.ylabel('X(t)')

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))
    plt.title("0.5*e^(t)*cos(t+0.4)")

    plt.show()

win = tkinter.Tk()
win.title("作业")
win.geometry("400x400+200+20")

#创建按钮
button1 = tkinter.Button(win, text="正弦", command=f1, )
button1.pack()

button2 = tkinter.Button(win, text="指数", command=f2, )
button2.pack()

button3 = tkinter.Button(win, text="幅度降低", command=f3, )
button3.pack()

button4 = tkinter.Button(win, text="幅度增加", command=f4, )
button4.pack()

button5 = tkinter.Button(win, text="退出", command=win.quit)
button5.pack()
win.mainloop()
