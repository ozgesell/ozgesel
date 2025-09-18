from sympy import symbols, sympify, diff, integrate


def diff_expr(expr: str, var: str) -> str:
	v = symbols(var)
	return str(diff(sympify(expr), v))


def integrate_expr(expr: str, var: str) -> str:
	v = symbols(var)
	return str(integrate(sympify(expr), v))
