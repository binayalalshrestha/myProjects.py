from tkinter import *

def submit():
    print("The temperature is: "+ str(scale.get())+ " degrees C")

window = Tk()
window.title("Temperature!")

hotImage = PhotoImage(file='images\hot.png')
hotLabel = Label(image=hotImage)
hotLabel.pack()

scale = Scale(window,
    from_=100,
    to=0,
    length=600,
    orient=VERTICAL,    #orientation of scare
    font = ('Consolas',20),
    tickinterval = 10,  #adds numeric indicators for value
    showvalue = 0,   #hide current value
    resolution = 5, #increment of slider
    troughcolor='#69EAFF',
    fg='#FF1C00',
    bg='#111111'
    )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

coldImage = PhotoImage(file='images\cold.png')
coldLabel = Label(image=coldImage)
coldLabel.pack()

button = Button(window,text='submit',command=submit)
button.pack()

window.config(background="white")
window.mainloop()