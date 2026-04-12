
#ESERCIZIO

class Canguro:

    def __init__(self, contenuto_tasca = None):

        if contenuto_tasca == None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = contenuto_tasca

    def intasca(self, oggetto):

        self.contenuto_tasca.append(oggetto)

    def __str__(self):

        return f"classe contente una lista sul contenuto della tasca. Contenuto: {self.contenuto_tasca}"
    
can = Canguro()
guro = Canguro()

can.intasca("siko")
#print(can)
#print(guro)

class Padre:

    def __init__(self, valore):
        self.valore = valore
    
    def output(self):
        return self.valore
    

class Figlio(Padre):

    pass

class Figlio2(Padre):

    def output(self):
        return self.valore*2
    
class Figlio3(Padre):

    def __init__(self, dato):
        #super().__init__()   
        self.dato = dato

    def met(self):

        return self.dato

Pietro = Figlio3(10)
#print(Pietro.output())
print(Pietro.met())

Giovanni = Figlio(10)
print(Giovanni.output())

Riccardo = Figlio2(10)
print(Riccardo.output())


#ESERCIZIO 2

class Veicolo:

    def __init__(self, modello, marca, anno, speed):

        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = speed

    def __str__(self):

        return f"""Modello: {self.modello}
Marca: {self.marca}
Anno: {self.anno}
Speed: {self.speed}"""
    
    def accellerare(self):
        
        self.speed += 5

    def frenare(self):
        
        if self.speed != 0:
            self.speed -= 5

    def get_speed(self):

        return self.speed
    
    
class Auto(Veicolo):

    def __init__(self, modello, marca, anno, speed, numero_porte):
        
        super().__init__(modello, marca, anno, speed)
        self.numero_porte = numero_porte

    def __str__(self):

        return f"""Modello: {self.modello}
Marca: {self.marca}
Anno: {self.anno}
Speed: {self.speed}
Numero di porte: {self.numero_porte}"""

class Moto(Veicolo):

    def __init__(self, modello, marca, anno, speed, tipo):
        
        super().__init__(modello, marca, anno, speed)
        self.tipo = tipo

    def __str__(self):

        return f"""Modello: {self.modello}
Marca: {self.marca}
Anno: {self.anno}
Speed: {self.speed}
Tipo: {self.tipo}"""


Chervolet = Auto("Chervolet", "Captiva", "2009", 20, 5)
#print(Chervolet)

Ducati = Moto("Ducati", "Leon", "2025", 300, "Sportiva")
#print(Ducati)


#ESERCIZIO 1

corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]

class Persona:

    def __init__(self, ruolo, nome, cognome):
        
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        
        print("Ciao sono", self.ruolo + ", ", self.nome, self.cognome)


class Studente(Persona):

    def __init__(self, nome, cognome, corso=None):

        super().__init__("Studente Units", nome, cognome)
        if corso == None:
            self.corso = []
        else:
            self.corso = corso

    def corsi(self):
        
        return self.corso  # è un attributo quindi lo posso chiamare direttamente!!

    def saluta(self):

        Persona.saluta(self) #####
        print('> Frequento i corsi: ', self.corso)

class Docente(Persona):

    lista_docenti = []

    def __init__(self, nome, cognome, corso=None):

        super().__init__("Docente UNITS", nome, cognome)
        if corso == None:
            self.corso_d = []
        else:
            self.corso_d = corso
        Docente.lista_docenti.append(self)

    @classmethod
    def torna_lista_docenti(cls):
        return Docente.lista_docenti
    
    def saluta(self):

        super().saluta() #####
        print("> Docente dei corsi: ", self.corso_d)

    def ok_per_studente(self, studente):

        for corso in studente.corso:
            if corso not in self.corso_d:
                return 0
        return 1
    

Mario = Studente("Mario", "Rossi", corsi)
Claudio = Docente("Claudio", "Russo", ["Italiano"])
Giovanni = Docente("Giovanni", "Gado", ["Programmazione", "Laboratorio", "Analisi", "Geometria"])
print(Claudio.ok_per_studente(Mario))



def esiste_docente(studente):

    for docente in Docente.lista_docenti:
        if docente.ok_per_studente(studente):
            return 1
    return 0

print(esiste_docente(Mario))

print(Docente.lista_docenti)
print(Docente.torna_lista_docenti())

#ESERCIZIO 4

class Poligono:

    def __init__(self, lati):
        
        self.lati = lati

    def __str__(self):

        return f'Sono un poligono con {self.lati}'
    
class Quadrilatero(Poligono):

    def __init__(self):
        super().__init__(4)
    
    def __str__(self):

        return f'Sono un quadrilatero'
    
class Rettangolo(Quadrilatero):

    def __init__(self, base, altezza):
        
        super().__init__(4)
        self.base = base
        self.altezza = altezza

    def __str__(self):
        
        return f"Sono un quadrilatero con base {self.base} e altezza {self.altezza}"
    
    def perimetro(self):

        return (self.base + self.altezza) * 2
    
    def area(self):

        return (self.base * self.altezza)
    
class Triangolo(Poligono):

    def __init__(self, lato1, lato2, lato3):
        
        super().__init__(3)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def __str__(self):
        
        return f"Sono un triangolo con lati: {self.lato1}, {self.lato2}, {self.lato3}"
    
    def perimetro(self):

        return self.lato1 + self.lato2 + self.lato3
    
    def is_equilatero(self):
        return (self.lato1 == self.lato2 == self.lato3)
    
Equilatero = Triangolo(10, 0, 10)
print(Equilatero.is_equilatero())