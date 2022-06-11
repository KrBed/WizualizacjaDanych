import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---
# title: "Egzamin (zerowy termin) - Wizualizacja danych - Zestaw 2"
# lang: pl
# output:
#   pdf_document: default
#   word_document: default
# ---
#
# *Zadanie 1 i 2 po 15 pkt. Zadanie 3 - 20 pkt. *
#
# *Punktacja: 46-50 pkt - bdb(5,0); 41-45 pkt - db+(4,5); 36-40 pkt - db(4,0); 31-35 pkt - dst+(3,5); 26-30 pkt - dst(3,0); 0-25 pkt - ndst (2,0).*
#
# Wykonując pierwsze zadanie na 75% można otrzymać przepisanie pozytywnej oceny z ćwiczeń.
#
# Zad.1. Odwzoruj wykres znajdujący się w pliku graficznym 2.png znajdującym się folderze. Odcienie kolorów mogą się różnić, jednak główne barwy muszą być zachowane.
# Zapisz powstały wykres w formacie jpg.
#
# Zad.2. W jednym pliku wykonaj poniższe czynności:
#
# * załaduj dane z pliku mieszkania2.xlsx jako ramkę danych (Data Frame),
# * stwórz wykres kołowy prezentujący dane tylko za 2015 rok
# * umieść swój numer indeksu w lewym górnym rogu wykresu.
# Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
#
# Zapisz wykres w formacie pdf za pomocą kodu.

df = pd.read_excel('mieszkania2.xlsx')
df = df[df['Rok'] == 2015]
ind = df.loc[:, ['Formy budownictwa','Wartość']]

labels = list(ind.loc[:,'Formy budownictwa'])
# labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
sizes = list(ind.loc[:,'Wartość'])
print(sizes)

plt.pie(sizes, labels=labels, autopct='%1.1f%%',shadow=False, startangle=50)
plt.axis('equal')
plt.text(1, 1, '136229', style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 10})
plt.title('Formy budownictwa 2015')
plt.legend(title='Legenda:',loc='lower right')
plt.savefig('pie_plot.pdf')
plt.show()

# Zad.3. W jednym pliku wykonaj poniższe czynności:
#
# * załaduj dane z pliku turystyka2.xlsx,
# * uporządkuj dane tak, aby dane liczbowe były zgodne z koncepcją "czystych danych" (w kolumnach)
# * stwórz wykres słupkowy prezentujące względny udział różnych kategorii hoteli w danym roku (wybierz dowolny rok samodzielnie)
# * Wykres powinien być estetyczny i podpisany. Im więcej - tym lepiej.
#
# Zapisz wykres w formacie png za pomocą kodu.

df = pd.read_excel('turystyka2.xlsx')
# df = pd.melt(df)
keys = list(df.keys())

data =[]
for key in keys:
     tkey = key
     dot = key.find('.')
     if dot > 0:
          tkey = key[0:dot]

     data.append(list([tkey,df.loc[0, key],df.loc[1, key]]))

newdf = pd.DataFrame(data, columns=["kategoria", "Rok", "Wartość"])
newdf = newdf[newdf['Rok'] == 2015]

plt.bar(newdf['kategoria'],newdf['Wartość'])
plt.show()
plt.title('Wykres słupkowy')
plt.savefig('słupkowt.png')

print(newdf)



