
# Parte 1 - Variabili e tipi di dati
print("PARTE 1: Variabili e tipi di dati")
print("-" * 40)

titolo = "Il Signore degli Anelli"
copie = 5
prezzo_medio = 24.99
disponibile = True

print("Titolo:", titolo, "(tipo:", type(titolo).__name__ + ")")
print("Copie disponibili:", copie, "(tipo:", type(copie).__name__ + ")")
print("Prezzo medio:", prezzo_medio, "(tipo:", type(prezzo_medio).__name__ + ")")
print("Disponibile:", disponibile, "(tipo:", type(disponibile).__name__ + ")")


# Parte 2 - Strutture dati
print("\n\nPARTE 2: Strutture dati")
print("-" * 40)

lista_libri = ["Il Signore degli Anelli", "1984", "Il Piccolo Principe", 
               "Harry Potter e la Pietra Filosofale", "Don Chisciotte"]
print("Lista libri:", lista_libri)

dizionario_copie = {
    "Il Signore degli Anelli": 5,
    "1984": 3,
    "Il Piccolo Principe": 7,
    "Harry Potter e la Pietra Filosofale": 4,
    "Don Chisciotte": 2
}
print("\nDizionario copie:")
for titolo, num_copie in dizionario_copie.items():
    print(f"  {titolo}: {num_copie} copie")

utenti_registrati = {"Mario Rossi", "Giulia Bianchi", "Luca Verdi", 
                     "Anna Neri", "Paolo Gialli"}
print("\nUtenti registrati:", utenti_registrati)


# Parte 3 - Classi e OOP
print("\n\nPARTE 3: Classi e OOP")
print("-" * 40)

class Libro:
    def __init__(self, titolo, autore, anno, copie_disponibili):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili
    
    def info(self):
        return f"{self.titolo} di {self.autore} ({self.anno}) - Copie: {self.copie_disponibili}"

class Utente:
    def __init__(self, nome, eta, id_utente):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente
    
    def scheda(self):
        print(f"Nome: {self.nome}")
        print(f"Età: {self.eta}")
        print(f"ID: {self.id_utente}")

class Prestito:
    def __init__(self, utente, libro, giorni):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni
    
    def dettagli(self):
        print(f"Libro: {self.libro.titolo}")
        print(f"Autore: {self.libro.autore}")
        print(f"Utente: {self.utente.nome} (ID: {self.utente.id_utente})")
        print(f"Durata prestito: {self.giorni} giorni")

# test delle classi
print("\nTest classe Libro:")
libro_test = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 5)
print(libro_test.info())

print("\nTest classe Utente:")
utente_test = Utente("Mario Rossi", 35, "U001")
utente_test.scheda()


# Parte 4 - Funzionalità
print("\n\nPARTE 4: Funzionalità")
print("-" * 40)

prestiti = []

def presta_libro(utente, libro, giorni):
    if libro.copie_disponibili > 0:
        libro.copie_disponibili = libro.copie_disponibili - 1
        nuovo_prestito = Prestito(utente, libro, giorni)
        prestiti.append(nuovo_prestito)
        print(f"OK - Prestito effettuato per {utente.nome}")
        print(f"Copie rimaste: {libro.copie_disponibili}")
        return nuovo_prestito
    else:
        print(f"ERRORE - Nessuna copia disponibile di '{libro.titolo}'")
        return None

# creo i libri
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 5)
libro2 = Libro("1984", "George Orwell", 1949, 3)
libro3 = Libro("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943, 7)
libro4 = Libro("Harry Potter e la Pietra Filosofale", "J.K. Rowling", 1997, 4)
libro5 = Libro("Don Chisciotte", "Miguel de Cervantes", 1605, 2)

catalogo = [libro1, libro2, libro3, libro4, libro5]

# creo gli utenti
utente1 = Utente("Mario Rossi", 35, "U001")
utente2 = Utente("Giulia Bianchi", 28, "U002")
utente3 = Utente("Luca Verdi", 42, "U003")
utente4 = Utente("Anna Neri", 31, "U004")

# faccio 3 prestiti
print("\nPrestiti:")
presta_libro(utente1, libro1, 14)
print()
presta_libro(utente2, libro2, 21)
print()
presta_libro(utente3, libro3, 7)

# stampo copie aggiornate
print("\n\nCopie disponibili dopo i prestiti:")
print("-" * 40)
for libro in catalogo:
    print(libro.info())

# stampo dettagli prestiti
print("\n\nDettagli prestiti effettuati:")
print("-" * 40)
for i in range(len(prestiti)):
    print(f"\nPrestito {i+1}:")
    prestiti[i].dettagli()
