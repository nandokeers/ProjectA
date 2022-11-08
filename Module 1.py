#import modules
import datetime
import random
from tkinter import *
from PIL import ImageTk, Image

def mainpage():
    #maken main window
    global root
    root = Tk()
    root.geometry('1920x1080')
    root.title('NS-Reviews')
    root.config(bg='#FFC917')
    root.attributes('-fullscreen', True)

    #window achergrond
    bg = Image.open('bg.png')
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    mainframe()

def mainframe():
    #maken frame
    global frame
    frame = Frame(root)
    frame.config(bg='#FFC917')
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.pack(pady=40)

    #frame achtergrond
    bg = Image.open('framewp.png')
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(frame, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    # maken title main
    mainlabel = Label(frame, text='Welkom bij NS', font=('Sans', 20), bg='#FFC917')
    mainlabel.grid(row=0, column=1, pady=20, padx=10, ipady=30, ipadx=50)
    sublabel = Label(frame, text='Laat een bericht achter en deel uw ervaring!', font=('Sans', 16), bg='#FFC917')
    sublabel.grid(row=1, column=1, pady=10, padx=10)

    berichtlabel = Label(frame, text='Uw bericht:', font=('Sans', 16), bg='#FFC917')
    berichtlabel.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    texbox = Text(frame, height=4, font=('Sans', 12))
    texbox.grid(row=3 , columnspan=3, pady=20, padx=20, ipady=50, ipadx=50, sticky='W')

    naamlabel = Label(frame, text='Uw naam:', font=('Sans', 16), bg='#FFC917')
    naamlabel.grid(row=4, column=0, padx=10, pady=10, sticky="W")

    entry = Entry(frame, width=20, justify=LEFT, font=('Sans', 12))
    entry.grid(row=5, column=0, pady=20, padx=20, ipady=5, ipadx=5, sticky='W')

    def sendinput():
        global bericht
        if len(entry.get()) <1:
            naam = 'anoniem'
        else:
            naam=str(entry.get())

        if len(texbox.get(1.0, "end-1c")) < 1 or len(texbox.get(1.0, "end-1c")) > 140:
            pass
        else:
            bericht = texbox.get(1.0, "end-1c")

        def verwerkbericht(bericht, naam):
            # datum en tijd
            d = datetime.datetime.now()
            datum = d.strftime("%m/%d/%Y:%H/%M/%S")

            # station
            stationnummer = random.randint(0, 2)
            stations = ['Hilversum', 'Amsterdam', 'Utrecht']
            station = stations[stationnummer]

            # filewrite
            with open('berichten.txt', 'a') as f:
                f.write('\n' + bericht + '%5%' + naam + '%5%' + station + '%5%' + datum)
            with open('berichten.txt') as fi:
                lines = fi.readlines()
            with open('berichten.txt', 'w') as fil:
                for line in lines:
                    if len(line) > 1:
                        fil.write(line)

        try:
            verwerkbericht(bericht, naam)
        except:
            pass
        entry.delete(0, END)
        texbox.delete("1.0", "end")

    sendinputbutton = Button(frame, text='Verzenden', font=('Sans', 20), bg='#FFC917', command=lambda: [sendinput()])
    sendinputbutton.grid(row=7, column=2, padx=20, pady=60, sticky='ES')

    def cleartext():
        entry.delete(0, END)
        texbox.delete("1.0","end")
    clearinputbutton = Button(frame, text='Leegmaken', font=('Sans', 20), bg='#FFC917', command=lambda: [cleartext()])
    clearinputbutton.grid(row=7, column=0, padx=20, pady=60, sticky='WS')

    root.mainloop()
mainpage()