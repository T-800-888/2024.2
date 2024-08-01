#Leia do teclado a temperatura em Celsius e imprima o equivalente em Fahrenheit.
#Fórmula: (X °C × 9/5) + 32

celcius = float(input("Digite a temperatura em Celcius para obter a conversão: "))
fahr = (celcius * (9/5)) + 32

print(celcius," Celcius = ",fahr," Faharenheit")
