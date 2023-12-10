from sympy import Symbol, symbols, solve


def solve_for_x():
    x, y = symbols('x,y')
    equation = x + 2*y - 5
    solution = solve(equation, x)
    print(solution)


def show_equation():
    x = Symbol('x')
    print(x + x + 1)


def tests():
    solve_for_x()
