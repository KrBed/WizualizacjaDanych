# Zadania.
# Zad1. Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu a następnie wyświetlte zmienne
import math

a = 10
b = 6
print(a)
print(b)
#Zad2. Stwórz skrypt kalkulator, w którym wykorzystać wszystkie podstawowe działania arytmetyczne
dzielenie = a / b
print(dzielenie)
dodawanie = a + b
print(dodawanie)
dzielenie_calkowite = a // b
print(dzielenie_calkowite)
reszta = a % b
print(reszta)
potega = b ** b
print(potega)
potega = pow(a, b)
print(potega)
#Zad3. Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +, -, *, /, **, %
c = 3
c += 2
print(c)
d = 5
d -= 1
print(d)
e = 2
e *= 2
print(e)
f = 3
f **= 3
print(f)
g = 7
g /= 3
print(g)
h = 7
h //= 3
print(g)
i = 9
i %= 4
print(i)


#Zad4. Napisz skrypt, który policzy i wyświetli następujące wyrażenia:
#𝑒10

#√ln (5 + 𝑠𝑖𝑛286
#⌊3, 55⌋
#⌈4, 80⌉

#Zad.5 Zapisz swoje imie i nazwisko w oddzielnych zmiennych wszystkie wielkimi literami. Użyj odpowiedniej
#metody by wyświetlić je pisane tak, że pierwsza litera jest wielka a pozostałe małe. (trzeba użyć metody capitalize)

name = 'KRZYSZTOF'
surname = 'BEDNARSKI'
print(name.capitalize() + ' ' + surname.capitalize())



#Zad.6 Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tekstu piosenki z powtarzającymi się
#słowami np. „la la la”. Następnie użyj odpowiedniej funkcji, która zliczy występowanie słowa „la”. (trzebaużyć metody count)
song = "Fajnie fajnie la la la ćwiczę pythona la la la bede go zjad la la la la la"
print(song.count('la'))

#Zad.7 Do poszczególnych elementów łańcucha możemy się odwoływać przez podanie indeksu. Np. pierwszy
#znak zapisany w zmiennej imie uzyskamy przez imie[0]. Zapisz dowolną zmienną łańcuchową i wyświetl jej
#drugą i ostatnią literę, wykorzystując indeksy.

zmiennalancuchowa = 'Kubuś Puchatek'
print(zmiennalancuchowa[1])
print(zmiennalancuchowa[len(zmiennalancuchowa) - 1])
#Zad.8 Zmienne łańcuchowe możemy dzielić wykorzystaj zmienną z Zad. 6 i spróbuj ją podzielić na
#poszczególne wyrazy. (trzeba użyć metody split)

chunk = song.split(' ')
print(chunk)

#Zad.9 Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. Następnie
#wyświetl je wykorzystując odpowiednie formatowanie
str ='string'
flo = 2.44
hex = '0x1b3'

print('string: {0:s},float: {1:2f},hex: {2:s} '.format(str, flo,hex))
