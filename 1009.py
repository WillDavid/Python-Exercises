nome = input()
salarioFixo = float(input())
vendasEfetuadasMes = float(input())
totalVendasPorMes = vendasEfetuadasMes * 0.15
salarioFinal = totalVendasPorMes + salarioFixo

print("TOTAL = R$ {:.2f}\n".format(salarioFinal))
