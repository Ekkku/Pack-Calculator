from tkinter import *

from mudelid.Asukoht import Asukoht
from mudelid.Lopp import Lopp
from mudelid.Retsept import Retsept
from mudelid.RetseptiMaterial import RetseptiMaterial
from mudelid.material import Material

root=Tk()


material_1=Material("Chopped Produce", 0)
material_2=Material("Trimmed Meat", 0)
material_3=Material("Ground Grain", 0)
material_4=Material("Dryed Flowers", 0)

materialid= {material_1, material_2, material_3, material_4}

retsepti_material_1 = RetseptiMaterial(material_1, 50)
retsepti_material_2 = RetseptiMaterial(material_2, 50)
retsepti_material_3 = RetseptiMaterial(material_3, 50)
retsepti_material_4 = RetseptiMaterial(material_4, 50)

retsepti_materialid = {retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4}


asukoht_1=Asukoht("Ahnimar")
asukohad = {asukoht_1}

retsept_1=Retsept(asukoht_1, "Ahnimar Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])

retseptid = {retsept_1}


lopp_1=Lopp("Solzreed", retsept_1, 23.4991, 0)

lopp = {lopp_1}

#***** Part 2 ******
instructions_1 = Label(root, text="Fill in the prices per material.", padx=30, pady=10)
instructions_1.grid(columnspan=2)

label_1 = Label(root, text=material_1.nimi)
label_1.grid(row = 1, column=0, padx=15)

label_2 = Label(root, text=material_2.nimi)
label_2.grid(row=2, column=0, padx=15)

label_3 = Label(root, text=material_3.nimi)
label_3.grid(row=3, column=0, padx=15)

label_4 = Label(root, text=material_4.nimi)
label_4.grid( row=4, column=0, padx=15)




def create_entry(material):
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
    entry = Entry(root, textvariable=sv)
    def callback(sv):
        material.hind = sv.get()
        print (material.nimi, material.hind)
    return entry

for mat in materialid:
    entry_1=create_entry(mat)
    entry_1.grid(column=1, padx=15)




#ei t00ta
#aa_icon = PhotoImage(file="download.png")
#lable = Label(root, image=aa_icon)
#label.pack()


root.mainloop()