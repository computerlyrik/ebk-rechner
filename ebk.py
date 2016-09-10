#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--wert", help="Wiederbeschaffungswert", type=int)
parser.add_argument("--alter", help="Gebrauchsjahre", type=int)
parser.add_argument("--lebensdauer", help="Lebensdauer", type=int)

args = parser.parse_args()

if args.wert:
	wiederbeschaffungswert = args.wert
else:
	wiederbeschaffungswert = 8000

if args.alter:
	jahre_gebrauch = args.alter
else:
	jahre_gebrauch = 11

if args.lebensdauer:
	max_lebensdauer = args.lebensdauer
else:
	max_lebensdauer = 25

factor_verlust_1_jahr = 0.24
factor_verlust_n_jahr = (1-factor_verlust_1_jahr)/(max_lebensdauer-1)
verlust_1_jahr = wiederbeschaffungswert * factor_verlust_1_jahr
verlust_n_jahr = wiederbeschaffungswert * factor_verlust_n_jahr
verlust_gebrauchsjahre = verlust_n_jahr * (jahre_gebrauch-1)

restwert = (wiederbeschaffungswert - verlust_1_jahr - verlust_gebrauchsjahre)*(max_lebensdauer-jahre_gebrauch)/(max_lebensdauer-1)

print('Berechnung des Restwertes der EBK')
print('Wiederbeschaffungswert:', wiederbeschaffungswert)
print('Verlust im 1. Jahr:', verlust_1_jahr)
print('Verlust in Folgejahren:', verlust_gebrauchsjahre)


print('Restwert der EBK:',restwert)

