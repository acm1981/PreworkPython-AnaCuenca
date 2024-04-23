# Construir una función salario que, al indicarle el salario por hora,
# el número de horas trabajadas durante una semana por un trabajador, y la
# retención,
# en decimales, calcule y devuelva el salario neto y el salario bruto,
# considerando
# que si el número de horas trabajadas semanalmente es mayor a 45, se consideran
# horas extras y debe pagarse a un 50% más. Por defecto, las horas
#semanales son 40,
# y la retención un 2%.

salario <- function(costehora, horas = 40, retenciones = 0.02) {
  if (horas > 45) {
    horasextras <- horas - 45
    costeextra <- costehora * 1.5
    bruto <- 45 * costehora + horasextras * costeextra
  } else {
    bruto <- horas * costehora
  }
  neto <- bruto * (1 - retenciones)
  return(list("Salario Bruto" = bruto, "Salario Neto" = neto))
}

salario(20)
salario(20,50,0.20)

# Calcular la media de un vector numérico, sumando todos sus elementos y dividiendo
# entre el número de elementos, sin emplear las funciones de R (mean()). Emplee 
# un bucle for

# bucle for
media <- function(x) {
  resultado <- 0
  for (i in 1:length(x)){
    resultado <- resultado + x[i]
  }
  resultado / length(x)
}

# bucle while
media <- function(x) {
  resultado <- 0
  i<-1
  while(i<=length(x)){
    resultado <- resultado + x[i]
    i<-i+1
  }
  resultado / length(x)
}

# vectorizacion de operaciones
media <- function(x) {
  sum(x) / length(x)
}

media(1:11)

# Definir la función con parámetros y un valor por defecto
operacion_matematica <- function(x, y = 2, multiplicar = TRUE) {
  if (multiplicar) {
    resultado <- x * y
  } else {
    resultado <- x + y
  }
  return(resultado)
}

# Llamar a la función sin especificar el parámetro 'y' (utilizará el valor por defecto)
resultado1 <- operacion_matematica(3)
print(resultado1)  # El resultado será 3 * 2 = 6

# Llamar a la función especificando el parámetro 'y'
resultado2 <- operacion_matematica(3, y = 4)
print(resultado2)  # El resultado será 3 * 4 = 12

# Llamar a la función especificando el parámetro 'y' y desactivando la multiplicación
resultado3 <- operacion_matematica(3, y = 4, multiplicar = FALSE)
print(resultado3)  # El resultado será 3 + 4 = 7
