import pandas as pd

data = {'Country': ['Belgium', 'India', 'Brazil'],
        'Capital': ['Brussels', 'New Delhi', 'Brasília'],
        'Population': [11190846, 1303171035, 207847528]}
frame = pd.DataFrame(data)
print(frame)
df = pd.DataFrame(data, columns=['Country', 'Capital',
                                 'Population'])
# print(df)
# print(df.iloc[[0], [2]])
# print(df.loc[[2], ['Country']])
# print(df.loc[1])
# print(df.loc[:, 'Capital'])
# print(df.loc[1, 'Capital'])
# print(df[df['Population'] > 120000000])
# print(df.drop('Country', axis=1))
# print(df.shape)
# print(df.index)
# print(df.columns)
# print(df.info())
# print(df.count())