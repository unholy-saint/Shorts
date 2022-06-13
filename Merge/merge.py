import pandas as pd

csv1 = pd.read_csv('stars.csv')
csv2 = pd.read_csv('new.csv')

h1 = csv1.head(0)
h2 = csv2.head(0)
print(h1)

merged = csv1.merge(csv2, on='serial')
del merged['mass']
del merged['rad']

merged.to_csv('merged.csv')
