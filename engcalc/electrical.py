from typing import List, Optional


def ohm(v: Optional[float] = None, i: Optional[float] = None, r: Optional[float] = None):
	provided = [(v is not None), (i is not None), (r is not None)]
	if sum(provided) != 2:
		raise ValueError("Provide exactly two of v, i, r")
	if v is None:
		return {"v": i * r}
	if i is None:
		return {"i": v / r}
	return {"r": v / i}


def series_resistance(resistances: List[float]) -> float:
	return float(sum(resistances))


def parallel_resistance(resistances: List[float]) -> float:
	inv = 0.0
	for r in resistances:
		if r == 0:
			raise ValueError("Resistance cannot be zero in parallel")
		inv += 1.0 / r
	return 1.0 / inv


def power(v: float = None, i: float = None, r: float = None):
	if v is not None and i is not None:
		return {"p": v * i}
	if v is not None and r is not None:
		return {"p": v * v / r}
	if i is not None and r is not None:
		return {"p": (i * i) * r}
	raise ValueError("Provide (v,i) or (v,r) or (i,r)")
