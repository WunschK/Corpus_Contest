#Tutorial zur Nutzung der REST-Schnittstellen von wdb+ am Beispiel des Projekts Religiöse Friedenswahrung und Friedensstiftung in Europa

#imports
import requests as r

response = r.get(url="https://exist.ulb.tu-darmstadt.de:8443/exist/restxq/edoc/collection/religionsfrieden.json")
response.raise_for_status()
data = response.json()

print(data)