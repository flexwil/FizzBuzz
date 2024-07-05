#age = int(input("Wie alt bist du? "))
#number = int(input("Wie viele Karten brauchst du? "))
#if age < 18:
#    print("Für ", number, "Tickets musst du ", 5 * number, "€ zahlen.")
#elif age >= 65:
#    print("Für ", number, "Tickets musst du ", 7.5 * number, "€ zahlen.")
#else:
#    print("Für ", number, "Tickets musst du ", 10 * number, "€ zahlen.")

#Leere Liste
leere_liste = []

# einkaufszettel = ["Banane", "Weintrauben", "Karotte", 22]
# print(einkaufszettel[2][3:], einkaufszettel[1][5], einkaufszettel[3])
# #fügt hinten ein Element hinzu
# einkaufszettel.append("Nüsse")
# print(einkaufszettel, ".append")
# #fügt ein Element an einem bestimmten Index hinzu
# einkaufszettel.insert(0, "Milch")
# print(einkaufszettel, ".insert")
# #löscht das erste Element das übereinstimmt
# einkaufszettel.remove("Weintrauben")
# print(einkaufszettel, ".remove")
# #löscht das letzte Element
# einkaufszettel.pop()
# print(einkaufszettel, ".pop")
# #löscht das Element mit bestimmten Index
# del einkaufszettel[3]
# print(einkaufszettel, "del ")

# print(len(einkaufszettel))
# print(min(einkaufszettel))
# print(max(einkaufszettel))

# liste = ["Banane", "Weintrauben", "Karotte"]
# print(liste)
# liste[1] = "Schokolade"
# print(liste)
# print(type(liste))
#
# liste_tup = ("Banane", "Weintrauben", "Karotte")
# print(type(liste_tup))

einkaufsliste = []
# Artikel hinzufügen
# Aktion-> hinzufügen, entfernen, anzeigen, beenden
menu = 0

while True:
    menu = input("1 = entfernen, 2 = anzeigen, 3 = beenden oder füge einen Artikel hinzu: ")
    if menu == "1":  # entfernen
        erase = input("Was möchtest du löschen? ")
        if erase in einkaufsliste:
            einkaufsliste.remove(erase)
            print("Der Artikel ", erase, "wurde gelöscht.")
        else:
            print(erase, " ist bisher nicht auf der Liste")

    elif menu == "2":  # anzeigen
        print("Deine Einkaufsliste: ", einkaufsliste)

    elif menu == "3":  # beenden
        break

    else:
        einkaufsliste.append(menu)
        print(menu, " wurde hinzugefügt.")