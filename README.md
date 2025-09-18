# Mühendislik Hesap Makinesi (engcalc)

Python tabanlı CLI mühendislik hesap makinesi.

## Kurulum

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Kullanım

Genel yardım:
```bash
python -m engcalc --help
```

Örnekler:
- Doğrusal denklem çöz (ax + b = 0):
```bash
python -m engcalc math solve-linear --a 2 --b -8
```
- İkinci dereceden denklem çöz (ax^2+bx+c=0):
```bash
python -m engcalc math solve-quadratic --a 1 --b -3 --c -4
```
- Türev/İntegral:
```bash
python -m engcalc calculus diff --expr "sin(x)*x^2" --var x
python -m engcalc calculus integrate --expr "x**2" --var x
```
- Birim dönüşümü (basit):
```bash
python -m engcalc units convert --category length --value 2 --from m --to ft
```
- Elektrik (Ohm kanunu):
```bash
python -m engcalc electrical ohm --v 12 --r 6
```
- Mekanik (gerilme):
```bash
python -m engcalc mechanics stress --force 10000 --area 0.005
```
- Malzeme (emniyet katsayısı):
```bash
python -m engcalc materials safety-factor --allowable 250e6 --actual 120e6
```

## Lisans
MIT
