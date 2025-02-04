import matplotlib.pyplot as plt

# Данные
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Построение линейного графика
plt.plot(x, y, label='Линейный график')
plt.xlabel('X-ось')
plt.ylabel('Y-ось')
plt.title('Пример линейного графика')
plt.legend()
plt.show()