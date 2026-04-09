#### prima parte ####

#Esercizio 1
def somma_lista(lista):
    return sum(lista)

lista = [1,2,3,4]
#print(somma_lista(lista))

#Esercizio 2
def is_palindromo(stringa):
    stringa = stringa.lower()
    for i in range(len(stringa)//2):
        if stringa[i] != stringa[len(stringa)-1-i]:
            return False
    return True

#print(is_palindromo("Aiia"))

#Esercizio 3
def scambia(lista_A, A_i, A_j):
    tmp = lista_A[A_i]
    lista_A[A_i] = lista_A[A_j]
    lista_A[A_j] = tmp
    return lista_A

#print(scambia(["a","b","c"], 0, 1))

#Esercizio 4
def comune(lista_A, lista_B):
    for elem in lista_A:
        if elem in lista_B:
            return True
    return False

#print(comune([1,2,3],[0,4]))

#Esercizio 5
def trascrivo(lista):
    diz = {0:"zero", 1:"uno", 2:"due", 3:"tre", 4:"quattro",
           5:"cinque", 6:"sei", 7:"sette", 8:"otto", 9:"nove"}
    lista_abc = []
    for elem in lista:
        lista_abc.append(diz[elem])
    return lista_abc

#print(trascrivo([1,2,3]))

#### seconda parte ####

#Esercizio 1
def conta_parole(lista):
    my_dict = dict()
    for parola in lista:
        if parola in my_dict:
            my_dict[parola] += 1
        else:
            my_dict[parola] = 1
    return my_dict

#print(conta_parole(["ciao", "come", "va", "va"]))

#Esercizio 2
def sum_sales(file):
    somma = 0
    values = []
    with open(file, "r") as my_file:
        print(my_file.readline())
        
        for line in my_file:
            print(line)
            riga = line.split(",")
            riga[1] = riga[1].strip()
            somma += float(riga[1])

            values.append(float(riga[1]))
    print(sum(values))
    return somma

#print(sum_sales("shampoo_sales.csv"))


#ESERCIZIO 3
def conta_parola(file, parola):
    k = 0
    with open(file, "r") as my_file:
        for riga in my_file:
            elementi = riga.split()
            for elem in elementi:
                if parola == elem:
                    k += 1
    return k

"""lista = [1,2]
lista2 = [3,4]

lista3 = lista + lista2
print(lista3)"""

#ESERCIZIO 4  (la punteggiatura attaccata alle parole non è rimossa)
def conteggio(file):
    my_dict = {}
    with open(file, "r") as mio_file:
        for riga in mio_file:
            elementi = riga.split()
            for elem in elementi:
                elem = elem.strip()
                if elem in my_dict:
                    my_dict[elem] += 1
                else:
                    my_dict[elem] = 1
    return my_dict

#print(conteggio("prova.txt"))

#ESERCIZIO 5
def unique_w(file):
    righe_file = []
    with open(file, "r") as f_lettura:
        for riga in f_lettura:
            if riga not in righe_file:
                righe_file.append(riga)
    with open("unique.txt", "w") as f_scrittura:
        for elem in righe_file:
            f_scrittura.write(elem)

unique_w("prova.txt")