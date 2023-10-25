"""
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
"""

# 1
numero=-1

if numero>=0:
    print(f'El numero {numero} es positivo')
else:
    print(f'El número {numero} es negativo')

# 2
numero=25

if numero%2>0:
    print(f'El numero {numero} es impar')
else:
    print(f'El número {numero} es par')

# 3
a=7
b=30
c=-5

if a>b:
    if a>c:
        numero_mayor=a
    else:
        numero_mayor=c
else:
    if b>c:
        numero_mayor=b
    else:
        numero_mayor=c
print(numero_mayor)
