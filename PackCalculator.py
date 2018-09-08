from tkinter import *

from mudelid.Asukoht import Asukoht
from mudelid.Retsept import Retsept
from mudelid.RetseptiMaterial import RetseptiMaterial
from mudelid.material import Material

root=Tk()


material_1=Material("Chopped Produce", 0)
material_2=Material("Trimmed Meat", 0)
material_3=Material("Ground Grain", 0)
material_4=Material("Dryed Flowers", 0)


retsepti_material_1 = RetseptiMaterial(material_1, 50)
retsepti_material_2 = RetseptiMaterial(material_2, 50)
retsepti_material_3 = RetseptiMaterial(material_3, 50)
retsepti_material_4 = RetseptiMaterial(material_4, 50)


asukoht_1=Asukoht("Ahnimar")


retsept_1=Retsept(asukoht_1, "Ahnimar Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])


#***** Graphic ******
instructions_1 = Label(root, text="Fill in the prices per material.", padx=30, pady=10)
instructions_1.pack(side=TOP)

label_1 = Label(root, text=material_1.nimi)
label_1.pack(side=LEFT, padx=15)

label_2 = Label(root, text=material_2.nimi)
label_2.pack(side=LEFT, padx=15)

label_3 = Label(root, text=material_3.nimi)
label_3.pack(side=LEFT, padx=15)

label_4 = Label(root, text=material_4.nimi)
label_4.pack(side=LEFT, padx=15)




def create_entry(material):
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
    entry = Entry(root, textvariable=sv)
    def callback(sv):
        material.hind = sv.get()
        print (material.nimi, material.hind)
    return entry

entry_1=create_entry(material_1)
entry_1.pack(side=RIGHT, padx=15)

entry_2=create_entry(material_2)
entry_2.pack(side=RIGHT, padx=15)

entry_3=create_entry(material_3)
entry_3.pack(side=RIGHT, padx=15)

entry_4=create_entry(material_4)
entry_4.pack(side=RIGHT, padx=15)


#ei t00ta
#aa_icon = PhotoImage(file="download.png")
#lable = Label(root, image=aa_icon)
#label.pack()


root.mainloop()