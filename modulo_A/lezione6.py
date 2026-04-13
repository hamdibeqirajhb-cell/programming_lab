val = "ciao"
val2 = "hello"
class Errori(Exception):
    pass

"""try:
    float(val)
    float(val2)
    print("Lo eseguo?")
except:
    raise NameError()
    print("non va)"""

for i in range(5):
    if i == 0:
        next
     #   print("Con il next printo")
     #   print("ha cambiato valore? ",i)
    else:
        pass
       # print(i)

for i in range(5):
    if i == 0:
        continue
      #  print("Con il continue non printo")
    else:
        pass
        #print(i)
    #print(i)


class CSVFile:

    def __init__(self, nome_file):

        self.name = nome_file
        
        if not isinstance(nome_file, str):
            raise TypeError("Il nome del file deve essere una stringa")
            
        try:
            with open(nome_file, 'r') as file:
                pass
        except:
            print("Il file che stai cercando di aprire non esiste")

        
    def get_data(self, start=None, end=None):
        
        #conto_lunghezza_righe
        with open(self.name, "r") as conta:
            k_righe = 0
            for riga in conta:
                k_righe += 1
        
        print(isinstance(start, int))
        print(isinstance(end, int))
        
        if start!=None or end!=None:
            
            if start!= None:
                if not isinstance(start, int):
                    raise TypeError("Hai messo valore non intero!") 
            else:
                start = 0   
            
            if end!=None:
                if not isinstance(end, int):
                    raise TypeError("Hai messo un valore non intero")
            else:
                end = k_righe-1
            
            
            if end!=None:
                if end > (k_righe):
                    raise Exception("End fuori range (> len(righe))")
                elif end < 0:
                    raise Exception("End fuori range (<0)")
                
            if start!=None:
                if start > (end):
                    raise Exception("Start fuori range (> end)",start, end)
                elif start < 0:
                    raise Exception("Start fuori range (< 0)")
                
        lista_dati = []

        my_file = open(self.name, 'r')
        
        for riga in my_file:
            x = (riga.split(",")) 
            for i in range(len(x)):    #bastava fare lo strip() su riga e poi lo split()
                x[i] = x[i].strip()
            
            lista_dati.append(x)
                
        my_file.close()

        return lista_dati[start:end]
    
CSV = CSVFile('shampoo_sales.csv')
#print(CSV.get_data(37))

#ESERCIZIO 2

class NumericalCSVFile(CSVFile):

    def __init__(self, nome_file):

        super().__init__(nome_file)

    def get_data(self, start = None, end = None):
    #def get_data(self, *arg1, **arg2):

        #lista_elementi = super().get_data(*arg1, **arg2)
        lista_elementi = super().get_data(start, end)
        lista_elementi_float = []
        
        for riga in lista_elementi:
            if riga == lista_elementi[0]:
                lista_elementi_float.append(riga)
            else:
                try:
                    data = riga[0]
                    val = float(riga[1])
                    lista_elementi_float.append([data, val])
                except ValueError as err:
                    print(f"ommessa la riga: {riga}, per impossibilità di conversione in float")
                except Exception as e:
                    print('errore è diverso: {}'.format(e))
        
        return lista_elementi_float
    
CSV_float = NumericalCSVFile('shampoo_sales.csv')
#print("Con float \n", CSV_float.get_data(37))

#ESERCIZIO 3

#ESERCIZIO 4

#ESERCIZIO 5
#def f(data_nascita): #04-01-2001

#ESERCIZIO 6

def num_intero():

    intero = input("Dammi un numero intero: ")

    ok = 0
    while (ok!=1):
        try:
            intero = int(intero)
            ok = 1
        except ValueError:
            print("non mi hai dato un intero")
            print("dammi un intero!")
            intero = input()

    return intero ** 2


print(num_intero())

#ESERCIZIO 7

def controlla_scelta(scelta):

    ok = 0 
    while (ok!=0):
        scelta = scelta.strip()
        try:
            scelta = int(scelta)
            if not (scelta == 1 or scelta == 2 or scelta == 3):
                scelta = input("Dammi o 1 o 2 o 3")
            else:
                ok = 1
        except:
            print("metti uno di quei valori!!")
            scelta = input()
    
    return scelta

def opzioni():

    scelta = input("1 o 2 o 3")

    scelta = controlla_scelta(scelta)

    while(scelta!=3):  
        if scelta == 1:
            x = int(input)
            y = int(input)
            print(x+y)
            scelta = input("1 o 2 o 3")
            scelta = controlla_scelta(scelta)
        elif scelta == 2:
            x = int(input)
            y = int(input)
            print(x-y)
            scelta = input("1 o 2 o 3")
            scelta = controlla_scelta(scelta)





    