import pandas as pd

df = pd.read_csv('merged.csv')


del df['Unnamed: 0']
del df['Unnamed: 0.1']

df = df[df['dist'].notna()]
df = df[df['SolMass'].notna()]
df = df[df['Solrad'].notna()]


df.to_csv('cleanAgain.csv')
