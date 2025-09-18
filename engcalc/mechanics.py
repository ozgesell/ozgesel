
def stress(force: float, area: float) -> float:
	if area == 0:
		raise ValueError("Area cannot be zero")
	return force / area


def axial_deflection(force: float, length: float, area: float, E: float) -> float:
	if area == 0 or E == 0:
		raise ValueError("Area and E must be non-zero")
	return (force * length) / (area * E)
