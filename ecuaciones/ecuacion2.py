from cmath import e, sin
import matplotlib as plt
import sympy
import math

'''Ecuacion 2:
 y' senx= y Ln y'''

def ecuacion1():
#Defino las incógnitas:
    x = sympy.symbols('x')
    y = sympy.Function('y')

    #Defino la función:
    f = (y(x).diff(x))*sin(x) - (y(x)*math.log(y(x), e))
    print(f)
    sympy.Eq(y(x).diff(x), f)

    #Condicion inicial:
    ics = {y(math.py()/2): e}

    #resolver la ecuacion:
    sol = sympy.dsolve(f)
    print("-------------------------SOLUCIÓN--------------------------")
    print(sol)