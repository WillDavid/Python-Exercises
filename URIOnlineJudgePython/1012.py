a, b, c = input().split(" ")

a = float(a)
b = float(b)
c = float(c)

pi = 3.14159
areaTriangulo = (a*c)/2
areaCirculo = (pi*(c**2))
areaTrapezio = ((a+b)/2)*c
areaQuadrado = b**2
areaRetangulo = (a*b)


print("TRIANGULO: {:.3f}".format(areaTriangulo))
print("CIRCULO: {:.3f}".format(areaCirculo))
print("TRAPEZIO: {:.3f}".format(areaTrapezio))
print("QUADRADO: {:.3f}".format(areaQuadrado))
print("RETANGULO: {:.3f}".format(areaRetangulo))
