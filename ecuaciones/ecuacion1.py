
import sympy


'''Ecuacion 1:
 dy/dx = (x^2y-y)/(y+1)'''

def ecuacion1():
#Defino las incógnitas:
    x = sympy.symbols('x')
    y = sympy.Function('y')

    #Defino la función:
    f = y(x).diff(x) - ((x**2)*y(x) - y(x))/(y(x)+1)
    print(f)
    sympy.Eq(y(x).diff(x), f)

    #Condicion inicial:
    ics = {y(3): -1}

    #resolver la ecuacion:
    solgen = sympy.dsolve(f)
    f2 = sympy.Eq(solgen.lhs.subs(x, 0).subs(ics), solgen.rhs.subs(x, 0))
    sol = sympy.solve(f2)
    print("-------------------------SOLUCIÓN--------------------------")
    print(sol)