class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

    def saluta(self):
        print('Ciao, sono', self.nome, 'e studio', self.corso)

studente1 = Studente('Anna', 'Informatica')
studente1.saluta()
