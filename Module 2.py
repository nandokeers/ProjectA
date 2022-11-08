#import modules
import datetime
import psycopg2
from tkinter import *
from PIL import ImageTk, Image

def transfer():
    #code voor overschrijven naar database

    #conecten met database
    conn = psycopg2.connect(database="Project A",
                            host="127.0.0.1",
                            user="postgres",
                            password="Laartje123",
                            port="5432")
    cursor = conn.cursor()

    #Moderator gegevens overschrijven
    cursor.execute(""" INSERT INTO moderator (naam, emailadress, datum) 
    VALUES(%s,%s,%s);""", (naam, modmail, datum))
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

def uitfilehalen():
    with open('berichten.txt') as fi:
        fi = fi.readlines()
        fi.remove(fi[0])
    with open('berichten.txt', 'w') as fw:
        for line in fi:
            fw.write(line)



def berichtophalen():
    with open('berichten.txt') as f:
        f = f.readlines()
        global aantal
        global gegevens
        aantal = len(f)
        gegevens = []
        for l in range(len(f)):
            gegevens.append(f[l].split('%5%'))

def backtomain():
    try:
        modframe.destroy()
    except:
        pass
    try:
        ctrlframe.destroy()
    except:
        pass
    mainframe()

def controleframe():
    # controleframe aanmaken
    global ctrlframe
    ctrlframe = Frame(root)
    ctrlframe.config(bg='#FFC917')
    ctrlframe.columnconfigure(0, weight=1)
    ctrlframe.columnconfigure(1, weight=1)
    ctrlframe.columnconfigure(2, weight=1)
    ctrlframe.pack(pady=40)
    # frame achtergrond
    bg = Image.open("foto's/framewp.png")
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(ctrlframe, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    # controle mainlabel maken
    ctrllabel = Label(ctrlframe, text='Welkom bij NS-Moderators', font=('Sans', 20), bg='#FFC917')
    ctrllabel.grid(row=0, column=1, pady=20, padx=10, ipady=30, ipadx=50)
    ctrlsublabel = Label(ctrlframe, text='U kunt hiermee berichten beoordelen', font=('Sans', 16), bg='#FFC917')
    ctrlsublabel.grid(row=1, column=1, pady=60, padx=10, sticky='W')



    #-----------------bericht
    # bericht label
    brlabel = Label(ctrlframe, text='Bericht:', font=('Sans', 12), bg='#FFC917')
    brlabel.grid(row=2, column=1, pady=10, padx=10, sticky='W')

    # berichten ophalen
    berichtophalen()
    if aantal > 0:
        bericht = gegevens[0][0]
        bernaam = gegevens[0][1]
    else:
        bernaam = 'Geen berichten beschikbaar'
        bericht = '\nProbeer later opnieuw'

    # bericht plaatsen
    berichtlabel = Label(ctrlframe, text=bernaam+': '+bericht, font=('Sans', 12), bg='#FFC917', justify=LEFT)
    berichtlabel.grid(row=3, column=1, pady=10, padx=10, sticky='W')

    # datum
    global datum
    d = datetime.datetime.now()
    datum = d.strftime("%m/%d/%Y:%H/%M/%S")

    #------------keurknoppen
    def goedgekeurd():
        global check
        check = True
        transfer()
        uitfilehalen()
        ctrlframe.destroy()
        controleframe()
    # goedknop
    if aantal > 0:
        goed = Button(ctrlframe, text='Goedgekeurd', font=('Sans', 16), bg='#FFC917', command=lambda: [goedgekeurd()])
        goed.grid(row=4, column=1, padx=10, pady=30, sticky='ES')

    def afgekeurd():
        global check
        check = False
        transfer()
        uitfilehalen()
        ctrlframe.destroy()
        controleframe()
    # nietgoedknop
    if aantal > 0:
        fout = Button(ctrlframe, text='Afgekeurd', font=('Sans', 16), bg='#FFC917', command=lambda: [afgekeurd()])
        fout.grid(row=4, column=1, padx=10, pady=30, sticky='WS')

    # terugknop
    uitloggen = Button(ctrlframe, text='Uitloggen', font=('Sans', 16), bg='#FFC917', command=lambda: [backtomain()])
    uitloggen.grid(row=5, column=1, padx=10, pady=30, sticky='WS')

def modframe():
    # modframe aanmaken
    frame.destroy()
    global modframe
    modframe = Frame(root)
    modframe.config(bg='#FFC917')
    modframe.columnconfigure(0, weight=1)
    modframe.columnconfigure(1, weight=1)
    modframe.columnconfigure(2, weight=1)
    modframe.pack(pady=40)
    # frame achtergrond
    bg = Image.open("foto's/framewp.png")
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(modframe, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    # modmainlabel maken
    modlabel = Label(modframe, text='Welkom bij NS-Moderators', font=('Sans', 20), bg='#FFC917')
    modlabel.grid(row=0, column=1, pady=20, padx=10, ipady=30, ipadx=50)
    modsublabel = Label(modframe, text='U kunt hiermee berichten beoordelen', font=('Sans', 16), bg='#FFC917')
    modsublabel.grid(row=1, column=1, pady=60, padx=10, sticky='W')

    #--------------modgegevens ophalen
    # naam
    nmlabel = Label(modframe, text='Vul hier uw naam in:', font=('Sans', 16), bg='#FFC917')
    nmlabel.grid(row=2, column=1, pady=10, padx=10, sticky='W')
    nm = Entry(modframe, width=40, font=('Sans', 12))
    nm.grid(row=3, column=1, pady=10, padx=10, sticky='W')

    # email
    maillabel = Label(modframe, text='Vul hier uw E-mail in:', font=('Sans', 16), bg='#FFC917')
    maillabel.grid(row=4, column=1, pady=10, padx=10, sticky='W')
    mail = Entry(modframe, width=50, font=('Sans', 12))
    mail.grid(row=5, column=1, pady=10, padx=10, sticky='W')

    # volgendeknop maken
    def volgende():
        global naam
        naam = str(nm.get())
        global modmail
        modmail = str(mail.get())
        if len(naam)>1 and len(modmail)>1:
            if '@' in modmail and ('.com' in modmail or '.nl' in modmail):
                modframe.destroy()
                controleframe()

    volg = Button(modframe, text='volgende', font=('Sans', 16), bg='#FFC917', command=lambda: [volgende()])
    volg.grid(row=8, column=1, padx=10, pady=30, sticky='ES')

    # afsluitenknop maken
    stop = Button(modframe, text='Terug', font=('Sans', 16), bg='#FFC917', command=lambda: [backtomain()])
    stop.grid(row=8, column=1, padx=10, pady=30, sticky='WS')



def mainpage():
    # maken main window
    global root
    root = Tk()
    root.geometry('1920x1080')
    root.title('NS-Reviews')
    root.config(bg='#FFC917')
    root.attributes('-fullscreen', True)

    # window achergrond
    bg = Image.open("foto's/bg.png")
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    mainframe()

def mainframe():
    # maken mainframe
    global frame
    frame = Frame(root)
    frame.config(bg='#FFC917')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.pack(pady=40)

    # mainframe achtergrond
    bg = Image.open("foto's/framewp.png")
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(frame, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image
    # maken title main
    mainlabel = Label(frame, text='Welkom bij NS-Moderators', font=('Sans', 20), bg='#FFC917')
    mainlabel.grid(row=0, column=1, pady=20, padx=10, ipady=30, ipadx=50)
    sublabel = Label(frame, text='U kunt hiermee berichten beoordelen', font=('Sans', 16), bg='#FFC917')
    sublabel.grid(row=1, column=1, pady=60, padx=10, sticky='W')

    # entry voor wachtwoord maken
    wwlabel = Label(frame, text='Voer hier het moderator wachtwoord in: ', font=('Sans', 16), bg='#FFC917')
    wwlabel.grid(row=2, column=1, padx=10, pady=10, sticky='W')

    ww = Entry(frame, font=('Sans', 12), width=20)
    ww.grid(row=3, column=1, pady=10, padx=10, sticky='W')


    # clearbutton
    def cleartext():
        ww.delete(0, END)
    clearinputbutton = Button(frame, text='Leegmaken', font=('Sans', 16), bg='#FFC917', command=lambda: [cleartext()])
    clearinputbutton.grid(row=7, column=1, padx=10, pady=30, sticky='WS')

    # verzendknop
    def verzend():
        wachtwoord = ww.get()
        if wachtwoord == 'Welkom123':
            modframe()
        else:
            ww.delete(0, END)
            errorlabel = Label(frame, text='Wachtwoord is niet correct', font=('Sans', 16), bg='#FFC917')
            errorlabel.grid(row=4, column=1, padx=10, pady=10, sticky='W')

    verzendbutton = Button(frame, text='Volgende', font=('Sans', 16), bg='#FFC917', command=lambda: [verzend()])
    verzendbutton.grid(row=7, column=1, padx=10, pady=30, sticky='ES')

    # window loopen
    root.mainloop()

# window openen aanroepen
mainpage()