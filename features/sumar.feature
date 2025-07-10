# features/sumar.feature
Característica: Suma de dos números enteros

  Como un usuario de la calculadora
  Quiero poder sumar dos números enteros
  Para obtener el resultado correcto

  Escenario: Sumar dos números positivos
    Dado que tengo los números 5 y 3
    Cuando sumo los números
    Entonces el resultado debe ser 8

  Escenario: Sumar un número con cero
    Dado que tengo los números 10 y 0
    Cuando sumo los números
    Entonces el resultado debe ser 10

  Escenario: Sumar un número positivo y uno negativo
    Dado que tengo los números 7 y -4
    Cuando sumo los números
    Entonces el resultado debe ser 3

  Escenario: Sumar dos números negativos
    Dado que tengo los números -5 y -2
    Cuando sumo los números
    Entonces el resultado debe ser -7