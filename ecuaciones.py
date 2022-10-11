import matplotlib as plt
import sympy

'''Ecuacion 1:
 dy/dx = (x^2y-y)/(y+1)'''

#Defino las incógnitas:
x = sympy.symbols('x')
y = sympy.Function('y')

#Defino la función:
f = (x**2*y-y)/(y+1)
sympy.Eq(y(x).diff(x), f)