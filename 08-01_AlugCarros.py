#Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por um cliente de uma locadora de carros.
#Sabe-se que: O valor de locação de cada carro é 100,00 reais; O cliente pode locar um único carro por vários dias.

quant_carros = int(input("Sabendo que o valor de aluguel de cada carro é de R$100.00 por dia, quantos carros gostaria de alugar? "))
dias = int(input("Por quantos dias gostaria de alugar? "))

valor=(quant_carros*100) * dias

print("O valor total do aluguel é: R$", valor)
