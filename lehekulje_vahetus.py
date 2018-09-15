from Mälu import *



def pageButton(first_page):
    def page2():
        # for label in labels:
        first_page.pack_forget()
        # page1text.pack_forget()
        infotext = Label(first_page, text="This is page 2")
        infotext.pack()

    page_button = Button(first_page, text="Maerials", command=page2)
    # = Button(first_page, text="Show my best pack options", command=page2)
    page_button.pack(side=RIGHT)


#entry tegemine
def create_entry(material, hindadelist):
    sv = StringVar()
    sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
    entry = Entry(hindadelist, textvariable=sv)
    def callback(sv):
        material.hind = sv.get()
        print (material.nimi, material.hind)
    return entry




