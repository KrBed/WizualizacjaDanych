import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ad.1. Odwzoruj wykres znajdujący się w pliku graficznym w11.png znajdującym się folderze. Odcienie kolorów mogą się różnić, jednak główne barwy muszą być zachowane.
# Zapisz powstały wykres w formacie pdf.
#
# Zad.2. W jednym pliku wykonaj poniższe czynności:
#
# * załaduj dane z pliku lasy11.xlsx jako ramkę danych (Data Frame),
# * stwórz wykres słupkowy pionowy prezentujący dane zawarte w ramce danych (wszystkie dane)
# * umieść swój numer indeksu w lewym górnym rogu wykresu.
# Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.

# Zapisz wykres w formacie png za pomocą kodu.

# df = pd.read_excel('lasy11.xlsx')
# plt.text(0, 0, '136229',
#         verticalalignment='bottom', horizontalalignment='right',
#         color='green', fontsize=15)
# plt.title('Wykres')
# plt.bar(df['Rok'],df['Wartość'])
# plt.show()
# plt.savefig('wykres_11.png')
# print(df)

# Zad.3. W jednym pliku wykonaj poniższe czynności:
#
# * załaduj dane z pliku sklepy11.csv,
# * uporządkuj dane tak, aby dane liczbowe były zgodne z koncepcją "czystych danych" (w kolumnach)
# * stwórz ramkę danych wybierając dane za 2018 rok i stwórz na ich podstawie wykres kołowy
# * Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
#
# Zapisz wykres w formacie jpg za pomocą kodu.

df = pd.read_csv('sklepy11.csv',sep=';')
# print(df)
keys = list(df.keys())
data = []
for key in keys:
        tkey = key
        dot = key.find('.')
        if dot > 0:
                tkey = key[0:dot]

        data.append(list([tkey,float(df.loc[0, key]),df.loc[1, key],int(str(df.loc[2,key]).replace(' ',''))]))

df = pd.DataFrame(data,columns=['Sklep','Rok','OB','Wartość'])
df = df[df['Rok'] == 2018]
print(df)
plt.pie(df['Wartość'],labels=df['Sklep'], autopct='%1.1f%%',shadow=False, startangle=50)
plt.show()
print(df)
