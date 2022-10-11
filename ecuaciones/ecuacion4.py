import sympy

'''Ecuacion 4:
 2t(dy/dt) - y = 3t^2'''

def ecuacion4():
#Defino las incógnitas:
    t = sympy.symbols('t')
    y = sympy.Function('y')

    #Defino la función:
    f = 2*t*(y(t).diff(t)) - y(t) - 3*t**2
    print(f)
    sympy.Eq(y(t).diff(t), f)

    #resolver la ecuacion:
    sol = sympy.dsolve(f)
    print("-------------------------SOLUCIÓN--------------------------")
    print(sol)


ecuacion4()