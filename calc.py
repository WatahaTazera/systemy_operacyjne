import sys

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

# Sprawdzenie liczby argumentów
if len(sys.argv) != 4:
    print("Użycie: calc.py <liczba_1> <+ lub -> <liczba_2>")
    sys.exit(1)

# Pobranie argumentów
liczba_1 = float(sys.argv[1])
operacja = sys.argv[2]
liczba_2 = float(sys.argv[3])

# Wybór operacji i obliczenie wyniku
if operacja == '+':
    wynik = dodawanie(liczba_1, liczba_2)
elif operacja == '-':
    wynik = odejmowanie(liczba_1, liczba_2)
else:
    print("Nieobsługiwana operacja. Dozwolone operacje to '+' i '-'.")
    sys.exit(1)

# Zapis wyniku do pliku
with open('/tmp/wynik.txt', 'w') as file:
    file.write(str(wynik))

print("Wynik został zapisany do pliku /tmp/wynik.txt.")
