from tkinter import *
number = 0
window = Tk()
window.geometry = ('500x500')
window.title('INC-DEC.exe')



def click1():
    global number
    number += 1
    label.config(text = number)


def click2():
     global number
     number -= 1
     label.config(text = number)
    
def click3():
    window.destroy()    

frame = Frame(window, height = 50)
label = Label(window, fg= 'blue', font = 500, bg = 'grey',width = 5, height = 5)
button1 = Button(text = '+', fg = 'red', command = click1,font = 500,width = 10)
button2 = Button(text = '-', fg = 'blue', command = click2,font = 500,width = 10)
button3 = Button(text = 'Close', fg = 'black', command = click3,font = 500,width = 10)


frame.pack()
label.pack()
button1.pack()
button2.pack()
button3.pack()


window.mainloop()