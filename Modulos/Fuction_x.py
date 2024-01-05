from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy import *

x, a, b, h = symbols('x a b h')

def Trapecio(a_valor, b_valor, n_valor, fx_valor):
    #import pdb; pdb.set_trace()

    if "²" in fx_valor:
        fx_valor = fx_valor.replace("²", "**2")

    h_valor= (b_valor - a_valor) / n_valor
    transformations = (standard_transformations +
        (implicit_multiplication_application,))
    f_x_valor = parse_expr(fx_valor, transformations=transformations)

    f_x = sympify(f_x_valor)

    base = h/2 * (f_x.subs(x, a_valor) + f_x.subs(x, b_valor))
    intermedio = f_x.subs(x, a + h)

    for i in range(2, n_valor):
        intermedio += f_x.subs(x, a + i * h)

    funcion = base + h * intermedio

    result_expre = funcion.subs({a: a_valor, b: b_valor, h: h_valor})

    result = result_expre.evalf()

    return result
