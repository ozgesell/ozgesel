import argparse
import sys
from . import math_ops, calculus, units, electrical, mechanics, materials


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(prog="engcalc", description="Mühendislik hesap makinesi")
	subparsers = parser.add_subparsers(dest="command", required=True)

	# math
	math_parser = subparsers.add_parser("math", help="Matematiksel işlemler")
	math_sub = math_parser.add_subparsers(dest="math_cmd", required=True)

	lin = math_sub.add_parser("solve-linear", help="ax + b = 0 çöz")
	lin.add_argument("--a", type=float, required=True)
	lin.add_argument("--b", type=float, required=True)

	quad = math_sub.add_parser("solve-quadratic", help="ax^2 + bx + c = 0 çöz")
	quad.add_argument("--a", type=float, required=True)
	quad.add_argument("--b", type=float, required=True)
	quad.add_argument("--c", type=float, required=True)

	cmag = math_sub.add_parser("complex", help="Karmaşık sayı işlemleri")
	cmag.add_argument("--op", choices=["magnitude", "phase"], required=True)
	cmag.add_argument("--real", type=float, required=True)
	cmag.add_argument("--imag", type=float, required=True)

	# calculus
	calc_parser = subparsers.add_parser("calculus", help="Türev ve integral")
	calc_sub = calc_parser.add_subparsers(dest="calc_cmd", required=True)
	cdiff = calc_sub.add_parser("diff", help="Sembolik türev")
	cdiff.add_argument("--expr", type=str, required=True)
	cdiff.add_argument("--var", type=str, required=True)
	cint = calc_sub.add_parser("integrate", help="Sınırsız integral")
	cint.add_argument("--expr", type=str, required=True)
	cint.add_argument("--var", type=str, required=True)

	# units
	units_parser = subparsers.add_parser("units", help="Birim dönüşümleri")
	units_sub = units_parser.add_subparsers(dest="units_cmd", required=True)
	uconv = units_sub.add_parser("convert", help="Birim çevir")
	uconv.add_argument("--category", choices=list(units.CATEGORY_TO_BASE.keys()), required=True)
	uconv.add_argument("--value", type=float, required=True)
	uconv.add_argument("--from", dest="from_unit", type=str, required=True)
	uconv.add_argument("--to", dest="to_unit", type=str, required=True)

	# electrical
	elec_parser = subparsers.add_parser("electrical", help="Elektrik hesapları")
	elec_sub = elec_parser.add_subparsers(dest="elec_cmd", required=True)
	ohm = elec_sub.add_parser("ohm", help="Ohm kanunu")
	ohm.add_argument("--v", type=float)
	ohm.add_argument("--i", type=float)
	ohm.add_argument("--r", type=float)

	series = elec_sub.add_parser("series", help="Seri direnç")
	series.add_argument("--res", type=float, nargs='+', required=True)

	parallel = elec_sub.add_parser("parallel", help="Paralel direnç")
	parallel.add_argument("--res", type=float, nargs='+', required=True)

	power = elec_sub.add_parser("power", help="Güç hesabı")
	power.add_argument("--v", type=float)
	power.add_argument("--i", type=float)
	power.add_argument("--r", type=float)

	# mechanics
	mech_parser = subparsers.add_parser("mechanics", help="Makine/mekanik hesapları")
	mech_sub = mech_parser.add_subparsers(dest="mech_cmd", required=True)
	stress = mech_sub.add_parser("stress", help="Gerilme: sigma=F/A")
	stress.add_argument("--force", type=float, required=True)
	stress.add_argument("--area", type=float, required=True)

	axdef = mech_sub.add_parser("axial-deflection", help="Eksenel uzama: delta=PL/(AE)")
	axdef.add_argument("--force", type=float, required=True)
	axdef.add_argument("--length", type=float, required=True)
	axdef.add_argument("--area", type=float, required=True)
	axdef.add_argument("--E", type=float, required=True, help="Elastisite modülü")

	# materials
	mat_parser = subparsers.add_parser("materials", help="Malzeme hesapları")
	mat_sub = mat_parser.add_subparsers(dest="mat_cmd", required=True)
	sf = mat_sub.add_parser("safety-factor", help="n = allowable / actual")
	sf.add_argument("--allowable", type=float, required=True)
	sf.add_argument("--actual", type=float, required=True)

	strain = mat_sub.add_parser("strain", help="epsilon = deltaL / L")
	strain.add_argument("--deltaL", type=float, required=True)
	strain.add_argument("--L", type=float, required=True)

	return parser


def main(argv: list[str] | None = None) -> int:
	if argv is None:
		argv = sys.argv[1:]
	parser = build_parser()
	args = parser.parse_args(argv)

	if args.command == "math":
		if args.math_cmd == "solve-linear":
			root = math_ops.solve_linear(args.a, args.b)
			print(root)
		elif args.math_cmd == "solve-quadratic":
			roots = math_ops.solve_quadratic(args.a, args.b, args.c)
			print(roots)
		elif args.math_cmd == "complex":
			z = complex(args.real, args.imag)
			if args.op == "magnitude":
				print(math_ops.complex_magnitude(z))
			else:
				print(math_ops.complex_phase_deg(z))

	elif args.command == "calculus":
		if args.calc_cmd == "diff":
			print(calculus.diff_expr(args.expr, args.var))
		else:
			print(calculus.integrate_expr(args.expr, args.var))

	elif args.command == "units":
		if args.units_cmd == "convert":
			print(units.convert(args.category, args.value, args.from_unit, args.to_unit))

	elif args.command == "electrical":
		if args.elec_cmd == "ohm":
			print(electrical.ohm(v=args.v, i=args.i, r=args.r))
		elif args.elec_cmd == "series":
			print(electrical.series_resistance(args.res))
		elif args.elec_cmd == "parallel":
			print(electrical.parallel_resistance(args.res))
		elif args.elec_cmd == "power":
			print(electrical.power(v=args.v, i=args.i, r=args.r))

	elif args.command == "mechanics":
		if args.mech_cmd == "stress":
			print(mechanics.stress(args.force, args.area))
		elif args.mech_cmd == "axial-deflection":
			print(mechanics.axial_deflection(args.force, args.length, args.area, args.E))

	elif args.command == "materials":
		if args.mat_cmd == "safety-factor":
			print(materials.safety_factor(args.allowable, args.actual))
		elif args.mat_cmd == "strain":
			print(materials.strain(args.deltaL, args.L))

	return 0


if __name__ == "__main__":
	sys.exit(main())
