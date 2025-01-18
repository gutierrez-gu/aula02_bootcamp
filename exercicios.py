# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_01 = int(input("Digite o primeiro número: "))
# numero_02 = int(input("Digite o segundo número: "))
# resultado = print(numero_01//numero_02)


#10. Escreva um programa que calcule a área do circulo, recebendo o raio como entrada.
import math
raio_circulo = float(input("Digite o raio do circulo: "))
area_do_circulo = math.pi*raio_circulo**2

print(f"{area_do_circulo:.2f}")