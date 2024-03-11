import pulp

# Створення моделі
model = pulp.LpProblem("Production Optimization", pulp.LpMaximize)

# Визначення змінних рішення
x1 = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  # Кількість одиниць лимонаду
x2 = pulp.LpVariable('Fruit Juice', lowBound=0, cat='Integer')  # Кількість одиниць фруктового соку

# Функція максимізації (кількість продуктів)
model += x1 + x2

# Обмеження на ресурси
# Води: 2x1 + x2 <= 100
model += 2 * x1 + x2 <= 100
# Цукру: x1 <= 50
model += x1 <= 50
# Лимонного соку: x1 <= 30
model += x1 <= 30
# Фруктового пюре: 2x2 <= 40
model += 2 * x2 <= 40

# Вирішення моделі
model.solve()

# Виведення результатів
print("Optimal Production Plan:")
print("Lemonade:", int(pulp.value(x1)))
print("Fruit Juice:", int(pulp.value(x2)))
