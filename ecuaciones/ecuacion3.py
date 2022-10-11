import sympy

'''Ecuacion 3:
 dy/dx -y/(x-2) = 2(x-2)^2'''

def ecuacion3():
#Defino las incógnitas:
    x = sympy.symbols('x')
    y = sympy.Function('y')

    #Defino la función:
    f = y(x).diff(x) - y(x)/(x-2) - 2*(x-2)**2
    print(f)
    sympy.Eq(y(x).diff(x), f)
    
     #resolver la ecuacion:
    sol = sympy.dsolve(f)
    print("-------------------------SOLUCIÓN--------------------------")
    print(sol)