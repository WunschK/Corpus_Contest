# Tutorial zur Nutzung der REST-Schnittstellen von wdb+ am Beispiel des Projekts Religiöse Friedenswahrung und Friedensstiftung in Europa


import requests as r

# Wie in Python üblich müssen zunächst die notwendigen Pakete installiert werden.
# Hier das Paket requests. Dieses Paket muss meist separat installiert werden.
# # Dieser Schritt wird nicht in diesem Tutorial behandelt! Genauere Informationen zum Installieren von Paketen findest du hier:https://packaging.python.org/tutorials/installing-packages/


# GLOBALE Variable URL festgelegt - Globale Variablen werden all-caps geschrieben. Diese vermeiden Wiederholungen im Code.
URL = "https://exist.ulb.tu-darmstadt.de:8443/exist/restxq/edoc"

# Mithilfe von requests führen wir einen get-request aus, der uns alle Einträge aus der collection unter der id "religionsfrieden" ausgibt

# die REST-Schnittstelle findet man unter {server-Adresse}/restxq/edoc - In unserem Fall also unter f"{URL}/restxq/edoc"
# Welche Möglichkeiten wdb+ bietet kann hier nachgelesen werden: https://github.com/dariok/wdbplus/wiki/REST-endpoints

# In unserem Fall benötigen wir die Collection unter religionsfrieden, sodass der Pfad um /collection/religionsfrieden.json ergänzt wird.
response = r.get(url=f"{URL}/collection/religionsfrieden.json")
# Die folgende Zeile ist nicht notwendig. Sie regelt das Error-Handling und ermöglicht leichteres Debugging.
response.raise_for_status()
# Diese Zeile speichert den Inhalt der response als Variable data
data = response.json()


# Hier könnte data ausgegeben werden. i.e. das dictionary, das aus den Einträgen '@id' und 'resources' besteht.
# print(data)



def get_all_texts ():
    for i in range(0, len(data['resources']) - 1):
        RESOURCES = f"{data['resources'][i]['@id']}"
        url = f"{URL}/resource/{RESOURCES}"
        # unter diesem Kommentar wird der Speicherpfad und die Benennung festgelegt. Wir haben uns für die Bennenung nach ID entschieden! Abgespeichert wird es im Ordner, in welchem main.py abgespeichert ist.
        file = r.get(url, allow_redirects=True)
        open(f"{RESOURCES}.xml", 'wb').write(file.content)
        i += 1


def get_a_single_text ():
    num = int(input(
        f"Welchen Text möchtest du herunterladen? Gib eine Position ein. \n Hier wird ausgeglichen, dass Python bei 0 zu zählen beginnt. "))
    url = f"{URL}/resource/{data['resources'][num - 1]['@id']}"
    file = r.get(url, allow_redirects=True)
    open(f"{data['resources'][num - 1]['@id']}.xml", 'wb').write(file.content)

# Um entweder alle oder einen Text herunterzuladen unten die Funktion auskommentieren.

# get_all_texts()
# get_a_single_text()
