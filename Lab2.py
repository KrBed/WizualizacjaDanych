import math
import sys as system

#Zad 1. Napisz skrypt, w którym tworzysz listę ulubionych sportów, odwróć ją a następnie dodaj mniej
#lubiane sporty na sam koniec.
sporty = ['bieganie', 'rower', 'siłownia', 'tenis']
sporty.reverse()
print(sporty)
sporty.append('piłka nożna')
sporty.append('narciarstwo')
print(sporty)
#Zad 2. Stwórz słownik skrótów powszechnie używanych w gazetach lub artykułach internetowych.
#Jako klucz przyjmij skrót danego słowa, wartość to rozwinięcie tego skrótu.
slownik = {"al.": 'aleja',"cd.": "ciąg dalszy","dr": "doktor", "lek.": "lekarz" }
print(slownik)
#Zad 3. Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl, co może być kluczem a co
#wartością w takim słowniku. Policz liczbę elementów w słowniku.
gry ={'Wiedzmin': 2008, 'OGame': 2000, 'War of Warcraft': 1997}
print(len(gry))
#Zad 4. Napisz skrypt, który pobiera od użytkownika zdanie i liczy wystąpienia litery a. Użyj funkcji input
print('Nampisz zdanie');
zdanie = str(input());
print(zdanie.count('a'))

#Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: ab + c.
#Użyj instrukcji readline() i write()).

system.stdout.write('wpisz pierwszą liczbę');
a = int(system.stdin.readline())
system.stdout.write('wpisz drugą liczbę');
b = int(system.stdin.readline())
system.stdout.write('wpisz trzecią liczbę');
c = int(system.stdin.readline())

result = a**b + c
print(result)

#Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od
#wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.
system.stdout.write('wpisz pierwszą liczbę');
a = int(system.stdin.readline())
system.stdout.write('wpisz drugą liczbę');
b = int(system.stdin.readline())
system.stdout.write('wpisz trzecią liczbę');
c = int(system.stdin.readline())

if a > b:
    if a > c:
        print('Liczba ' + str(a) + ' jest największa')
    else:
        print('Liczba ' + str(c) + ' jest największa')
else:
    if b > c:
        print('Liczba ' + str(c) + ' jest największa')
    else:
        print('Liczba ' + str(c) + ' jest największa')


#Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą
#użycia pętli for podnieś każdą liczbę do kwadratu.
liczby = [2, 3.5, 6, 7.5, 9, 2.5]
liczby2 = []

for liczba in liczby:
    num = math.pow(liczba, 2)
    liczby2.append(num)
print(liczby2)

#Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko parzyste liczby.

def isnumber(num):
   try:
     float(num)
     return True
   except ValueError:
       return False


oddNumber =[]
count = 1;

while count <= 10:
    print('Podaj ' + str(count) +'liczbę')
    num = input()
    while isnumber(num) != True:
        print('Podaj właściwą ' + str(1) + ' wartość')
        num = input()

    count += 1
    result = float(num) % 2
    if result == 0:
        oddNumber.append(num)

print(oddNumber)

#Zad. 9.
#Napisz skrypt, który liczy pierwiastek z liczby podanej przez użytkownika jeśli użytkownik poda wartość ujemną to powinien być wyłapany błąd.

print('Podaj liczbę z której chcesz obliczyć pierwiastek')
digit = input()

try:
    result = math.sqrt(float(digit))
    print(result)
except (ValueError, Exception):
    print('Wartość jest mniejsza od zera');



