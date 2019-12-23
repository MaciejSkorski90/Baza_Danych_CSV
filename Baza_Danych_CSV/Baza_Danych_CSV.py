#-------------------------------------------------------------------------------
# Name:        Baza_Danych_CSV
# Purpose:
#
# Author:      Maciej Skórski
#
# Created:     23-12-2019
# Copyright:   Maciej Skórski 2019
# Licence:     -
#-------------------------------------------------------------------------------

import csv

punkty = []

def srednia(lista):
    return (sum(lista) / len(lista))

with open("punkty_2019.csv", "r") as plikCSV:
    czytnikCSV = csv.reader(plikCSV, delimiter = ";")
    for wiersz in czytnikCSV:
        print(wiersz[0] + " " + wiersz[1])
        punkty.append(int(wiersz[1]))

print("Maksymalna liczba punktow wynosila: ", max(punkty),)
print("Minimalna liczba punktow wynosila: ", min(punkty))
print("Srednia liczba punktow wynosila: ", round(srednia(punkty)))