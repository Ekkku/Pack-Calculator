from lehekulje_vahetus import *
from Mälu import *

def main():
    first_page=Frame(root)
    first_page.pack()

    instructions_1 = Label(first_page, text="Fill in the prices per material.", padx=30, pady=10)
    instructions_1.pack()

    materialidelist=Frame(first_page)
    materialidelist.pack(side=LEFT)

    hindadelist=Frame(first_page)
    hindadelist.pack(side=RIGHT)



    for mate in materialid:
        label = Label(materialidelist, text=mate.nimi)
        label.pack(padx=20)




    for mat in materialid:
        entry_1=create_entry(mat, hindadelist)
        entry_1.pack(pady=0.6)

    pageButton(first_page)

    root.mainloop()

if __name__  == "__main__":
    main()