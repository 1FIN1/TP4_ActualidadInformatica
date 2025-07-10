# features/sumar.feature
Feature: Suma de dos números enteros

  Como un usuario de la calculadora  
  Quiero poder sumar dos números enteros  
  Para obtener el resultado correcto

  Scenario: Sumar dos números positivos
    Given que tengo los números 5 y 3
    When sumo los números
    Then el resultado debe ser 8

  Scenario: Sumar un número con cero
    Given que tengo los números 10 y 0
    When sumo los números
    Then el resultado debe ser 10

  Scenario: Sumar un número positivo y uno negativo
    Given que tengo los números 7 y -4
    When sumo los números
    Then el resultado debe ser 3

  Scenario: Sumar dos números negativos
    Given que tengo los números -5 y -2
    When sumo los números
    Then el resultado debe ser -7
