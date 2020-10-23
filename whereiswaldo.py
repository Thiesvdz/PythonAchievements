import random
people = ["Jackson","Ray","Eric","Vaughn","Jesse","Herbert","Waldo","Robert", "Rodrigo","Elija","Sasha","Nathaniel","Ellie","Allison","Jeremiah", "Paula", "Alisha","Tory","Troy", "Faye"]
random.shuffle(people)

for x in people:
  if x == "Waldo":
     break

cijfer = people.index("Waldo")

print("Waldo zit op nummer:", cijfer + 1)

print(people)
