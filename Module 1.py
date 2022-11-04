import datetime
import random


bericht = ''
while len(bericht) < 1 or len(bericht) > 140:
    bericht = input('Vul hier uw bericht in (maximaal 140 tekens): ')
    if len(bericht) < 1 or len(bericht) > 140:
        print('Uw bericht voldoet niet aan de eisen.')


d = datetime.datetime.now()
datum = d.strftime("%m/%d/%Y:%H/%M/%S")


naam = input('Geef uw naam (voor een anoniem bericht druk op enter): ')
if naam == '':
    naam = 'Anoniem'


stationnummer = random.randint(0,2)
stations = ['Hilversum', 'Amsterdam', 'Utrecht']
station = stations[stationnummer]


with open('berichten.txt', 'a') as f:
    f.write('\n'+bericht+'%5%'+naam+'%5%'+station+'%5%'+datum)
with open('berichten.txt') as fi:
    lines = fi.readlines()
with open('berichten.txt', 'w') as fil:
    for line in lines:
        if len(line)>1:
            fil.write(line)