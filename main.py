from sympy import symbols
a, b, h, x = symbols('a b h x')

rango = int(input("Ingrese el numero en dividir la funcion"))

# print("h =", latex(expresion_h))

# a_valor = 0
# b_valor = 1

# h_valor = expresion_h.subs({a: a_valor, b: b_valor})

expresion = "h/2*(f(a)+2*(f(a + h)) "
expresion_list = list(expresion)

for n in range(2, rango):
    formula_part = f" + 2*(f(a + {n} * h))"
    # print(formula_part)
    expresion_list.append(formula_part)
    n = n + 1

expresion_list.append("+ f(b))")
formula_completa = "".join(expresion_list)
print(formula_completa)

# print(f"Cuando a={a_valor} y b={b_valor}, entonces h = {h_valor}")
