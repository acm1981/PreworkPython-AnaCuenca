"""
1. Ejercicio: Define una función que tome dos números y retorne su suma.
2. Ejercicio: Defineuna función que tome un número y retorne su factorial.
3. Ejercicio: Define una función que tome un número y determine si es primo.
4. Ejercicio: Define una función que reciba una lista de números y retorne la suma
de ellos.
5. Ejercicio: Define una función que reciba una cadena de texto y retorne la
cadena en reversa.
"""

# 1
def suma(a,b):
  return a+b

print(suma(5,7))

# 2
def factorial(a):
  i=1
  a_factorial=1
  while i<=a:
    a_factorial*=i
    i+=1

  return a_factorial

print(factorial(5))
print(factorial(50))

# 3
def Es_primo(a):
  i=a-1
  if i<1:
    return False
  while i>1:
    if a%i==0:
      return False
    i-=1
  return True

i=10
while i>0:
  print(f"El número {i} es primo ")
  print(Es_primo(i))
  i-=1

# 4
def suma_lista(lista):
  suma=0
  for numero in lista:
    suma+=numero
  
  return suma

lista_numeros = [1,2,3,4,6,4,44,76,4]
print(suma_lista(lista_numeros))
  
# 5
def cadena_inversa(cadena):  
  longitud=len(cadena) 
  cadena_invertida=""
  while longitud>0:
    cadena_invertida+=cadena[longitud-1]
    cadena=cadena[0:longitud-1]
    longitud=len(cadena) 
  return cadena_invertida
      
print(cadena_inversa('Hola Mundo'))