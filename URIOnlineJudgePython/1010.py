a, b, c = input().split(" ")
d, e, f = input().split(" ")


codigoPeca1 = int(a)
numeroDePecas1 = int(b)
valorPeca1 = float(c)

codigoPeca2 = int(d)
numeroDePecas2 = int(e)
valorPeca2 = float(f)

total = (numeroDePecas1 * valorPeca1) + (numeroDePecas2 * valorPeca2)
print("VALOR A PAGAR: R$ {:.2f}".format(total))

