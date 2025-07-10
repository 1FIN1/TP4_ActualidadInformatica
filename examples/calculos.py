def suma(a, b):
    """ Función que realiza una suma 
        de dos argumentos

    Args:
        a (int/float): argumento a
        b (int/float): argumento b

    Returns:
        int/float: resultado de la suma
    """
    try:
        num_a = int(a)
        num_b = int(b)
        return num_a + num_b
    except (TypeError, ValueError):
        return None


def cuadrado(n):
    """ Función que calcula el cuadrado 
        de un número

    Args:
        n (int/float): número a elevar

    Returns:
        int/float: n elevado al cuadrado
    """
    try:
        num = int(n)
        return num * num
    except (TypeError, ValueError):
        return None


def cuadrado_binomio(a, b):
    """ Función que calcula el cuadrado del binomio (a + b)^2

    Args:
        a (int/float): primer término
        b (int/float): segundo término

    Returns:
        int/float: resultado del cuadrado del binomio
    """
    try:
        num_a = int(a)
        num_b = int(b)
        return cuadrado(num_a) + 2 * num_a * num_b + cuadrado(num_b)
    except (TypeError, ValueError):
        return None
