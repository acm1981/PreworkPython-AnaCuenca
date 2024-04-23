# Ejercicio 1: Definir una Función sin Parámetros
# Enunciado: Define una función llamada saludo que imprima en la consola el
# mensaje "Hola, bienvenido a R".
saludo <- function(){
  print('Hola, bienvenido a R')
}

saludo()

# Ejercicio 2: Definir una Función con Parámetros y Condicionales
# Enunciado: Crea una función llamada calificar_edad que tome un parámetro
# numérico llamado edad y muestre en la consola si la persona es "menor de
# edad" o "mayor de edad".
calificar_edad <- function(edad){
  if (edad>=18)
    print('Mayor de edad')
  else
    print('Menor de edad')
}

calificar_edad(18)

# Ejercicio 3: Bucle con Operaciones Aritméticas
# Enunciado: Define una función llamada tabla_multiplicar que tome un
# parámetro numérico n e imprima la tabla de multiplicar del 1 al 10 de ese
# número.
tabla_multiplicar <- function(n=0){
  for (i in 0:10)
    print(paste(n,'x',i,'=',n*i))
}
tabla_multiplicar(7)

# Ejercicio 4: Bucle con Condicionales y Operaciones con Vectores
# Enunciado: Crea una función llamada numeros_pares que tome un parámetro
# numérico limite e imprima los números pares hasta ese límite.
numeros_pares <- function(limite){
  if (limite>0){
    numeros_pares <- seq(from=0,to=limite, by=2)
    i<-1
    for(i in 1:length(numeros_pares))
      print(numeros_pares[i])
  }
  else
    print('El número debe ser mayor o igual a cero.')
}
numeros_pares(10)

# Ejercicio 5: Bucle Anidado con Condicionales y Operaciones de Listas
# Enunciado: Define una función llamada matriz_cuadrada que tome un parámetro
# numérico n e imprima una matriz cuadrada de tamaño n x n donde los
# elementos son el resultado de la suma de sus índices de fila y columna
matriz_cuadrada <- function(n){
  for (fila in 1:n){
    lista_suma=list()
    for (columna in 1:n){
      lista_suma[columna] <- fila+columna
    }
    if (fila==1){
      matriz <- matrix(ncol=n)
    }
    matriz <- rbind(matriz,lista_suma)
  }
  matriz <- matriz[-1, , drop=FALSE]
  print(matriz)
}
  
matriz_cuadrada(10)
  
