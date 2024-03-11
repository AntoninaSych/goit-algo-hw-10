import numpy as np
import scipy.integrate as spi

# Визначення функції, яку потрібно інтегрувати
def f(x):
    return x ** 2

# Визначення меж інтегрування
a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла за допомогою методу Монте-Карло
def monte_carlo_integration(f, a, b, num_points=100000):
    random_x = np.random.uniform(a, b, num_points)
    random_y = np.random.uniform(0, f(b), num_points)
    area_rectangle = (b - a) * f(b)
    count_points_under_curve = np.sum(random_y < f(random_x))
    ratio_points_under_curve = count_points_under_curve / num_points
    integral_approximation = area_rectangle * ratio_points_under_curve
    return integral_approximation

monte_carlo_result = monte_carlo_integration(f, a, b)

# Обчислення інтеграла за допомогою функції quad з бібліотеки SciPy
quad_result, _ = spi.quad(f, a, b)

# Виведення результатів
print("Результат методом Монте-Карло:", monte_carlo_result)
print("Результат за допомогою функції quad:", quad_result)
