import matplotlib as plt
import sympy
import math

'''Ecuacion 2:
 y' senx= y Ln y'''

def ecuacion2():
#Defino las incógnitas:
    x = sympy.symbols('x')
    y = sympy.Function('y')

    #Defino la función:
    f = (y(x).diff(x))*math.sin(x) - (y(x)*math.log(y(x), math.e))
    print(f)
    sympy.Eq(y(x).diff(x), f)

    #Condicion inicial:
    ics = {y(math.py()/2): math.e}

    #resolver la ecuacion:
    sol = sympy.dsolve(f)
    print("-------------------------SOLUCIÓN--------------------------")
    print(sol)

ecuacion2()