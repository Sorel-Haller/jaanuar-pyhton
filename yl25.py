#Koosta dictionary vähemalt viie endale iseloomuliku tunnusega 
#(näiteks: eesnimi, perenimi, sünniaasta, elukoht, lemmik magustoit).
#Väljasta elukoht kahel erineval viisil 
# (kasutades get() meetodit ja mitte kasutades seda).
#Muuda magustoidu väärtust.
#Tee kordus üle dictionary ja väljasta kõik võtmed.
#Tee kordus üle dictionary ja väljasta kõik väärtused 
#(pööra tähelepanu sellele, et saab mitmel viisil, proovi erinevaid võimalusi).
#Kontrolli, kas isikukood on dictionary's olemas.
#Leia dictionary suurus (elementide arv).
#Lisa element enda pikkuse jaoks.
#Eemalda element sünniaasta (pane tähele, et saab mitut moodi).
#Pane tähele, et del võtmesõnaga on võimalik kogu dictionary kustutada.
#Saa aru ja katseta del võtmesõna ja clear meetodi erinevusest.
#Tutvu kõigi dictionary meetoditega.
#Läbi ülesanne juhendi lõpus.

d = {"first_name": "Sörel", "last_name": "Haller", "birth_year": "1999", "residence": "Saaremaa", "dessert": "ice cream"}

print(d["residence"])
print(d.get("residence"))

d["dessert"] = "sorbet"
print(d)

d.update(dessert="muffin")
print(d)

for key in d:
    print(key)

for value in d.values():
    print(value)

check = d.get("personification_code")
print(check)

if "personification_code" in d.keys():
    print(d.get("personification_code"))
else:
    print("none")

print(len([key for key in d]))

d["height"] = "158cm"
print(d)

val = d.pop("birth_year")
print(d)

# del d["birth_year"]
# print(d)

d.clear()
print(d)