import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Zad.1. Odwzoruj wykres znajdujący się w pliku graficznym 1.png znajdującym się folderze. Odcienie kolorów mogą się różnić, jednak główne barwy muszą być zachowane.
# Zapisz powstały wykres w formacie pdf.
#
# Zad.2. W jednym pliku wykonaj poniższe czynności:
#
# * załaduj dane z pliku mieszkania1.xlsx jako ramkę danych (Data Frame),
# * stwórz wykres słupkowy pionowy prezentujący dane zawarte w ramce danych (wszystkie dane)
# * umieść swój numer indeksu w lewym górnym rogu wykresu.

df = pd.DataFrame(np.random.rand(7,4), columns=list('ABCD'), index=list('abcdefg'))
print(df)
a = df.loc[['b','d'],['A','B']]
b = df.iloc[1:4, 0:3]
print(b)
df= pd.read_excel('mieszkania1.xlsx')
print(df)
a = df[df['Wartość'] >3000] # print(df.iloc[:, 0]);
print(a)
# bud = pd.DataFrame(df,columns=['Formy budownictwa'])
# print(bud)
# print(df.columns)
# print(df.index)
# d = {'fst': pd.Series(np.random.rand(3)),
#      'snd': pd.Series(np.random.rand(4))}
#
# df = pd.DataFrame(d,columns=['fst','dupa'])
# print(df)
# print(df.columns)
# print(df.index)

# indywidualne = df(df[0,'undywidualne'])
# komunalne = df(df[0,'komunalne'])
# print(indywidualne)
# print(komunalne)
# np.random.seed(10)
# data = np.random.normal(100, 20, 200)
# plt.boxplot(data)
# plt.show()
# Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
#
# Zapisz wykres w formacie pdf za pomocą kodu.
#
# Zad.3. W jednym pliku wykonaj poniższe czynności:
#
# * załaduj dane z pliku transport1.xlsx,
# * uporządkuj dane tak, aby dane liczbowe były zgodne z koncepcją "czystych danych" (w kolumnach)
# * stwórz dwa wykresy kołowe prezentujące względny udział różnych kategorii hoteli w danym roku (wybierz dowolne dwa lata samodzielnie)
# * Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
#
# Zapisz wykres w formacie jpg za pomocą kodu.