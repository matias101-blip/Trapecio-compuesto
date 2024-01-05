from sympy import *

x, a, b, h = symbols('x a b h')

n = 6

a_valor = 0
b_valor = 1

h_valor = (b_valor - a_valor) / n

f_x = x**2
Expresion = [f"h/2*( {f_x.subs(x, a)}"]

# 2 / h * (f(a) + 2*(f(a + h)) + 2(f(a + 2 * h)) + ... + f(b))
for i in range(1, n):
    part = f_x.subs(x, a + i *h)
    Expresion_str = f"2 * {part}"
    Expresion.append(Expresion_str)
    print(Expresion)

Expresion = " + ".join(Expresion)
Expresion = list(Expresion)
Expresion = Expresion + [" + ", str(f_x.subs(x, b)), ")"]
Expresion = "".join(Expresion)

Formula = sympify(Expresion)

integral = Formula.subs({a: a_valor, b: b_valor, h: h_valor})

print(integral)
