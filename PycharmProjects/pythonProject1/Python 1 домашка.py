from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry('300x300')
window.title("Регистрация")

label1=Label(text='Email Address')
label1.place(x=50,y=60)
entry1=Entry()
entry1.place(x=50,y=80)

label2=Label(text='Passworld')
label2.place(x=50,y=100)
entry2=Entry()
entry2.place(x=50,y=120)
button=Button(text='Login')
button.place(x=50,y=140)



window.mainloop()