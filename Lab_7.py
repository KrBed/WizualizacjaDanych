import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
#bardzo prosty wykres liniowy
plt.plot([1, 2, 3, 4])
plt.ylabel('jakieś liczby')
plt.show()

#przekazujemy dwa wektory wartości, najpierw dla wektora x,
# następnie dla wektora y
#dodatkowo mamy tutaj przekazywany parametr w postaci stringa,
# który określa styl wykresu
#dla pełnej listy sprawdź dokumentację pod adresem
#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
#tutaj określamy listę parametrów w postaci [xmin, xmax, ymin,ymax]
# plt.axis([0, 6, 0, 20])
# plt.show()
#możemy też ustawić różne kolory dla poszczególnych elementów nakładając na siebie dwa wykresy
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'o')
# plt.axis([0, 6, 0, 20])
# plt.show()

#bazowy wektor wartości
t = np.arange(0., 5., 0.2)
#za pomocą pojedynczego wywołania funkcji plot() możemy
# wygenerować wiele wykresów na jednym płótnie (ang. canvas)
#każdorazowo podając niezbędne wartości: wartości dla osi x,
# wartości dla osi y, styl wykresu, ...
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
# plt.show()

# x = np.linspace(0, 2, 100)
#wykresy mogą być też dodawane do płótna definicja podefinicji zamiast w pojedynczym wywołaniu funkcji plot()
#tutaj użyty został również parametr label, który określa etykietę danego wykresu w legendzie
# plt.plot(x, x, label="liniowa")
# plt.plot(x, x**2, label="kwadratowa")
# plt.plot(x, x**3, label="sześcienna")
#etykiety osi
# plt.xlabel('etykieta x')
# plt.ylabel("etykieta y")
#tytuł wykresu
# plt.title("Prosty wykres")
#włączamy pokazanie legendy
# plt.legend()
# plt.savefig('wykres matplot.png')
# plt.show()
# im1 = Image.open('wykres matplot.png')
# im1 = im1.convert('RGB')
# im1.save('nowy.jpg')
#
# x = np.arange(0, 10, 0.1)
# s = np.sin(x)
# plt.plot(x, s, label="sin(x)")
#etykieta osi
# plt.xlabel('x')
# plt.ylabel('sin(x)')
#tytuł wykresu
# plt.title('Wykres sin(x)')
#umieszczamy legendę na wykresie
# plt.legend()
# plt.show()


#dane w postaci słownika, ale równie dobrze może to być Pandas DataFrame
# data = {'a': np.arange(50),
# 'c': np.random.randint(0, 50, 50),
# 'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
#aby w ten sposób przekazać parametry wykresu należy dodać niezbędny parametr data, który zawiera dane dostępne poprzez etykiety
#to oznacza, że 'a' jest równoważne data['a'] itd. Parametr c
# to skrót od color, tutaj przekazywany w formie wektora
#wartości kolorów dla każdej kolejnej wartości wykresu.
# Parametr s to scale - określa rozmiar, w tym przypadku punktu,dla
#każdej kolejnej wartości wektora wykresu. Reasumując dla
# pierwszego punktu wykresu będą brane poniższe wartości
# print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]},d={data['d'][0]}")
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('wartość a')
# plt.ylabel('wartość b')
# plt.show()

#podwykresy

# x1 = np.arange(0, 2, 0.02)
# x2 = np.arange(0, 2, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# plt.subplot(2, 1, 1,)
# plt.plot(x1, y1, '-')
# plt.title('wykres sin(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'r-')
# plt.xlabel('x')
# plt.ylabel('cos(x)')
# plt.title('wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()


# x1 = np.arange(0.0, 2.0, 0.02)
# x2 = np.arange(0.0, 2.0, 0.02)
# y1 = np.sin(2 * np.pi * x1)
# y2 = np.cos(2 * np.pi * x2)
# fig, axs = plt.subplots(3, 2)
# axs[0, 0].plot(x1, y1, '-')
# axs[0, 0].set_title('wykres sin(x)')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[1, 1].plot(x2, y2, 'r-')
# axs[1, 1].set_title('wykres cos(x)')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[2, 0].plot(x2, y2, 'r-')
# axs[2, 0].set_title('wykres cos(x)')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()

#wykres słupkowy
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia',
'Polska'],
'Stolica': ['Bruksela', 'New Delhi',
'Brasilia', 'Warszawa'],
'Kontynent': ['Europa', 'Azja', 'AmerykaPołudniowa', 'Europa'],
'Populacja': [11190846, 1303171035,207847528, 38675467]}
df = pd.DataFrame(data)
print(df)
grupa = df.groupby('Kontynent')
etykiety = list(grupa.groups.keys())
wartosci = list(grupa.agg('Populacja').sum())
plt.bar(x=etykiety, height=wartosci, color=['yellow','green', 'red'])
plt.xlabel('Kontynenty')
plt.ylabel('Populacja w mld')
plt.show()

#histogram

x = np.random.randn(10000)
# bins oznacza ilość "koszy" czyli słupków, do których mają wpadać wartości z wektora x
# facekolor oznacza kolor słupków
# alpha to stopień przezroczystości wykresu
# density oznacza czy suma ilości zostanie znormalizowana do rozkładu prawdopodobieństwa (czyli przedział 0, 1)
plt.hist(x, bins=50, facecolor='g', alpha=0.75, density=True)
plt.xlabel('Wartości')
plt.ylabel('Prawdopodobieństwo')
plt.title('Histogram')
#wyświetlanie siatki
plt.grid()
plt.show()

# wczytanie z pliku

df = pd.read_csv('dane.csv', header=0, sep=";",
decimal=".")
print(df)
seria = df.groupby('Imię i nazwisko')['Wartość zamówienia'].sum()
wedges, texts, autotext = plt.pie(x=seria,labels=seria.index, autopct=lambda pct:"{:.1f}%".format(pct),textprops=dict(color="black"), colors=['red','green'])
plt.title('Suma zamówień dla sprzedawców')
plt.legend(loc='lower right')
plt.ylabel('Procentowy wynik wartości zamówienia')
plt.show()





#zad1
# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ε [1, 20]. Dodaj etykietę do linii wykresu i
# wyświetl legendę. Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0,
# 1) oraz (1, długość wektora x)
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, label='f(x) = 1/x')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()

# zad2
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.
# x = np.arange(1, 21, 1)
# plt.plot(x, 1/x, 'g>:', label='f(x) = 1/x' )
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.axis([0, 20, 0, 1])
# plt.legend()
# plt.title('Wykres funkcji f(x) = 1/x dla x[1,20]')
# plt.show()

# zad3
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ε [0, 30] z krokiem 0.1. Dodaj
# etykiety i legendę do wykresu
# x = np.arange(0, 30, .1)
# plt.plot(x, np.sin(x), 'b', label='sin(x)')
# plt.plot(x, np.cos(x), 'r', label='cos(x)')
# plt.xlabel('x')
# plt.ylabel('sin(x) cos(x)')
# plt.legend(loc='upper right')
# plt.title('Wykres sin(x), cos(x)')
# plt.show()

# zad4
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj wykres
# punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’, dodaj paletę kolorów c na
# przykładzie listingu 6 a parametr s niech będzie wartością absolutną z różnicy wartości
# poszczególnych elementów wektorów x oraz y

# df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')
# print(df)
# # przygotowanie wektora kolorów
# colors = np.random.randint(0, 50, len(df.index))
# # przygotowanie wektora z rozmiarami 'kropek'
# scale = np.abs(df['sepal length'] - df['sepal width'])
#
# #
# plt.scatter(df['sepal length'], df['sepal width'], c=colors, s=scale)
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.show()

#zad5
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów
# stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# xlsx = pd.ExcelFile('..\\lab 5 i 6\\imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
# print(df)
# plt.subplot(1, 3, 1)
# grouped = df.groupby('Plec')
# etykiety = list(grouped.groups.keys())
# wartosci = list(grouped.agg('Liczba').sum())
# plt.bar(x=etykiety, height=wartosci, color=['green', 'red'])
# plt.xlabel('Płeć')
# plt.ylabel('Liczba narodzonych dzieci')
# # wykres 2
# plt.subplot(1, 3, 2)
# x = df['Rok'].unique()
# kobiety = df[(df.Plec == 'K')].groupby('Rok').agg({'Liczba':['sum']}).values
# mezczyzni = df[(df.Plec == 'M')].groupby('Rok').agg({'Liczba':['sum']}).values
# plt.plot(x, kobiety, label="Kobiety")
# plt.plot(x, mezczyzni, label="Mężczyźni")
# plt.xlabel('Rok')
# #
# # # wykres 3
# plt.subplot(1, 3, 3)
# x = df['Rok'].unique()
# y = df.groupby('Rok').agg('Liczba').sum()
# plt.bar(x, y)
# plt.xlabel('Rok')
# # wyświetlamy cały wykres
# plt.subplots_adjust(wspace=0.85)
# plt.show()
#zad6
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego sprzedawcy i
# wyświetl wykres kołowy z procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień.
# Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut ‘explode’ tego wykresu.
# Przetestuj ten atrybut na wykresie.
# df = pd.read_csv('..\\lab 5 i 6\\zamowienia.csv', sep=';')
# policzone = df.groupby('Sprzedawca')['Utarg'].sum()
# print(policzone)
# # explode
# explode = [0.0 for n in range(len(policzone.index))]
# # określamy które kawałki i o ile wysunąć, tu losujemy jeden
# explode[np.random.randint(0, len(policzone.index))] = 0.2
# wedges, texts, autotext = plt.pie(x=policzone, labels=policzone.index,
#                                   autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color='black'), explode=explode, shadow=True)
# plt.title("Procentowy udział kwot zamówień sprzedawców")
# plt.show()