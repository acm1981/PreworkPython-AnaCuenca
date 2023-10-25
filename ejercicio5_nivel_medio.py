# 1. Define una función que utilice un bucle para imprimir los primeros n números de la serie de Fibonacci.
def serie_fibonacci(numero):
    if numero < 1:
        return []

    serie = [1]
    n0 = 0
    n1 = 1
    n = 0

    for i in range(1, numero):
        n = n0 + n1
        serie.append(n)
        n0 = n1
        n1 = n
    return serie


print("*****************")
print("** EJERCICIO 1 **")
print("*****************")
num = int(input("Ingresa el valor de n para generar la serie de Fibonacci: "))
print(serie_fibonacci(num))


# 2. Ejercicio: Define una función que tome un número y retorne una lista de sus divisores.
def lista_divisores(numero):
    lista = []

    for i in range(1, numero + 1):
        if numero % i == 0:
            lista.append(i)
    return lista


print("*****************")
print("** EJERCICIO 2 **")
print("*****************")
num = int(input("Ingresa el número para el que desea conocer sus divisores: "))
print(lista_divisores(num))


# 3. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos únicos de la lista original.
def borra_duplicados_lista(lista):
    if len(lista) < 1:
        return []

    longitud_lista = len(lista)
    i = 0
    j = 0

    while i < longitud_lista:
        elemento_lista = lista[i]
        j = i + 1
        while j < longitud_lista:
            if lista[i] == lista[j]:
                lista.pop(j)
                longitud_lista = len(lista)
            j += 1
        i += 1
    return lista


print("*****************")
print("** EJERCICIO 3 **")
print("*****************")
print(borra_duplicados_lista([1, 1, 2, 0, 3, 1, -7, 5, 0]))


# 4. Ejercicio: Define una función que tome un número y retorne la suma de sus dígitos.
def suma_digitos(numero):
    suma = 0
    for str_numero in str(numero):
        suma += int(str_numero)
    return suma


print("*****************")
print("** EJERCICIO 4 **")
print("*****************")
num = int(input("Ingresa el número para el que desea sumar sus digitos: "))
print(suma_digitos(num))


# 5. Ejercicio: Define una función que tome una cadena y cuente el número de vocales en la cadena.
def cuenta_vocales(cadena):
    lista_vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    numero_vocales = 0
    for letra in cadena:
        for vocal in lista_vocales:
            if letra == vocal:
                numero_vocales += 1

    return numero_vocales


print("*****************")
print("** EJERCICIO 5 **")
print("*****************")
frase = str(input("Escribe una frase para que contemos las vocales: "))
print(cuenta_vocales(frase))


# 6. Ejercicio: Define una función que tome una lista y un número n, y retorne los primeros n elementos de la lista.
def recupera_primeros_n_elementos(lista, n):
    lista_retornar = []
    if n > len(lista):
        n = len(lista)
    for i in range(0, n):
        lista_retornar.append(lista[i])
    return lista_retornar


print("*****************")
print("** EJERCICIO 6 **")
print("*****************")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input("¿Cuantos elementos quiere ver?"))
print(recupera_primeros_n_elementos(lista, n))


# 7. Ejercicio: Define una función que tome una cadena y retorne la cantidad de letras mayúsculas y minúsculas en la cadena.
def cuenta_mayusculas_minusculas(cadena):
    mayusculas = 0
    minusculas = 0
    for letra in cadena:
        if letra.isalpha():
            if letra.isupper():
                mayusculas += 1
            else:
                minusculas += 1
    return mayusculas, minusculas


print("*****************")
print("** EJERCICIO 7 **")
print("*****************")

mayusculas = 0
minusculas = 0

frase = str(
    input("Escribe una frase para que contemos las mayúsculas y las minúsculas: ")
)
mayusculas, minusculas = cuenta_mayusculas_minusculas(frase)
print(f"La frase tiene {mayusculas} mayúsculas y {minusculas} minúsculas")


# 8. Ejercicio: Define una función que tome un número y retorne True si es un número perfecto, False en caso contrario. Un número perfecto es aquel que es
# igual a la suma de sus divisores propios positivos. Por ejemplo, 6 es un número perfecto porque sus divisores son 1, 2 y 3, y 6 = 1 + 2 + 3.
def es_numero_perfecto(numero):
    divisores = lista_divisores(numero)
    divisores.remove(numero)
    suma = 0
    for divisor in divisores:
        suma += divisor
    return suma == numero


print("*****************")
print("** EJERCICIO 8 **")
print("*****************")
numero = int(input("Introduzca un número y vamos a comprobar si es perfecto o no:"))
if numero < 0:
    print("El número tiene que ser positivo")
else:
    if es_numero_perfecto(numero):
        print("El número es perfecto")
    else:
        print("El número no es perfecto")


# 9. Ejercicio: Define una función que reciba un número y retorne su representación en binario.
def convertir_a_binario(numero):
    cadena_binario = ""
    i = numero
    while i > 0:
        resto = i % 2
        cadena_binario = str(resto) + cadena_binario
        i = i // 2
    return cadena_binario


print("*****************")
print("** EJERCICIO 9 **")
print("*****************")
numero = int(input("Introduzca un número y vamos a convertirlo a binario:"))
print(f"El valor binario del número {numero} es {convertir_a_binario(numero)}")


# 10. Ejercicio: Define una función que reciba dos listas y retorne la intersección de ambas (los elementos que están en las dos listas).
def interseccion_listas(lista1, lista2):
    lista_elementos_comunes = []

    for elemento_lista1 in lista1:
        if elemento_lista1 in lista2 and elemento_lista1 not in lista_elementos_comunes:
            lista_elementos_comunes.append(elemento_lista1)

    return lista_elementos_comunes


print("******************")
print("** EJERCICIO 10 **")
print("******************")
lista_primera = [1, 6, 4, 4, 5, 7, 24, 10]
lista_segunda = [4, 0, 5, 65]

print(interseccion_listas(lista_primera, lista_segunda))


# 11. Ejercicio: Define una función que tome una cadena y determine si es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def es_palindromo(cadena):
    cadena_invertida = cadena.lower()[::-1]
    return cadena.lower() == cadena_invertida


print("******************")
print("** EJERCICIO 11 **")
print("******************")
cadena = str(input("Inserta una cadena:"))
if es_palindromo(cadena):
    print("Es palíndromo")
else:
    print("NO es palíndromo")


# 12. Ejercicio: Escribe un programa que imprima los números del 1 al 50, pero para múltiplos de tres imprima “Fizz” en lugar del número y para los múltiplos de
# cinco imprima “Buzz”. Para números que son múltiplos de tanto tres como cinco imprima “FizzBuzz”.
print("******************")
print("** EJERCICIO 12 **")
print("******************")
for numero in range(1, 51):
    divisores = lista_divisores(numero)
    if 3 in divisores and 5 in divisores:
        print("FizzBuzz")
    elif 3 in divisores:
        print("Fizz")
    elif 5 in divisores:
        print("Buzz")
    else:
        print(str(numero))


# 13. Ejercicio: Define una función que tome una lista y retorne la lista ordenada en orden ascendente.
def ordenar_lista(lista):
    lista.sort()
    return lista


def ordenar_lista_manual(lista):
    lista_ordenada = []
    lista_ordenada.append(lista[1])
    lista.pop(1)

    for elemento in lista:
        for i in range(0, len(lista_ordenada)):
            if elemento < lista_ordenada[i]:
                lista_ordenada.insert(i, elemento)
                break
        if elemento not in lista_ordenada:
            lista_ordenada.append(elemento)
    return lista_ordenada


print("******************")
print("** EJERCICIO 13 **")
print("******************")
lista_sin_ordenar = [1, -5, 0, 19, 8, 999, 3]
print(ordenar_lista(lista_sin_ordenar))
print(ordenar_lista_manual(lista_sin_ordenar))


# 14. Ejercicio: Define una función que reciba una lista de palabras y un entero n, y retorne la lista de palabras que son más largas que n.
def palabras_mas_largas_que_n(lispa_palabras, n):
    lista_palabas_mas_largas = []
    for palabra in lispa_palabras:
        if len(palabra) > n:
            lista_palabas_mas_largas.append(palabra)

    return lista_palabas_mas_largas


print("******************")
print("** EJERCICIO 14 **")
print("******************")
lista_palabras = ["fresa", "melocotón", "uva", "platano", "paraguaya"]
numero = int(input("Introduzca la longitud minima de la palabra a buscar:"))

print(palabras_mas_largas_que_n(lista_palabras, numero))

# 15. Ejercicio: Define una función que tome un número y calcule su serie de Fibonacci.
# no entiendo en que se diferencia con el ejercicio 1


# 16. Ejercicio: Define una función que tome una lista de números y retorne el número más grande de la lista.
def numero_maximo_lista(lista_numeros):
    maximo = -9999999999999
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero

    return maximo


print("******************")
print("** EJERCICIO 16 **")
print("******************")
lista_numeros = [-500, 9, -520, 6, 9, 532, 45, 965]
print(max(lista_numeros))
print(numero_maximo_lista(lista_numeros))


# 17. Ejercicio: Define una función que reciba un número y retorne la suma de sus dígitos al cubo.
def suma_digitos_al_cubo(numero):
    return suma_digitos(numero) ** 3


print("******************")
print("** EJERCICIO 17 **")
print("******************")
numero = int(
    input(
        "Introduzca el número para el que desea sumar sus digitos y elevarlo al cubo:"
    )
)
print(suma_digitos_al_cubo(numero))


# 18. Ejercicio: Define una función que reciba una lista de números y retorne el segundo número más grande de la lista.
def segundo_mas_grande(lista):
    lista_ordenada = ordenar_lista_manual(lista)
    longitud = len(lista)
    numero_mayor = lista_ordenada[longitud]

    for numero in reversed(lista_ordenada):
        if numero < numero_mayor:
            return numero

    return numero_mayor


print("******************")
print("** EJERCICIO 18 **")
print("******************")
lista_original = [1, 87, 90, 0, 652, 25, 2]
print(segundo_mas_grande(lista_original))


# 19. Ejercicio: Define una función que tome dos listas y retorne True si tienen al menos un miembro en común, de lo contrario, retorne False.
def algo_en_comun(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False


print("******************")
print("** EJERCICIO 19 **")
print("******************")
lista1 = ["a", "bbb", "3", "27", "manzana"]
lista2 = ["platano", "azul"]

if algo_en_comun(lista1, lista2):
    print("Tienen al menos un elemento en común")
else:
    print("No tienen nada en común")


# 20. Ejercicio: Define una función que tome una lista y retorne una nueva lista con los elementos de la lista original en orden inverso.
def lista_orden_inverso(lista):
    lista_invertida = []
    for elemento in reversed(lista):
        lista_invertida.append(elemento)
    return lista_invertida


print("******************")
print("** EJERCICIO 20 **")
print("******************")
lista_sin_ivertir = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista_orden_inverso(lista_sin_ivertir))


# 21. Ejercicio: Define una función que reciba una cadena y cuente el número de dígitos y letras que contiene.
def cuenta_digitos_y_letras(cadena):
    num_digitos = 0
    num_letras = 0

    for caracter in cadena:
        if caracter.isalpha():
            num_letras += 1
        if caracter.isnumeric():
            num_digitos += 1

    return num_digitos, num_letras


print("******************")
print("** EJERCICIO 21 **")
print("******************")
frase = str(input("Introduzca una frase:"))
digitos, letras = cuenta_digitos_y_letras(frase)
print(f"La frase introducida tiene {digitos} dígitos y {letras} letras.")


# 22. Ejercicio: Define una función que reciba una lista de números y retorne la suma acumulada de los números
def suma_numeros_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero

    return suma


print("******************")
print("** EJERCICIO 22 **")
print("******************")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(suma_numeros_lista(lista))


# 23. Ejercicio: Define una función que encuentre el elemento más común en una lista.
def elemento_mas_comun(lista):
    num_apariciones = 0
    for elemento in lista:
        if lista.count(elemento) > num_apariciones:
            elemento_mas_comun = elemento
            num_apariciones = lista.count(elemento)

    return elemento_mas_comun


print("******************")
print("** EJERCICIO 23 **")
print("******************")
lista_comunes = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 66, 6, 7, 7]
print(elemento_mas_comun(lista_comunes))


# 24. Ejercicio: Define una función que tome un número y retorne un diccionario con la tabla de multiplicar de ese número del 1 al 10.
def tabla_multiplicar(numero):
    multiplicacion = {}

    for i in range(0, 11):
        multiplicacion[i] = i * numero

    return multiplicacion


print("******************")
print("** EJERCICIO 24 **")
print("******************")
print(tabla_multiplicar(5))


# 25. Ejercicio: Define una función que tome una cadena y retorne un diccionario con la cantidad de apariciones de cada caracter en la cadena.
def apariciones(cadena):
    dic_caracteres = {}

    for caracter in cadena:
        dic_caracteres[caracter] = cadena.count(caracter)

    return dic_caracteres


print("******************")
print("** EJERCICIO 25 **")
print("******************")
frase = str(input("Introduzca una frase:"))
print(apariciones(frase))


# 26. Ejercicio: Define una función que tome dos listas y retorne la lista de elementos que no están en ambas listas.
def elementos_no_comunes_listas(lista1, lista2):
    lista_elementos_no_comunes = []

    for elemento_lista1 in lista1:
        if (
            elemento_lista1 not in lista2
            and elemento_lista1 not in lista_elementos_no_comunes
        ):
            lista_elementos_no_comunes.append(elemento_lista1)
    for elemento_lista2 in lista2:
        if (
            elemento_lista2 not in lista1
            and elemento_lista2 not in lista_elementos_no_comunes
        ):
            lista_elementos_no_comunes.append(elemento_lista2)

    return lista_elementos_no_comunes


print("******************")
print("** EJERCICIO 26 **")
print("******************")
lista_primera = [1, 6, 4, 4, 5, 7, 24, 10]
lista_segunda = [4, 0, 5, 65]

print(elementos_no_comunes_listas(lista_primera, lista_segunda))


# 27. Ejercicio: Define una función que tome una lista y retorne la lista sin duplicados.
def quitar_duplicados_lista(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)

    return lista_sin_duplicados


print("******************")
print("** EJERCICIO 27 **")
print("******************")
lista_duplicados = [1, 6, 4, 4, 5, 7, 24, 10, 1, 6]
print(quitar_duplicados_lista(lista_duplicados))


# 28. Ejercicio: Define una función que reciba un número entero positivo y retorne la suma de los cuadrados de todos los números pares menores o iguales a ese número.
def suma_cuadros_pares_menores(numero):
    if numero < 0:
        raise "El número debe ser positivo"
    suma = 0
    i = 2
    while i < numero:
        if i % 2 == 0:
            suma += i**2
        i += 1
    return suma


print("******************")
print("** EJERCICIO 28 **")
print("******************")
numero = int(input("Introduzca una número entero positivo:"))
print(suma_cuadros_pares_menores(numero))


# 29. Ejercicio: Define una función que reciba una lista de números y retorne el promedio de los números en la lista.
def promedio(lista_enteros):
    suma = 0.0
    if len(lista_enteros) == 0:
        raise "La lista está vacía"
    for numero in lista_enteros:
        suma += numero
    print(len(lista_enteros))
    return suma / len(lista_enteros)


print("******************")
print("** EJERCICIO 29 **")
print("******************")
lista_numeros = [2, 0, 8, 15, 78]
print(promedio(lista_numeros))


# 30. Ejercicio: Define una función que reciba una lista de cadenas y retorne la cadena más larga en la lista.
def cadena_mas_larga(lista_cadenas):
    cadena_larga = ""
    for cadena in lista_cadenas:
        if len(cadena) > len(cadena_larga):
            cadena_larga = cadena

    return cadena_larga


print("******************")
print("** EJERCICIO 30 **")
print("******************")
lista_de_cadenas = [
    "el perro",
    "el gato blanco",
    "el oso polar",
    "la vaca lola",
    "el escorpión venenoso",
]
print(cadena_mas_larga(lista_de_cadenas))


# 31. Ejercicio: Define una función que reciba un número entero n y retorne una lista con los n primeros números primos.
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True


def n_primeros_numeros_primos(n):
    if n < 0:
        raise "El número debe de ser positivo"
    lista = []
    i = 0
    while i <= n:
        if es_primo(i):
            lista.append(i)
        i += 1
    return lista


print("******************")
print("** EJERCICIO 31 **")
print("******************")
numero = int(input("Introduzca una número entero positivo:"))
print(n_primeros_numeros_primos(numero))


# 32. Ejercicio: Define una función que reciba una cadena y retorne la misma cadena pero con las palabras en orden inverso.
def palabras_orden_inverso(cadena):
    lista_palabras = cadena.split(" ")
    cadena_al_reves = ""
    for palabra in reversed(lista_palabras):
        cadena_al_reves += palabra + " "
    return cadena_al_reves.strip()


print("******************")
print("** EJERCICIO 32 **")
print("******************")
texto = str(input("Introduzca un texto:"))
print(palabras_orden_inverso(texto))


# 33. Ejercicio: Escribe una función que reciba una lista de tuplas y retorne una lista ordenada basada en el último elemento de cada tupla.
def ordena_lista_tuplas(lista_tuplas, pos_elemento_ordenar):
    lista_ordenada = []

    i = 1
    while len(lista_tuplas) > 0:
        tupla1 = lista_tuplas[0]
        for tupla in lista_tuplas:
            if tupla[pos_elemento_ordenar] < tupla1[pos_elemento_ordenar]:
                tupla1 = tupla

        i = lista_tuplas.index(tupla1)
        lista_ordenada.append(tupla1)
        lista_tuplas.pop(i)

    return lista_ordenada


print("******************")
print("** EJERCICIO 33 **")
print("******************")
lista_tuplas_sin_ordenar = []
alumno1 = ("Ana", 5)
alumno2 = ("Carlos", 8)
alumno3 = ("Cristina", 2)
lista_tuplas_sin_ordenar.append(alumno1)
lista_tuplas_sin_ordenar.append(alumno2)
lista_tuplas_sin_ordenar.append(alumno3)
print(ordena_lista_tuplas(lista_tuplas_sin_ordenar, 1))


# 34. Ejercicio: Define una función que reciba una cadena y retorne la cantidad de letras vocales en la cadena.
def numero_vocales(cadena):
    vocales = ["a", "e", "i", "o", "u"]
    numero_vocales = 0
    for letra in cadena:
        if letra.isalpha() and letra.lower() in vocales:
            numero_vocales += 1
    return numero_vocales


print("******************")
print("** EJERCICIO 34 **")
print("******************")
texto = str(input("Introduzca un texto:"))
print(f"El texto tiene {numero_vocales(texto)} vocales")


# 35. Ejercicio: Define una función que reciba un número entero y retorne True si es un número primo, de lo contrario retorne False.
def es_primo(numero):
    if numero <= 1:
        raise "Tiene que ser un número entero"
    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True


print("******************")
print("** EJERCICIO 35 **")
print("******************")
num = int(input("Ingresa un número: "))
if es_primo(num):
    print("Es un número primo.")
else:
    print("No es un número primo.")
