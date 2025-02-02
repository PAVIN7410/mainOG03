def area_circle(r):
    s = 3.14 * r ** 2
    return s

radius = float(input("Введи радиус: "))
s = area_circle(radius)
print(f"Площадь круга = {s}")


def area_square_area(a):
    S_s = a ** 2
    return S_s

a = float(input("Введи сторону квадрата: "))

S_s = area_square_area(a)
print(f"Площадь квадрата = {S_s}")
