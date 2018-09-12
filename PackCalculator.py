from tkinter import *

from mudelid.Asukoht import Asukoht
from mudelid.Lopp import Lopp
from mudelid.Retsept import Retsept
from mudelid.RetseptiMaterial import RetseptiMaterial
from mudelid.material import Material

root=Tk()

#storage

material_1=Material("Chopped Produce", 0)
material_2=Material("Trimmed Meat", 0)
material_3=Material("Ground Grain", 0)
material_4=Material("Dryed Flowers", 0)
material_5=Material("Grape", 0)
material_6=Material("Mushroom", 0)
material_7=Material("Gilda Star", 0.00001)
material_8=Material("Duck Down", 0)
material_9=Material("Barley", 0)
material_10=Material("Medicinal Powder", 0)
material_11=Material("Corn", 0)
material_12=Material("Rice", 0)
material_13=Material("Ground Spices", 0)
material_14=Material("Bay leaf", 0)
material_15=Material("Apple", 0)
material_16=Material("Narcissus", 0)
material_17=Material("Wool", 0)
material_18=Material("Orchard Puree", 0)
material_19=Material("Goose down", 0)
material_20=Material("Egg", 0)
material_21=Material("Yam", 0)
material_22=Material("Banana", 0)
material_23=Material("Olive", 0)
material_24=Material("Milk", 0)
material_25=Material("Cherry", 0)
material_26=Material("Avocado", 0)
material_27=Material("Rosemary", 0)
material_28=Material("Pomegranade", 0)


materialid= {material_1, material_2, material_3, material_4, material_5, material_6, material_7, material_8, material_9, material_10, material_11, material_12, material_13, material_14, material_15,
             material_16, material_17, material_18, material_19, material_20, material_21, material_22, material_23, material_24, material_25, material_26, material_27, material_28}

retsepti_material_1 = RetseptiMaterial(material_1, 50)
retsepti_material_2 = RetseptiMaterial(material_2, 50)
retsepti_material_3 = RetseptiMaterial(material_3, 50)
retsepti_material_4 = RetseptiMaterial(material_4, 50)

retsepti_materialid = {retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4}


asukoht_1=Asukoht("Ahnimar")
asukoht_2=Asukoht("Hellswamp")
asukoht_3=Asukoht("Halcyona")
asukoht_4=Asukoht("Sanddeep")
asukoht_5=Asukoht("Two Crown")
asukoht_6=Asukoht("Cinderstonr  Moor")
asukoht_7=Asukoht("Marianople")
asukoht_8=Asukoht("Dewstone Plains")
asukoht_9=Asukoht("White Arden")
asukoht_10=Asukoht("Aubre Cradle")
asukoht_11=Asukoht("Airain Rock")
asukoht_12=Asukoht("Gweonid Forest")
asukoht_13=Asukoht("Solzreed Peninsula")
asukoht_14=Asukoht("Lilyut Hills")
asukoht_15=Asukoht("Karkasse Ridgelands")


asukohad = {asukoht_1, asukoht_2, asukoht_3, asukoht_4, asukoht_5, asukoht_6, asukoht_7, asukoht_8, asukoht_9, asukoht_10, asukoht_11, asukoht_12,
            asukoht_13, asukoht_14, asukoht_15}

#igal kohal on oma ferilizer
retsept_1=Retsept(asukoht_1, "Ahnimar Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_2=Retsept(asukoht_2, "Hellswamp Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_3=Retsept(asukoht_3, "Halcyona Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_4=Retsept(asukoht_4, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_5=Retsept(asukoht_5, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_6=Retsept(asukoht_6, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_7=Retsept(asukoht_7, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_8=Retsept(asukoht_8, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_9=Retsept(asukoht_9, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_10=Retsept(asukoht_10, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_11=Retsept(asukoht_11, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_12=Retsept(asukoht_12, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_13=Retsept(asukoht_13, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_14=Retsept(asukoht_14, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])
retsept_15=Retsept(asukoht_15, "Dewstone Fertilizer", [retsepti_material_1, retsepti_material_2, retsepti_material_3, retsepti_material_4])






retseptid = {retsept_1}


lopp_1=Lopp("Solzreed", retsept_1, 23.4991, 0)

lopp = {lopp_1}

#***** 2. ******
instructions_1 = Label(root, text="Fill in the prices per material.", padx=30, pady=10)
instructions_1.pack(side=TOP)

first_frame=Frame(root)
first_frame.pack()



label_1 = Label(first_frame, text=material_1.nimi)
label_1.pack(side=LEFT, padx=15,anchor=W)

label_2 = Label(first_frame, text=material_2.nimi)
label_2.pack(side=LEFT, padx=15,anchor=W)

label_3 = Label(first_frame, text=material_3.nimi)
label_3.pack(side=LEFT, padx=15,anchor=W)

label_4 = Label(first_frame, text=material_4.nimi)
label_4.pack(side=LEFT, padx=15,anchor=W)

labels={label_1,label_2, label_3, label_4}

#labeli tegemine, ei toota
def create_label(material):
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
    label = Label(first_frame, textvariable=sv)
    def callback(sv):
        material.nimi = sv.get()
    return label

for mat in materialid:
    label_5=create_label(mat)
    label_5.pack( padx=15,anchor=W)

#entry tegemine
def create_entry(material):
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
    entry = Entry(first_frame, textvariable=sv)
    def callback(sv):
        material.hind = sv.get()
        print (material.nimi, material.hind)
    return entry

for mat in materialid:
    entry_1=create_entry(mat)
    entry_1.pack(side=RIGHT, padx=15,anchor=W)

entrys=[entry_1]

# ***** googlist, lehe keeramine****
# kergem versioon

def page1():
    for label in labels:
        label.pack()
    page2text.pack_forget()


def page2():
    for label in labels:
        label.pack_forget()
    # page1text.pack_forget()
    page2text.pack()
    for entry in entrys:
        entry.pack_forget()

page1btn = Button(first_frame, text="Maerials", command=page1)
page2btn = Button(first_frame, text="Show my best pack options", command=page2)
page2text = Label(first_frame, text="This is page 2")

page1btn.pack()
page2btn.pack()

# lehe keeramise lopp

#ei t00ta
#aa_icon = PhotoImage(file="download.png")
#lable = Label(root, image=aa_icon)
#label.pack()


root.mainloop()