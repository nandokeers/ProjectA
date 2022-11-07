from tkinter import *
from PIL import ImageTk, Image
import requests
from time import strftime

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
    global img_code

    city = weather["name"]
    temp = str(round((weather['main']['temp'] - kelvin), 2))
    temp_min = str(round((weather['main']['temp_min'] - kelvin), 2))
    temp_max = str(round((weather['main']['temp_max'] - kelvin), 2))
    img_code = weather["weather"][0]["icon"]


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

    #hilversum label maken
    hillabel = Label(stationframe, text='Welkom op '+stad+' Centraal!', font=('Sans', 20), bg='#FFC917')
    hillabel.grid(row=0, column=1, pady=20, padx=10)

    #tijd
    def time():
        string = strftime('%H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000, time)

    lbl = Label(stationframe, font=('Sans', 20, 'bold'), bg='#FFC917')
    time()
    lbl.grid(row=0, column=2, padx=10, sticky='E')

    # terugknop maken
    bckbutton = Button(stationframe, text='Terug', font=('Sans', 20), command=terug)
    bckbutton.grid(row=2, column=2, pady=10, padx=10, sticky='E')

    #berichten importeren
    

def terug():
    try:
        stationframe.destroy()
    except:
        pass
    mainframe()


def mainpage():
    #maken main window
    global root
    root = Tk()
    root.geometry('1920x1080')
    root.title('NS-Reviews')
    root.config(bg='#FFC917')
    root.attributes('-fullscreen', True)
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

    # maken title main
    mainlabel = Label(frame, text='Welkom bij NS!', font=('Sans', 20), bg='#FFC917')
    mainlabel.grid(row=0, column=1, pady=20, padx=10)
    mainsublabel = Label(frame, text='Selecteer het station waar u zich bevindt:', font=('Sans', 12), bg='#FFC917')
    mainsublabel.grid(row=1, column=1, pady=10, padx=10)

    #plaatsen foto's
    utrimg = Image.open("utrecht.jpg")
    amsimg = Image.open("amsterdam.jpg")
    hilimg = Image.open("hilversum.png")

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
    utrbtn.grid(row=3, column=0, padx=10, pady=10, sticky='WE')
    amsbtn.grid(row=3, column=1, padx=10, pady=10, sticky='WE')
    hilbtn.grid(row=3, column=2, padx=10, pady=10, sticky='WE')

    # tijd
    def time():
        string = strftime('%H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000, time)

    lbl = Label(frame, font=('Sans', 20, 'bold'), bg='#FFC917')
    time()
    lbl.grid(row=0, column=2, pady=10, padx=10, sticky='E')


    root.mainloop()

mainpage()