
studente = {
    "nome": "Luca",
    "età": 21,
    "corso": "Informatica"
}

print(studente)

studente["età"] = 22
print("Dopo la modifica dell'età:", studente)


studente["matricola"] = "A12345"
print("Dopo aver aggiunto la matricola:", studente)


valore_sconosciuto = studente.get("media", "Chiave non trovata")
print("Valore della chiave 'media':", valore_sconosciuto)


print("\nTutte le coppie chiave-valore:")
for chiave, valore in studente.items():
    print(chiave, ":", valore)
