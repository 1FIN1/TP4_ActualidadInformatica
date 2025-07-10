
from behave import *
from app import sumar 
@given('que tengo los números {num1:d} y {num2:d}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('sumo los números')
def step_impl(context):
    context.resultado = sumar(context.num1, context.num2)

@then('el resultado debe ser {esperado:d}')
def step_impl(context, esperado):
    assert context.resultado == esperado