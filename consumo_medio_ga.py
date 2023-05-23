d= float(input("Digite a distância percorrida (km): "))
c = float(input("Digite a quantidade de combustível gasto (litros): "))
p = float(input("Digite o preço da gasolina (litros): "))

consu_m = d / c
gasto_litro = p * 1  # considerando que o usuário informou o preço por litro

print("Consumo médio do veículo: {:.2f} km/l".format(consu_m))
print("Gasto com a gasolina por litro: R$ {:.2f}".format(gasto_litro))

