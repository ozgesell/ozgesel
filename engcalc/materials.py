
def safety_factor(allowable: float, actual: float) -> float:
	if actual == 0:
		raise ValueError("Actual stress cannot be zero")
	return allowable / actual


def strain(deltaL: float, L: float) -> float:
	if L == 0:
		raise ValueError("Original length cannot be zero")
	return deltaL / L
