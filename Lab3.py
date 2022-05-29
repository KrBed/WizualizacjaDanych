import ciagi
# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
# A = {1-x: x∈<1,10>}
import random

a = [x - 1 for x in range(1, 10)]
print(a)
# B = {1,4,16,...,4 do 7}
b = [4 ** x for x in range(0, 8)]
print(b)
# C = {x: x∈B i x jest liczbą podzielną przez 2}
c = {x for x in b if x % 2 == 0}
print(c)

# Zad2
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując Python
# Comprehension zdefiniuj nową listę, która będzie zawierała tylko parzyste elementy
a = random.randint(1, 1000)
print(a)
lista1 = [random.randint(1, 1000) for i in range(10)]
listOdd = [i for i in lista1 if i % 2 == 0]

print('lista:', lista1)
print('lista elementy parzyste:', listOdd)

# Zad3
# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu a wartość
# - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python Comprehension dozdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.
products = {'chleb': 'szt', 'bułki': 'szt', 'pomidory': 'kg', 'cukier': 'kg'}
sztuki = {key: value for key, value in products.items() if value == 'szt'}
print(sztuki)


# Zad4
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.
def check_triangle(a, b, c):
    if a * a + b * b == c * c:
        print('Trójkąt jest prostokątny')
    else:
        print('Trójkąt nie jest prostokątny')


check_triangle(2, 4, 7)


# Zad5
# Zdefiniuj funkcje która policzy pole trapezu. Funkcja ma przyjmować wartości domyślne.
def trapez_field(a=2, b=4, h=2):
    pole = (a + b) * (h / 2)
    print(pole)


trapez_field(10, 10, 5)


# Zad6.
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa), b (wielkość o ile mnożone są kolejne elementy), ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10
def iloczyn(a=1, b=4, ile=10):
    for i in range(ile):
        print(a)
        a = a * b
iloczyn(2,4,5)
iloczyn()
# Zad7
# Napisz funkcje za pomocą operatora *, która wykona te same działanie co w zadaniu 6.
def iloczyn_krotka(*liczby):
    for i in range(liczby[2]):
        print(liczby[0])
        liczby[0] = liczby[0] * liczby[1]
iloczyn(2, 4, 5)


# Zad8
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować listę zakupów w postaci: klucz
# to nazwa produktu a wartość to jego koszt. Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową wartość tych produktów.
def lista_zakupy(** zakupy):
    ilosc = len(zakupy)
    koszt = 0
    for value in zakupy.values():
        koszt += float(value)
    print('Ilośc produktów na liście: ' + str(ilosc))
    print('Koszt produktów na liście: ' + str(koszt))


lista_zakupy(slodycze=13, ziemniaki=50, piwo=15)
# Zad9
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami
# arytmetycznymi a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.

#zrobione

# Zad10.
# Z przedziału od 0 do 100 wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
def zapis_przedzial():
    liczby = []
    plik = open('ciagi.txt', 'w+')
    for i in range (101):
        if i % 4 == 0:
            liczby.append(i)

    plik.write(str(liczby))
    plik.close()

zapis_przedzial()
# Zad11.
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli

def odczyt_plik():
    plik = open('ciagi.txt',  'r')
    result = plik.readlines()
    print(result)

odczyt_plik()