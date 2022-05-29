import pandas as pd
import numpy as np

# s = pd.Series([[1, 3, 5, np.nan, 6, 8]])
# print(s)
# s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek',
#                                       'Wiesiek', 'Eleonora'])
# print(s)

# DataFrame
# tworzenie dataframe na podstawie słownika
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528]}
# df = pd.DataFrame(data)
# print(df)
# DataFrame przechowuje typ dla każdej kolumny co możemy
# sprwadzić wpisując
# print(df.dtypes)
# możemy również w prosty sposób stworzyć serię danych - czyli
# próbki dla kolejnych
# dat, pomiarów czasu
# daty = pd.date_range('20210324', periods=5)
# print(daty)
# df = pd.DataFrame(np.random.randn(5, 4), index=daty,
#                   columns=list('ABCD'))
# print(df)
# biblioteka Pandas umożliwia również tworzenie DataFrame'ów z
# zewnętrznych źródeł danych
# CSV, odczyt i zapis
# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=',')
# print(df)
# df.to_csv('plik.csv', index=False)
# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx,header=0)
# print(df)

s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek',
'Wiesiek', 'Eleonora'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(s['Wiesiek'])
print(s.Wiesiek)
print(df['Populacja'])
print(df.iloc[[1],[1]])
#kolumna po etykiecie
print(df['Populacja'])
#pobieranie pojedynczej wartości po indeksie wiersza i kolumny
print(df.iloc[[0],[0]])
#pobieranie wartości po indeksie wiersza i etykiecie kolumny
print(df.loc[[0],["Kraj"]])
print(df.at[0,"Kraj"])
#podobnie jak w przypadku serii można odwoływać się do kolumn
# jak do pól klasy
#dodatkowo print jest wywoływany jak w pętli dla każdego
# elementu danej kolumny
# print('kraj: ' + df.Kraj)
#Pandas posiada również funkcje pozwalające na losowe
# pobieranie elementów lub
#w odniesieniu do procentowej wielkości całego zbioru
#jeden losowy element
# print(df.sample())
#n losowych elementów
# print(df.sample(2))
#ilość elementów procentowo, uwaga na zaokrąglenie
# print(df.sample(frac=0.5))
#jeżeli potrzeba nam więcej próbek niż znajduje się w zbiorze
# i dopuszczamy duplikaty
#to możemy użyć parametru replace, który będzie losował z
# powtórzeniami
# print(df.sample(n=10, replace=True))
#zamiast wyświetlać całą kolekcje możemy wyświetlić określoną
# ilość elementów od początku kolekcji
#lub od jej końca
# print(df.head())
# print(df.head(2))
# print(df.tail(1))
# Pandas jest też w stanie wyświetlić statystykę dla wartości,
# które dana kolekcja zawiera, o ile są jakieś kolumny
# z danymi numerycznymi
# print(df.describe())
# transpozycja to zmienna T kolekcji, podobnie jak w Numpy
# print(df.T)

# wyświetla dane z serii gdzie wartość większa od 1
print(s[(s>9)])
# nieco inny efekt można osiągnąć wykorzystując funkcję where,
# tóra zwraca kolekcję w oryginalnej wielkości
# (liczebności) elementów, ale wartości nie spełniające
# warunku uzupełnia wartością NaN
print(s.where(s > 10))
#możemy też podać wartość, która zostanie podstawiona zamiast
# NaN
print(s.where(s>10, 'za duże'))
# jeszcze inna własność where pozwala na modyfikowanie
# oryginalnego zbioru (domyślnie zwaracana jest kopia)
seria = s.copy()
seria.where(seria > 10, 'za duże', inplace=True)
print("########")
print(seria)
#wyświetla dane z serii gdzie wartość nie jest większa od 10
print(s[~(s > 10)])
#warunki możemy też łączyć
print(s[(s < 13) & (s > 8)])
#warunki dla pobierania DataFrame
print(df[df['Populacja']>1200000000])
#bardziej skomplikowane warunki
print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])
#inny przykład z listą dopuszczalnych wartości oraz isin
# zwracająca wartości boolowskie
print('#########')
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))
#zmiana, usuwanie i dodawanie danych
#w przypadku serii możemy dodać/zmienić wartość poprzez
# odwołanie się do elementu serii przez klucz (indeks)
s['Wiesiek'] = 15
print(s.Wiesiek)
s['Alan'] = 16
print(s)
# podobna operacja dla DataFrame ma nieco inny efekt - wartość
# ustawiona dla wszystkich kolumn
df.loc[3] = 'dodane'
print(df)
# ale można dodać wiersz w postaci listy
df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)
# usuwanie danych można wykonać przez funkcję drop, ale
# pamiętajmy, że operacja nie wykonuje się in-place więc
# zwracana jest kopia DataFrame z usuniętymi wartościami
new_df = df.drop([3])
print(new_df)
# więc jeżeli chcemy zmienić pierwotny zbiór dodajemy parametr
inplace=True
df.drop([3], inplace=True)
print(df)
# można usuwać również całe kolumny po nazwie indeksu, ale
# wykonanie tej komendy uniemożliwi
# wykonanie dalszego kodu (można przetstować po zakomentowaniu
# dalszej części listingu)
#df.drop('Kraj', axis=1, inplace=True)
# do DataFrame możemy dodawać również kolumny zamiast wierszy
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa','Europa']
print(df)
# Pandas ma również własne funkcje sortowania danych
print(df.sort_values(by='Kraj'))
# grupowania
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
# można też jak w SQL czy Excelu uruchomić funkcje agregujące
# na danej kolumnie
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))


#zad1,2
# plik = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(plik, header=0)
#
# print(df[df.Liczba > 1000])
# print('')
# print(df[df.Imie == 'RADOSŁAW'])
# print('')
# print(df.Liczba.sum())
# print('')
# grupa = df[df.Rok < 2006]
# print(grupa.Liczba.sum())
# grupa = df[df.Rok < 2006].groupby('Rok').agg({'Liczba': ['sum']})
# print(grupa)
# print('')
#
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
# print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#
# new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
# for index, group in enumerate(new_df, start=1):
#     print(f"{index} {group[0]}")
#     print(f" {group[1].iloc[0]['Imie']}", end='')
#     print(f" {group[1].iloc[0]['Liczba']}")
# print('')
# print("Chłopiec")
# print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])
# print("Dziewczynka")
# print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),
#                                                                                    ascending=False).iloc[0])

#zad3

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

print(df['Sprzedawca'].unique())
print('')
print(df.sort_values('Utarg', ascending=False).head(5))
print('')
print(df.groupby('Sprzedawca').size())
print('')
print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
print(df.groupby('Kraj').size())
print('')
print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
      agg({'Utarg': ['sum']}))
print('')
print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
rok_2004.to_csv("zamowienia_2004.csv", index=False)


