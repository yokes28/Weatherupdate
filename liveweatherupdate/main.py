
import tkinter
import json
import requests
from tkinter import *
from tkinter import messagebox



def tell_weather():
    api_key = "API KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get()
    complete_url = base_url + "appid =" + api_key+ "&q =" + city_name

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        description = data['weather']

        current_temperature = ({temperature})
        current_humidity = ({humidity})
        current_pressure = ({pressure})
        weather_description = ({[description]})

        temp_field.insert(20, str(current_temperature) + " Kelvin")
        atm_field.insert(15, str(current_pressure) + " hPa")
        humid_field.insert(20, str(current_humidity) + " %")
        desc_field.insert(15, str(weather_description))

    else:
        messagebox.showerror("Error", "City Not Found \n"
                                      "Please enter valid city name")

        city_field.delete(0, END)

def clear_all():

    city_field.delete(0, END)
    temp_field.delete(0, END)
    atm_field.delete(0, END)
    humid_field.delete(0, END)
    desc_field.delete(0, END)

    city_field.focus_set()

if __name__ == "__main__":
    #configuring the dialog box

    root = Tk()
    root.title('Olivegreen Creation')
    root.configure(background = 'white')
    root.geometry("450x200")

    #labeling the contents
    headlabel =Label(root, text = "*** LIVE WEATHER UPDATE ***",fg ='black',bg ='white')
    label1 = Label(root,text = 'City Name :', fg = 'black',bg = 'white')
    label2 = Label(root, text = 'Temperature :',fg='black',bg='white')
    label3 = Label(root,text = 'Humidity :',fg ='black',bg ='white')
    label4 = Label(root, text='Atm.Pressure :',fg='black',bg='white')
    label5 = Label(root,text=' Weather Status :',fg='black',bg='white')

    # assigning positions
    headlabel.grid(row=0,column=1)
    label1.grid(row=1,column=0,sticky ="E")
    label2.grid(row=3, column=0,sticky = "E")
    label3.grid(row=4, column=0,sticky ="E")
    label4.grid(row=5, column=0,sticky ="E")
    label5.grid(row=6, column=0,sticky = "E")

    #creating text entry box
    city_field = Entry(root)
    temp_field = Entry(root)
    atm_field = Entry(root)
    humid_field = Entry(root)
    desc_field = Entry(root)

    #displaying answers
    city_field.grid(row = 1,column = 1, ipadx = "100")
    temp_field.grid(row=3, column=1, ipadx="100")
    atm_field.grid(row=4, column=1, ipadx="100")
    humid_field.grid(row=5, column=1, ipadx="100")
    desc_field.grid(row=6, column=1, ipadx="100")

    #creatingbuttons
    button1 = Button(root,text ='Submit',bg = 'grey',fg ='black',command = tell_weather)
    button2 = Button(root,text ='clear',bg = 'grey',fg ='black',command = clear_all)

    #locate buttons
    button1.grid(row = 2,column = 1)
    button2.grid(row = 7,column = 1)

    root.mainloop()
















