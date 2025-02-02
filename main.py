def area_circle(r):
    s = 3.14 * r ** 2
    return s

radius = float(input("Введи радиус: "))
s = area_circle(radius)
print(f"Площадь круга = {s}")