import math

a, b, c = map(float, input('Введите сторону a,b и угол между ними в градусах: ').split())
print((a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(c))) ** 0.5)