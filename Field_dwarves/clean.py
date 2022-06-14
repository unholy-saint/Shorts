import pandas as pd

df = pd.read_csv('stars.csv')

df = df[df['dist'].notna()]
df = df[df['mass'].notna()]
df = df[df['rad'].notna()]

mass = df['mass'].tolist()
rad = df['rad'].tolist()

newMass = []
newRad = []

for i in range(len(mass)):
    m = float(mass[i])*0.102763
    r = float(rad[i])*0.000954588

    newMass.append(m)
    newRad.append(r)

newDf = pd.DataFrame(
    list(zip(newMass, newRad)), columns=['SolMass', 'Solrad']
)

newDf.to_csv('new.csv')
