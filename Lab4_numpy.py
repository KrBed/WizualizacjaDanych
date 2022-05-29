import numpy as np

# a = np.arange(10)
# print(a)
# b = np.array([0, 1, 2], dtype='int16')
# print(b.dtype)
# c = b.astype('float')
# print(c.dtype)
# print(c.shape)
# print(c.ndim)
# print(b)
# m = np.array([np.arange(2), np.arange(2)])
# print(type(m.shape))
# zeros = np.zeros((5, 2))
# ones = np.ones((5, 5))
# print(zeros.dtype)
# print(ones.dtype)
# empty = np.empty((4,4))
# print(empty)
# liczby = np.arange(1,2,0.1)
# print(liczby)
# liczby_lin = np.linspace(1,2,10)
# print(liczby_lin)
# z = np.indices((5,3))
# print(z)
# x, y = np.mgrid[0:5, 0:5]
# print(x)
# print(y)
# a = [2,3,4,5,56]
# mat_diag = np.diag(a)
# print(mat_diag)
# marcin = b'Marcin'
# mar = np.frombuffer(marcin,'S1')
# print(mar)
# a= np.arange(10)
# print(a)
# s = slice(4,7,2)
# print(a[s])
# mat = np.arange(25)
# print(mat)
# mat = mat.reshape((5,5))
# # print(mat)
# # print(mat[2:])
# print(mat[:,1])
# Zad 1 Za pomocą funkcji arange stwórz tablicę numpy składającą się z 15 kolejnych wielokrotności liczby 3.
a = np.arange(3, 48, 3)
# print(a)
# Zad2 Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej
# kopię przekonwertowaną na typ int64
b =np.arange(1,23,1.3,dtype='float')
conwert = b.astype('int64')
# print(conwert)
#zad3Napisz funkcję, która będzie:
# • Przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# • Zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1

# def create_array(n):
#     return np.arange(1,n*n +1)
#
# print(create_array(5))
# zad 4 Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji
# potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji logspace generuj
# tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2,4,8,16]
def generuj_array(liczba,ilosc):
    print(np.logspace(1,ilosc,num=ilosc,base=liczba))

generuj_array(2, 4)

# Napisz funkcję, która:
# • Na wejściu przyjmuje jeden parametr określający długość wektora
# • Na podstawie parametru generuj wektor, ale w kolejności odwróconej
# • Generuj macierz diagonalną z w/w wektorem jako przekątną
def diagonalna(n):
    a = np.arange(n,-1,-1)
    print(a)
    diag = np.diag(a)
    return diag

print(diagonalna(5))


# Zad6.
# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci
# wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.
malina = np.array(list('malina'))
mrowka = np.array(list('mrówka'))
armata = np.array(list('armata'))
armata = np.flip(armata)

wykreslanka = np.zeros((6,6), dtype='str')

print(wykreslanka)

wykreslanka = np.diag(mrowka)
wykreslanka[:, 0] = malina
#wykreslanka[5,::-1] = armata
wykreslanka[5,:] = armata
print(wykreslanka)
print("")
wykreslanka[:, 0] = mrowka
wykreslanka[5,::-1] = armata
for a in range(5):
    wykreslanka[a,a] = malina[a]
print(wykreslanka)

# Zad7.
# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
# [4 2 4]
# [6 4 2]]
# Przy założeniach:
# funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność
# liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

def macierz(n):
    mac = np.zeros((n, n), dtype='int32')
    mac += np.diag([2 for _ in range(n)])
    for i in range(1, n):
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=i)
        mac += np.diag([2+(2*i) for _ in range(n-i)], k=-i)
    print(mac)

macierz(8)

# Zadanie 8
# Napisz funkcję, która:
# • jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr
# ‘kierunek’,
# • parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# • funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że ilość
# wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację
def podziel(tab, kierunek='poziomo'):
    print(tab)
    if kierunek == 'poziomo':
        # nieparzysta liczba wierszy
        if tab.shape[0] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę wierszy")
            return
        p1 = tab[0:int(tab.shape[0]/2), :]
        p2 = tab[int(tab.shape[0]/2):, :]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)
    elif kierunek == "pionowo":
        if tab.shape[1] % 2 != 0:
            print("Tablica posiada nieprzystą liczbę kolumn")
            return
        p1 = tab[:, 0:int(tab.shape[1]/2)]
        p2 = tab[:, int(tab.shape[1] / 2):]
        print("***** część 1 *****")
        print(p1)
        print("***** część 2 *****")
        print(p2)

podziel(np.arange(36).reshape((6,6)), kierunek='pionowo')

# zad9
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)

# Zadanie 9
# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie
# zawierała kolejne wartości ciągu Fibonacciego.
macierz = np.ones(25, dtype='int32')
print(macierz)
for a in range(0, 25, 1):
    element = fib(a)
    macierz[a] = element
print(macierz)
macierz = macierz.reshape((5, 5))
print(macierz)