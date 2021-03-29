from tkinter import *
from tkinter.ttk import *


def move():
	print('moving...')
	print('moving...')


root = Tk()
f = open("Names.txt", encoding='utf-8-sig')

people = f.read().split('\n')
print(people)

root.title("First_Window")
frame = Frame(root)
frame.pack()

for person in people:
	label = Label(frame, text=person).pack()
	up = Button(frame, text="UP", command=move).pack()
	down = Button(frame, text="DOWN", command=move).pack()


root.mainloop()
