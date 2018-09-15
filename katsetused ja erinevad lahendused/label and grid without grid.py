from tkinter import *
import tkinter as tk

root=Tk()
vasak=Frame(root)
vasak.pack(side=LEFT)
parem=Frame(root)
parem.pack(side=RIGHT)


parem_pool=Label(parem, text="parem pool")
paremalumine=Label(parem, text="parem alumine")

vasak_pool=Label(vasak, text="vasak pool")
vasakalumine=Label(vasak, text="vasakalumine" )


parem_pool.pack()
vasak_pool.pack()
paremalumine.pack()
vasakalumine.pack()



root.mainloop()