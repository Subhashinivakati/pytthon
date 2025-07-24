'''
weather application project
-i just want to get current temperature,current pressure,current humidity,current wind
from tkinter import *
import requests
import json

root=Tk()
root.title('Weather app')

def get_data(root):
    city=user.get()
    print(city)
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid= bcaaf5f628463c81f367d16b6bf17902"
    resp=requests.get(api)
     #print(resp)
    if resp.status_code == 200:
        data=resp.json()
        temp=int(data['main']['temp']-273.15)
        print(temp)
        pressure=int(data['main']['pressure'])
        hum=int(data['main']['humidity'])
        condition=data['weather'][0]['main']
        wind=int(data['wind']['speed'])
        print(temp,pressure,hum,wind,condition)
        output="temperature:"+str(temp)+"°C"+"\n"+"pressure:"+str(pressure)+"hpa"+"\n"+"humidity:"+str(hum)+"%"+"\n"+"wind:"+str(wind)+"m/s"+"\n"+"condition:"+condition
        print(output)
        label.configure(text=output)

        
user=Entry(root,width=30,justify='center',font=('poppins',20,'bold'))
user.grid(row=0,column=0)
user.bind("<Return>",get_data)

label=Label(root,font=('poppins',20,'bold'))
label.grid(row=1,column=0)


root.mainloop()
'''

'''
weather application project
-i just want to get current temperature,current pressure,current humidity,current wind
'''
from tkinter import *
import requests
#import json

root=Tk()
root.title('Weather app')

def get_data(root):
    city=user.get()
    print(city)
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=bcaaf5f628463c81f367d16b6bf17902"
    resp=requests.get(api)
    #print(resp)
    if resp.status_code == 200:
        data=resp.json()
        temp=int(data['main']['temp']-273.15)
        #print(temp)
        pressure=int(data['main']['pressure'])
        hum=int(data['main']['humidity'])
        condition=data['weather'][0]['main']
        wind=int(data['wind']['speed'])
         #print(temp,pressure,hum,wind,condition)
        output="temperature:"+str(temp)+"°C"+"\n"+"pressure:"+str(pressure)+"hpa"+"\n"+"humidity:"+str(hum)+"%"+"\n"+"wind:"+str(wind)+"m/s"+"\n"+"condition:"+condition
        print(output)
        label.configure(text=output)

        
user=Entry(root,width=30,justify='center',font=('poppins',20,'bold'))
user.grid(row=0,column=0)
user.bind("<Return>",get_data)

label=Label(root,font=('poppins',20,'bold'))
label.grid(row=1,column=0)


root.mainloop()








