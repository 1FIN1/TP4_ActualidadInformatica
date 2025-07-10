
def cuadrado(numero):
    return numero * numero


def sumar(a, b):
    return a + b


from app import sumar, cuadrado 

def cuadrado_binomio(a, b):
    # (a + b)² = a² + 2*a*b + b²
    return sumar(cuadrado(a), sumar(2 * a * b, cuadrado(b)))