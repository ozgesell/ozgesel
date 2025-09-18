from typing import Dict

# Simple base-unit maps per category
CATEGORY_TO_BASE = {
	"length": "m",
	"mass": "kg",
	"force": "N",
	"pressure": "Pa",
	"energy": "J",
}

_LENGTH_TO_M = {
	"m": 1.0,
	"cm": 0.01,
	"mm": 0.001,
	"km": 1000.0,
	"in": 0.0254,
	"ft": 0.3048,
}

_MASS_TO_KG = {
	"kg": 1.0,
	"g": 0.001,
	"lb": 0.45359237,
}

_FORCE_TO_N = {
	"N": 1.0,
	"kN": 1000.0,
	"lbf": 4.4482216152605,
}

_PRESSURE_TO_PA = {
	"Pa": 1.0,
	"kPa": 1000.0,
	"MPa": 1_000_000.0,
	"bar": 100000.0,
	"psi": 6894.757293168,
}

_ENERGY_TO_J = {
	"J": 1.0,
	"kJ": 1000.0,
	"MJ": 1_000_000.0,
	"Wh": 3600.0,
	"kWh": 3_600_000.0,
}


def _convert_generic(value: float, from_unit: str, to_unit: str, table: Dict[str, float]) -> float:
	if from_unit not in table or to_unit not in table:
		raise ValueError("Unsupported unit")
	base = value * table[from_unit]
	return base / table[to_unit]


def convert(category: str, value: float, from_unit: str, to_unit: str) -> float:
	if category == "length":
		return _convert_generic(value, from_unit, to_unit, _LENGTH_TO_M)
	if category == "mass":
		return _convert_generic(value, from_unit, to_unit, _MASS_TO_KG)
	if category == "force":
		return _convert_generic(value, from_unit, to_unit, _FORCE_TO_N)
	if category == "pressure":
		return _convert_generic(value, from_unit, to_unit, _PRESSURE_TO_PA)
	if category == "energy":
		return _convert_generic(value, from_unit, to_unit, _ENERGY_TO_J)
	raise ValueError("Unknown category")
