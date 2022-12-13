import numpy as np
import matplotlib.pyplot as plt

n = 150
b = 2

x1 = np.random.random(n)
x2 = x1 + [np.random.randint(100)/15 for i in range(n)] + b
c1 = [x1, x2]

x1 = np.random.random(n)
x2 = x1 - [np.random.randint(100)/23 for i in range(n)] - 0.5 + b
c2 = [x1, x2]

# x = np.array([0+b, 2+b])


f = [-0.25+b, 0.75+b] 

def re():
    # Создаём экземпляр класса figure и добавляем к Figure область Axes
    fig, ax = plt.subplots()
    # Добавим заголовок графика
    ax.set_title('График функции')
    # Название оси X:
    ax.set_xlabel('x')
    # Название оси Y:
    ax.set_ylabel('y')
    # Начало и конец изменения значения X, разбитое на 100 точек
    x = np.linspace(-5, 5, 100) # X от -5 до 5
    # Построение прямой
    y = x**2
    # Вывод графика
    ax.plot(x, y)
    plt.show()


w2 = 1
w3 = -b*w2
w = np.array([-w2, w2, w3])
for i in range(n):
    x = np.array([c1[0][i], c1[1][i], 10])
    y = np.dot(w, x)
    if y >= 0:
        print("Klass1")
    else:
        print("Klass2")


plt.scatter(c1[0][:], c1[1][:], s=10, c="green")
plt.scatter(c2[0][:], c2[1][:], s=10, c="red")
plt.plot(f)
plt.grid(True)
plt.show()