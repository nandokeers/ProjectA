from tkinter import *
from PIL import ImageTk, Image
import requests
from time import strftime
import psycopg2

def faciliteitenophalen(stad):
    # connectie database
    conn = psycopg2.connect(database="Project A",
                            host="127.0.0.1",
                            user="postgres",
                            password="Laartje123",
                            port="5432")
    # connectie cursor
    cursor = conn.cursor()

    # execute Query
    cursor.execute('''SELECT station_city, ov_bike, elevator, toilet, park_and_ride FROM station_service''')

    # berichten gesorteerd op dit station
    faciliteiten = cursor.fetchall()
    global opstation
    opstation = []
    for trans in faciliteiten:
        if trans[0] == stad:
            opstation = trans



    # close cursor
    cursor.close()

    # close connection
    conn.close()
def berichtenophalen(stad):
    conn = psycopg2.connect(database="Project A",
                            host="127.0.0.1",
                            user="postgres",
                            password="Laartje123",
                            port="5432")
    # cursor
    cursor = conn.cursor()

    # execute Query
    cursor.execute('''SELECT naam, bericht, datum, locatie, goedgekeurd FROM bericht''')

    # berichten gesorteerd op dit station
    berichten = cursor.fetchall()
    berichten.reverse()
    bericht = []
    for trans in berichten:
        if trans[3] == stad and trans[4] == True:
            bericht.append(trans)

    # benodigde berichten
    global bericht1
    global bericht2
    global bericht3
    global bericht4
    global bericht5
    bericht1 = ''
    bericht2 = ''
    bericht1 = ''
    bericht2 = ''
    bericht2 = ''
    try:
        bericht1 = bericht[0]
        bericht2 = bericht[1]
        bericht3 = bericht[2]
        bericht4 = bericht[3]
        bericht5 = bericht[4]
    except:
        pass

    # close cursor
    cursor.close()

    # close connection
    conn.close()

def weather_get(stad):
    key = "785b13658e57032c0a8b258a7dbe1afa"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    compleet = url + "appid=" + key + "&q=" + stad
    response = requests.get(compleet)
    weather = response.json()
    kelvin = 273
    global city
    global temp
    global temp_min
    global temp_max

    city = weather["name"]
    temp = str(round((weather['main']['temp'] - kelvin), 1))
    temp_min = str(round((weather['main']['temp_min'] - kelvin), 1))
    temp_max = str(round((weather['main']['temp_max'] - kelvin), 1))


def terug():
    try:
        stationframe.destroy()
    except:
        pass
    mainframe()




def station(stad):
    #main window sluiten
    frame.destroy()

    #frame maken
    global stationframe
    stationframe = Frame(root)
    stationframe.config(bg='#FFC917')
    stationframe.columnconfigure(0, weight=1)
    stationframe.columnconfigure(1, weight=1)
    stationframe.columnconfigure(2, weight=1)
    stationframe.pack(pady=40)

    # frame wallpaper
    bg = Image.open("foto's/framewp.png")
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(stationframe, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image

    #station label maken
    stationlabel = Label(stationframe, text='Welkom op '+stad+' Centraal!', font=('Sans', 20), bg='#FFC917')
    stationlabel.grid(row=0, column=1, pady=20, padx=10, sticky='WE', ipady=50, ipadx=50)

    #tijd
    def time():
        string = strftime('%H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000, time)
    lbl = Label(stationframe, font=('Sans', 20, 'bold'), bg='#FFC917')
    time()
    lbl.grid(row=0, column=2, padx=60, sticky='E')

    #datum
    d = strftime("%d %b, %Y")
    datum = Label(stationframe, text=d, font=('Sans', 20, 'bold'), bg='#FFC917')
    datum.grid(row=0, column=0, padx=60, sticky='W')

    # terugknop maken
    bckbutton = Button(stationframe, text='Terug', font=('Sans', 20), command=terug)
    bckbutton.grid(row=7, column=2, pady=10, padx=10, sticky='E')



    #weer
    weather_get(stad)

    #weermainlabel plaatsen
    weersberichtlabel = Label(stationframe, text='De weersvoorspelling voor '+stad+':', font=('Sans', 18), bg='#FFC917', justify='left')
    weersberichtlabel.grid(row=1, column=1, padx=10, pady=10, sticky='WN')


    huidigtemplabel = Label(stationframe, text='De huidige temperatuur is: '+temp+'°C\n', font=('Sans', 12), bg='#FFC917', justify='left')
    huidigtemplabel.grid(row=2, column=1, padx=10, pady=10, sticky='WS')

    mintemplabel = Label(stationframe, text='De minimale temperatuur vandaag is: ' + temp_min + '°C\n', font=('Sans', 12), bg='#FFC917', justify='left')
    mintemplabel.grid(row=3, column=1, padx=10, pady=10, sticky='WS')

    maxtemplabel = Label(stationframe, text='De maximale temperatuur vandaag is: ' + temp_max + '°C\n', font=('Sans', 12), bg='#FFC917', justify='left')
    maxtemplabel.grid(row=4, column=1, padx=10, pady=10, sticky='WS')


    #berichten ophalen
    berichtenophalen(stad)

    #berichten plaatsen
    bertitle = Label(stationframe, text='De laatste berichten over dit station:', font=('Sans', 18), bg='#FFC917', justify='left')
    bertitle.grid(row=1, column=0, pady=10, padx=10, sticky='W')
    try:
        #bericht1
        ber1 = Label(stationframe, text='Bericht 1:\n' + bericht1[0] + ': ' + bericht1[1] + '\n' + bericht1[2], font=('Sans', 12), bg='#FFC917', justify='left')
        ber1.grid(row=2, column=0, pady=10, padx=10, sticky='WS')

        #bericht2
        ber2 = Label(stationframe, text='Bericht 2:\n' + bericht2[0] + ': ' + bericht2[1] + '\n' + bericht2[2], font=('Sans', 12), bg='#FFC917', justify='left')
        ber2.grid(row=3, column=0, pady=10, padx=10, sticky='W')

        #bericht 3
        ber3 = Label(stationframe, text='Bericht 3:\n' + bericht3[0] + ': ' + bericht3[1] + '\n' + bericht3[2], font=('Sans', 12), bg='#FFC917', justify='left')
        ber3.grid(row=4, column=0, pady=10, padx=10, sticky='W')

        #bericht4
        ber4 = Label(stationframe, text='Bericht 4:\n' + bericht4[0] + ': ' + bericht4[1] + '\n' + bericht4[2], font=('Sans', 12), bg='#FFC917', justify='left')
        ber4.grid(row=5, column=0, pady=10, padx=10, sticky='W')

        #bericht5
        ber5 = Label(stationframe, text='Bericht 5:\n' + bericht5[0] + ': ' + bericht5[1] + '\n' + bericht5[2], font=('Sans', 12), bg='#FFC917', justify='left')
        ber5.grid(row=6, column=0, pady=10, padx=10, sticky='W')

    except:
        pass

    #faceliteiten ophalen
    faciliteitenophalen(stad)

    #faciliteitenlabel maken
    faciliteitenlabel = Label(stationframe, text='Beschikbare faciliteiten op dit station:        ', font=('Sans', 18), bg='#FFC917', justify='left')
    faciliteitenlabel.grid(row=1, column=2, pady=10, padx=10, sticky='WS')

    #faciliteitenfotos aanmaken
    imglift = Image.open("foto's/img_lift.png")
    imgfiets = Image.open("foto's/img_ovfiets.png")
    imgpr = Image.open("foto's/img_pr.png")
    imgtoilet = Image.open("foto's/img_toilet.png")

    #fotos resizen
    resized_image3 = imglift.resize((50, 50))
    liftfoto = ImageTk.PhotoImage(resized_image3)
    resized_image2 = imgfiets.resize((50, 50))
    fietsfoto = ImageTk.PhotoImage(resized_image2)
    resized_image1 = imgpr.resize((50, 50))
    parkandridefoto = ImageTk.PhotoImage(resized_image1)
    resized_image1 = imgtoilet.resize((50, 50))
    toiletfoto = ImageTk.PhotoImage(resized_image1)

    #fotogrid aanmaken
    fotoframe = Frame(stationframe, bg='#FFC917')
    fotoframe.grid(row=2, column=2, pady=10, padx=10, sticky='W')
    fotoframe.columnconfigure(0, weight=1)
    fotoframe.columnconfigure(1, weight=1)
    fotoframe.columnconfigure(2, weight=1)
    fotoframe.columnconfigure(3, weight=1)

    #foto plaatsen en uit garbage collector halen als faciliteit beschikbaar is

    #lift
    if opstation[2] == True:
        labellift = Label(fotoframe, image=liftfoto)
        labellift.grid(row=0, column=0, padx=10, pady=10)
        labellift.image = liftfoto
    else:
        labellift = Label(fotoframe, image=liftfoto)
        labellift.grid(row=0, column=0, padx=10, pady=10)

    #fiets
    if opstation[1] == True:
        labelfiets = Label(fotoframe, image=fietsfoto)
        labelfiets.grid(row=0, column=1, padx=10, pady=10)
        labelfiets.image = fietsfoto
    else:
        labelfiets = Label(fotoframe, image=fietsfoto)
        labelfiets.grid(row=0, column=1, padx=10, pady=10)

    #park and ride
    if opstation[4] == True:
        labelparkandride = Label(fotoframe, image=parkandridefoto)
        labelparkandride.grid(row=0, column=2, padx=10, pady=10)
        labelparkandride.image = parkandridefoto
    else:
        labelparkandride = Label(fotoframe, image=parkandridefoto)
        labelparkandride.grid(row=0, column=2, padx=10, pady=10)

    #toilet
    if opstation[3] == True:
        labeltoilet = Label(fotoframe, image=toiletfoto)
        labeltoilet.grid(row=0, column=3, padx=10, pady=10)
        labeltoilet.image = toiletfoto
    else:
        labeltoilet = Label(fotoframe, image=toiletfoto)
        labeltoilet.grid(row=0, column=3, padx=10, pady=10)




def mainpage():
    #maken main window
    global root
    root = Tk()
    root.geometry('1920x1080')
    root.title('NS-Reviews')
    root.config(bg='#FFC917')
    root.attributes('-fullscreen', True)
    bg = Image.open("foto's/bg.png")
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

    #frame wallpaper
    bg = Image.open("foto's/framewp.png")
    background_image = ImageTk.PhotoImage(bg)
    background_label = Label(frame, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = background_image


    #maken title main
    mainlabel = Label(frame, text='Welkom bij NS', font=('Sans', 20), bg='#FFC917')
    mainlabel.grid(row=0, column=1, pady=20, padx=10, ipady=30, ipadx=50)
    mainsublabel = Label(frame, text='Selecteer het station waar u zich bevindt:', font=('Sans', 12), bg='#FFC917')
    mainsublabel.grid(row=1, column=1, pady=10, padx=10)

    #plaatsen foto's
    utrimg = Image.open("foto's/utrecht.jpg")
    amsimg = Image.open("foto's/amsterdam.jpg")
    hilimg = Image.open("foto's/hilversum.png")

    resized_image3 = utrimg.resize((300, 300))
    utrechtimg = ImageTk.PhotoImage(resized_image3)
    resized_image2 = amsimg.resize((300, 300))
    amsterdamimg = ImageTk.PhotoImage(resized_image2)
    resized_image1 = hilimg.resize((300, 300))
    hilversumimg = ImageTk.PhotoImage(resized_image1)


    utrphoto = Label(frame, image=utrechtimg)
    utrphoto.grid(row=2, column=0, padx=20, pady=40, sticky='WE')

    amsphoto = Label(frame, image=amsterdamimg)
    amsphoto.grid(row=2, column=1, padx=20, pady=40, sticky='WE')

    hilphoto = Label(frame, image=hilversumimg)
    hilphoto.grid(row=2, column=2, padx=20, pady=40, sticky='WE')


    #maken buttons
    utrbtn = Button(frame, text='  Utrecht  ', font=('Sans', 20), command=lambda: [station('Utrecht')])
    amsbtn = Button(frame, text='Amsterdam', font=('Sans', 20), command=lambda: [station('Amsterdam')])
    hilbtn = Button(frame, text='Hilversum', font=('Sans', 20), command=lambda: [station('Hilversum')])
    utrbtn.grid(row=3, column=0, padx=10, pady=20, sticky='WE')
    amsbtn.grid(row=3, column=1, padx=10, pady=20, sticky='WE')
    hilbtn.grid(row=3, column=2, padx=10, pady=20, sticky='WE')

    # tijd
    def time():
        string = strftime('%H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000, time)
    lbl = Label(frame, font=('Sans', 20, 'bold'), bg='#FFC917')
    time()
    lbl.grid(row=0, column=2, pady=10, padx=60, sticky='E')

    # datum
    d = strftime("%d %b, %Y")
    datum = Label(frame, text=d, font=('Sans', 20, 'bold'), bg='#FFC917')
    datum.grid(row=0, column=0, padx=60, sticky='W')

    root.mainloop()

mainpage()