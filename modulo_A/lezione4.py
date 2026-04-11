#ESERCIZIO 1

import random

class Coin:

    def __init__(self):

        #faccia deve valere 0 'croce' o 1 'testa'
        self.faccia =   -1  #nessun lancio

    def lancio(self):

        self.faccia = random.randint(0,1)

    def risultato(self):

        return self.faccia


moneta = Coin()
#print(moneta.risultato())
moneta.lancio()
#print(moneta.risultato())


#Esercizio 1

class Veicolo:

    def __init__(self, modello, marca, anno, speed = 0):

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
    
Toyota = Veicolo('Yaris', 'Toyota', 2024)
#print(Toyota)
#print(Toyota.get_speed())
Toyota.accellerare()
Toyota.accellerare()
#print(Toyota.get_speed())
Toyota.frenare()
#print(Toyota.get_speed())
Toyota.frenare()
Toyota.frenare()
Toyota.frenare()
#print(Toyota.get_speed())


#ESERCIZIO 2

class CSV:

    def __init__(self, nome_file):

        self.name = nome_file

    def get_data(self):
        
        lista_dati = []

        my_file = open(self.name, 'r')
        
        for riga in my_file:
            x = (riga.split(",")) 
            for i in range(len(x)):    #bastava fare lo strip() su riga e poi lo split()
                x[i] = x[i].strip()
            
            lista_dati.append(x)
                
        my_file.close()

        return lista_dati
    
CSVFile = CSV('shampoo_sales.csv')

print(CSVFile.get_data())


    