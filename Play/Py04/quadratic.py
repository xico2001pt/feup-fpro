"""
Define a function solver(a, b, c) that returns the solution to the quadratic formula of the type: ax²+bx+c=0. Return the result in the form of a list: empty list if no solution exists in ℝ, a list with one or two elements if one or two solutions exist, respectively; if there are two solutions, use ascending order.

"""

def solver(a, b, c):
    solution = []
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        pass
    elif delta == 0:
        x1 = -b / (2 * a)
        solution.append(x1)
    else:
        x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        solution.append(min(x1, x2))
        solution.append(max(x1, x2))
    return solution