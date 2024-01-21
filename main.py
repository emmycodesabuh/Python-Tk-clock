 from tkinter import *
from time import strftime

root = Tk()

root.title("Clock")

def time():

	string = strftime('%I %M %p on %A, %B %e, %Y')
	Label.config(text = string)
	Label.after(1000, time)

Label = Label(root, font = ('Consolas', 5))

Label.pack(anchor = 'center')

time()
mainloop()
