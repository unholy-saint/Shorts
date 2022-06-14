import csv

with open('cleanAgain.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

for i in range(len(data)):
    if i == 0:
        data[i].append('gravity')

    else:
        Solmass = data[i][3]
        Solrad = data[i][4]

        m = float(Solmass) * 1.989e+30
        r = float(Solrad) * 6.957e+8

        g = (6.67e-11 * m)/r**2

        g = f'{str(g)} m/s^2'

        data[i].append(g)

with open('g.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
