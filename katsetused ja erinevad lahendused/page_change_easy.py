from tkinter import *


def page1():
    page2text.pack_forget()
    page1text.pack()

def page2():
    page1text.pack_forget()
    page2text.pack()

window = Tk()

page1btn = Button(window, text="Page 1", command=page1)
page2btn = Button(window, text="Page 2", command=page2)

page1text = Label(window, text="This is page 1")
page2text = Label(window, text="This is page 2")

text=Label(window, text="test")
text.pack()


page1btn.pack()
page2btn.pack()



window.mainloop()