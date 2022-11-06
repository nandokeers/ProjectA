#import modules
import datetime
import psycopg2

def wachtwoord():
    # Mod wachtwoord
    ww = ''
    while ww != 'Welkom123':
        ww = input('Voer hier uw moderator wachtwoord in: ')
        if ww == 'Welkom123':
            controle()
            break
        else:
            print('Wachtwoord is incorrect')

def controle():
    #mod gegevens
    global modnaam
    global modmail
    global datum
    modnaam = input('Geef uw naam: ')
    modmail = input('geef uw E-mail: ')
    d = datetime.datetime.now()
    datum = d.strftime("%m/%d/%Y:%H/%M/%S")
    #import bericht
    with open('berichten.txt') as f:
        f = f.readlines()
        aantal = len(f)
        gegevens = []
        for l in range(len(f)):
            gegevens.append(f[l].split('%5%'))

    #hoeveelheid berichten tonen
    if aantal < 1:
        print('\nEr zijn geen berichten te controleren\nU bent klaar')
        raise SystemExit
    else:
        print('\nEr zijn nog', aantal, 'berichten te beoordelen')

    #Controleren?
    controleren = ''
    while controleren != 'ja' or controleren != 'Ja':
        controleren = input('Wilt u nu controleren? Ja / Nee:\n')
        if controleren == 'ja' or controleren == 'Ja':

            #bericht printen
            print('\nbericht:\n'+gegevens[0][0]+'\n')
            keuring = input('Keurt u dit bericht goed?\n')

            #bericht goedgekeurd
            if keuring == 'ja' or keuring == 'Ja':
                print('\ngoedgekeurd')
                global check
                check = True

                #overschrijven naar database
                transfer()

                #uit file halen
                f.remove(f[0])
                with open('berichten.txt', 'w') as file:
                    for line in f:
                        file.write(line)
                break

            #bericht afgekeurd
            elif keuring == 'nee' or keuring == 'Nee':
                print('\nafgekeurd')
                check = False

                #overschrijven naar databse
                transfer()

                #uit file halen
                f.remove(f[0])
                with open('berichten.txt', 'w') as file:
                    for line in f:
                        file.write(line)
                break

            #verkeerde invoer gegeven bij keuren
            else:
                print('Geen correcte invoer gegeven, probeer opnieuw')

        #berichten niet controleren
        elif controleren == 'nee' or controleren == 'Nee':
            print('U bent klaar')
            break

        #verkeerde invoer bij controleren
        else:
            print('Geen correcte invoer gegeven, probeer opnieuw')



def transfer():
    #code voor overschrijven naar database

    #bericht importeren
    with open('berichten.txt') as file:
        file = file.read()
        lines = file.split('\n')
        gegevens = []
        for line in lines:
            gegevens.append(line.split('%5%'))

    #conecten met database
    conn = psycopg2.connect(database="Project A",
                            host="127.0.0.1",
                            user="postgres",
                            password="Laartje123",
                            port="5432")
    cursor = conn.cursor()

    #Moderator gegevens overschrijven
    cursor.execute(""" INSERT INTO moderator (naam, emailadress, datum) 
    VALUES(%s,%s,%s);""", (modnaam, modmail, datum))
    conn.commit()
    conn.close()

    #opnieuw conecten database
    conn = psycopg2.connect(database="Project A",
                            host="127.0.0.1",
                            user="postgres",
                            password="Laartje123",
                            port="5432")
    cursor = conn.cursor()

    #modID ophalen
    cursor.execute("""SELECT ModID FROM Moderator WHERE emailadress = %s """, (modmail,))
    ModID = cursor.fetchone()

    #bericht gegevens incl. modID importeren in database
    cursor.execute(""" INSERT INTO bericht (Naam, locatie, Datum, Bericht, Goedgekeurd, ModID) 
    VALUES(%s,%s,%s,%s,%s,%s);""", (gegevens[0][1], gegevens[0][2], gegevens[0][3], gegevens[0][0], check, ModID))

    conn.commit()
    conn.close()
    print('\nOvergeschreven naar database')

#Run
wachtwoord()