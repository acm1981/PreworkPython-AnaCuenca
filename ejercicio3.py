"""
1. Ejercicio: Imprime los números del 1 al 10 usando un bucle for .
2. Ejercicio: Imprime los números pares del 1 al 20 usando un bucle while .
3. Ejercicio: Usa un bucle para calcular la suma de los números del 1 al 100.
"""

# 1
numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
  print(numero)

# 2
numero_par =20
while numero_par>=0:
  print(numero_par)
  numero_par -= 2

# 3
i=0
suma=0

while i<=100:
  suma+=i
  i+=1

print(suma)