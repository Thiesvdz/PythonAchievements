def FunctieA() :
    print("voer uit")
    print("cool")
    print("----------------------------")

def FunctieMetParameter(waarde) :
    print("De waarde is:", waarde)
    print("----------------------------")



def FunctieB(x, y) :
    print("X is", x, "en Y is", y)
    print("----------------------------")


def FunctieMetDefaultValue(DezeMoet, optioneel = "Hallo",nogEenOptioneel = "leuk") :
    print("bla", DezeMoet)
    print("bli", optioneel)
    print("poh",nogEenOptioneel)

def FuntieMetJallah(Lego) :
    print("Hey:",Lego)
    print("----------------------------")

FunctieA()

FunctieMetParameter("STUK TEKST")
FunctieMetParameter(True)

FunctieB(0,1)
FunctieB(y=True, x= "joe mama")

FunctieMetDefaultValue("a")
FunctieMetDefaultValue(True,False)
FunctieMetDefaultValue("Ja!, a", nogEenOptioneel="Wa zoep ie da")
FunctieMetDefaultValue(1, 2, 3)

FuntieMetJallah("Build the rescue helicopter")
