import sys
import time

def callMe(naam, werknummer):
    print("?: Hey Peter")
    time.sleep(2)
    print("Peter: Met wie bel ik?")
    time.sleep(2)
    print(naam,": Ik ben "+ naam)
    time.sleep(1)
    print("Peter:Hoi "+ naam+ ", Hoe gaat het?")
    time.sleep(3)
    print(naam,": Met mij gaat het goed hoor, met jou?")
    time.sleep(2)
    print("Peter: Met mij ook hoor.")
    time.sleep(3)
    print(naam,"Gaan we nog luchen morgen?")
    time.sleep(1)
    print("Peter: Ja komt goed bel me maar op mijn werknummer,"+werknummer)
    time.sleep(2)
    print(naam,":Toppie, dan zie ik je morgen")
    time.sleep(1)
    print("Peter:Tot morgen")
    time.sleep(1)
callMe(sys.argv[1], sys.argv[2])

def getal(6):

getal()
