import tkinter as tk
from PIL import Image, ImageTk
import string

def button_press(symbol):
    entry.insert("end", symbol)

def clear():
    entry.delete(0, "end")

def clear_the_last_symbol():
    entry.delete(len(entry.get())-1)

def multiplie():
    x = int(entry.get())
    res = x*x
    entry.delete(0, "end")
    entry.insert(0, str(res))

def equal():
    pass

def operation():
    text = entry.get()
    result = 0
    if '+' in text:
        splitted_text = text.split('+')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first + second
    elif '-' in text:
        splitted_text = text.split('-')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first - second
    elif '*' in text:
        splitted_text = text.split('*')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first * second
    elif '/' in text:
        splitted_text = text.split('/')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first / second
    elif '%' in text:
        splitted_text = text.split('%')
        first = float(splitted_text[0])
        second = float(splitted_text[1])
        result = first % second
        
    clear()
    entry.insert(0, result)

win = tk.Tk()
win.title('Calculator v1.0')
win.geometry('400x600+100+100')
win.resizable(False, False)

win.iconbitmap('img\icon.png')

win.image = ImageTk.PhotoImage(file='bg_image.png')
bg_image = tk.Label(win, image=win.image, bd=0, highlightthickness=0)
bg_image.grid(row=0, column=0)

title = tk.Canvas(win, width=399, height=40, bd=1, highlightthickness=1, highlightbackground="black", bg='#34819a')
title.create_text(10, 10, anchor='nw', text="Python calculator v1.0", fill="black", font=('Helvetica 15 bold'))
title.place(x=0, y=0)

entry = tk.Entry(win, font=("arial", 24), fg="#0c1b24", bg="#c3c3c3")
# entry.grid(row=0, column=0, columnspan=4)
entry.place(x=11, y=57, width=378, height=45)

x2 = Image.open('img\img_of_x2.png')
x2_img=x2.resize((1, 1))
x2_image = ImageTk.PhotoImage(x2)

tk.Button(text="%", bd=5, bg='#a1afb3', command=lambda: button_press('%')).place(x=28, y=185, width=50, height=50)
tk.Button(text="CE", bd=5, bg='#a1afb3', command=lambda: clear()).place(x=98, y=185, width=50, height=50)
tk.Button(text="C", bd=5, bg='#a1afb3', command=lambda: clear()).place(x=168, y=185, width=50, height=50)
tk.Button(text="DEL", bd=5, bg='#a1afb3', command=lambda: clear_the_last_symbol()).place(x=238, y=185, width=50, height=50)
tk.Button(text="", bd=5, bg='#a1afb3', command=lambda: button_press()).place(x=308, y=185, width=50, height=50)
tk.Button(text="1/x", bd=5, bg='#a1afb3', command=lambda: button_press("doesn't work")).place(x=28, y=245, width=50, height=50)
tk.Button(image=x2_image, bd=5, bg='#a1afb3', command=lambda: multiplie()).place(x=98, y=245, width=50, height=50)
tk.Button(text="x^0.5", bd=5, bg='#a1afb3', command=lambda: button_press("doesn't work")).place(x=168, y=245, width=50, height=50)
tk.Button(text="/", bd=5, bg='#a1afb3', command=lambda: button_press('/')).place(x=238, y=245, width=50, height=50)
tk.Button(text="", bd=5, bg='#a1afb3', command=lambda: button_press('')).place(x=308, y=245, width=50, height=50)
tk.Button(text="7", bd=5, bg='#c3d2d6', command=lambda: button_press(7)).place(x=28, y=305, width=50, height=50)
tk.Button(text="8", bd=5, bg='#c3d2d6', command=lambda: button_press(8)).place(x=98, y=305, width=50, height=50)
tk.Button(text="9", bd=5, bg='#c3d2d6', command=lambda: button_press(9)).place(x=168, y=305, width=50, height=50)
tk.Button(text="*", bd=5, bg='#a1afb3', command=lambda: button_press('*')).place(x=238, y=305, width=50, height=50)
tk.Button(text="", bd=5, bg='#a1afb3', command=lambda: button_press()).place(x=308, y=305, width=50, height=50)
tk.Button(text="4", bd=5, bg='#c3d2d6', command=lambda: button_press(4)).place(x=28,  y=365, width=50, height=50)
tk.Button(text="5", bd=5, bg='#c3d2d6', command=lambda: button_press(5)).place(x=98, y=365, width=50, height=50)
tk.Button(text="6", bd=5, bg='#c3d2d6', command=lambda: button_press(6)).place(x=168, y=365, width=50, height=50)
tk.Button(text="-", bd=5, bg='#a1afb3', command=lambda: button_press('-')).place(x=238, y=365, width=50, height=50)
tk.Button(text="", bd=5, bg='#a1afb3', command=lambda: button_press()).place(x=308, y=365, width=50, height=50)
tk.Button(text="1", bd=5, bg='#c3d2d6', command=lambda: button_press(1)).place(x=28,  y=425, width=50, height=50)
tk.Button(text="2", bd=5, bg='#c3d2d6', command=lambda: button_press(2)).place(x=98, y=425, width=50, height=50)
tk.Button(text="3", bd=5, bg='#c3d2d6', command=lambda: button_press(3)).place(x=168, y=425, width=50, height=50)
tk.Button(text="+", bd=5, bg='#a1afb3', command=lambda: button_press('+')).place(x=238, y=425, width=50, height=50)
tk.Button(text="", bd=5, bg='#a1afb3', command=lambda: button_press()).place(x=308, y=425, width=50, height=50)
tk.Button(text="+/-", bd=5, bg='#a1afb3', command=lambda: button_press("doesn't work")).place(x=28, y=485, width=50, height=50)
tk.Button(text="0", bd=5, bg='#c3d2d6', command=lambda: button_press(0)).place(x=98, y=485, width=50, height=50)
tk.Button(text=".", bd=5, bg='#a1afb3', command=lambda: button_press('.')).place(x=168, y=485, width=50, height=50)
tk.Button(text="=", bd=5, bg='#6a7375', command=lambda: operation()).place(x=238, y=485, width=120, height=50)

def new_win():
    import time

    xVelocity = 1
    yVelocity = 1
        
    info_win = tk.Tk()
    info_win.title('Information')
    info_win.geometry('400x400+500+200')
    info_win.resizable(False,False)
        
    #making canvas
    canvas = tk.Canvas(info_win, width=400, height=400, bg='#80bed2', bd=0, highlightthickness=0)
    canvas.pack()
    ball1 = canvas.create_oval(10, 10, 30, 30, fill='red')
    ball2 = canvas.create_oval(390, 10, 370, 30, fill='red')
    ball3 = canvas.create_oval(150, 350, 170, 330, fill='red')

    while True:
        coordinates = canvas.coords(ball1)
        print(coordinates)
        canvas.move(ball1, xVelocity, yVelocity)
        canvas.move(ball2, xVelocity, yVelocity)
        canvas.move(ball3, xVelocity, yVelocity)
        info_win.update()
        time.sleep(0.01)

    info_win.mainloop()


more_info_img = ImageTk.PhotoImage(file='img\info_img.png')
more_info = tk.Button(win, image=more_info_img, command= lambda: new_win())
more_info["border"] = "0"
more_info.place(x=365, y=10, width=25, height=25)

win.mainloop()