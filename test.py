'''a%5%Anoniem%5%Utrecht%5%11/03/2022:14/00/25
b%5%Anoniem%5%Amsterdam%5%11/03/2022:14/11/09
c%5%Anoniem%5%Amsterdam%5%11/03/2022:14/11/12'''

with open('berichten.txt') as file:
    file = file.read()
    lines = file.split('\n')
    gegevens = []
    for line in lines:
        gegevens.append(line.split('%5%'))
    print(gegevens)
