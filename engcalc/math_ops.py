import cmath
import math
from typing import Tuple


def solve_linear(a: float, b: float) -> float:
	if a == 0:
		raise ValueError("a = 0, not a linear equation")
	return -b / a


def solve_quadratic(a: float, b: float, c: float) -> Tuple[complex, complex]:
	if a == 0:
		root = solve_linear(b, c)
		return (complex(root, 0.0), complex(root, 0.0))
	delta = b * b - 4.0 * a * c
	sqrt_delta = cmath.sqrt(delta)
	root1 = (-b + sqrt_delta) / (2.0 * a)
	root2 = (-b - sqrt_delta) / (2.0 * a)
	return (root1, root2)


def complex_magnitude(z: complex) -> float:
	return abs(z)


def complex_phase_deg(z: complex) -> float:
	return math.degrees(cmath.phase(z))
