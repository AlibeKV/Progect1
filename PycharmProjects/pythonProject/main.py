
import tkinter
from tkinter import ttk,messagebox
window = tkinter.Tk()
window.geometry('5000x5000')
window.config(bg='white')
def who_win():
 b = num1['text']
 c = num2['text']
 d= num3['text']
 ab = num4['text']
 cd = num5['text']
 gh = num6['text']
 ba = num7['text']
 ca = num8['text']
 ac = num9['text']
 if b==c==d=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if ab==cd==gh=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if ba==ca==ac=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if b==cd==ac=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if d==cd==ba=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if b==ab==ba=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if d==gh==ac=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if ab==cd==gh=='X':
  a = tkinter.Label(text='Winner X',bg='orange',fg='yellow')
  a.place(x=450,y=500)


 if b==c==d=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if ab==cd==gh=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if ba==ca==ac=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if b==cd==ac=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if d==cd==ba=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if b==ab==ba=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if d==gh==ac=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
 if ab==cd==gh=='O':
  a = tkinter.Label(text='Winner O',bg='orange',fg='yellow')
  a.place(x=450,y=500)
def restart():
 b = num1['text'] = ''
 c = num2['text']= ''
 d= num3['text']= ''
 ab = num4['text']= ''
 cd = num5['text']= ''
 gh = num6['text']= ''
 ba = num7['text']= ''
 ca = num8['text']= ''
 ac = num9['text']= ''
who_win=tkinter.Button(text='Who win?',command=who_win)
who_win.place(x=500,y=300)
result=tkinter.Button(text='result',command=restart)
result.place(x=500,y=400)
r_var = tkinter.BooleanVar()
r_var.set(1)
x = ttk.Radiobutton(text='X',variable=r_var,value=1)
x.place(x=100,y=300)
o = ttk.Radiobutton(text='O',variable=r_var,value=0)
o.place(x=300,y=300)
num1= tkinter.Button(
    width=3,
    height=3,
    command=lambda : num1.config(text='X') if r_var.get() == True else num1.config(text='O')
    )
num1.place(x=200,y=690)
num2= tkinter.Button(
    width=3,
    height=3,
    command=lambda : num2.config(text='X') if r_var.get() == True else num2.config(text='O')
    )
num2.place(x=420,y=690)
num3 = tkinter.Button(
    width=3,
    height=3,
    command=lambda : num3.config(text='X') if r_var.get() == True else num3.config(text='O')
    )
num3.place(x=640,y=690)
num4= tkinter.Button(
    width=3,
    height=3,
    command=lambda : num4.config(text='X') if r_var.get() == True else num4.config(text='O')
    )
num4.place(x=200,y=940)
num5 = tkinter.Button(
    width=3,
    height=3,
    command=lambda : num5.config(text='X') if r_var.get() == True else num5.config(text='O')
    )
num5.place(x=420,y=940)
num6= tkinter.Button(
    width=3,
    height=3,
    command=lambda : num6.config(text='X') if r_var.get() == True else num6.config(text='O')
    )
num6.place(x=640,y=940)
num7 = tkinter.Button(
    width=3,
    height=3,
    command=lambda : num7.config(text='X') if r_var.get() == True else num7.config(text='O')
    )
num7.place(x=200,y=1190)
num8 = tkinter.Button(
    width=3,
    height=3,

command=lambda : num8.config(text='X') if r_var.get() == True else num8.config(text='O')
    )
num8.place(x=420,y=1190)
num9 = tkinter.Button(
    width=3,
    height=3,
    command=lambda : num9.config(text='X') if r_var.get() == True else num9.config(text='O')
    )
num9.place(x=640,y=1190)
window.mainloop()