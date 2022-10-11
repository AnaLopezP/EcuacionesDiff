import matplotlib as plt
import sympy

'''Ecuacion 2:
 y' senx= y Ln y'''

def ecuacion2():
#Defino las incógnitas:
    x = sympy.symbols('x')
    y = sympy.Function('y')

    #Defino la función:
    f = (y(x).diff(x))*sympy.sin(x) - (y(x)*sympy.log(y(x), sympy.e))
    print(f)
    sympy.Eq(y(x).diff(x), f)

    #Condicion inicial:
    ics = {y(sympy.py()/2): sympy.e}

    #resolver la ecuacion:
    sol = sympy.dsolve(f)
    print("-------------------------SOLUCIÓN--------------------------")
    print(sol)

ecuacion2()