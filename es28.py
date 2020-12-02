#es28

#tasto per uscire dal ciclo di domande
print("Quando desidera che il ciclo termini, scriva: stop ")

#lista dei valori del lancio dei vari studenti
list_val = []

while True:
    
    nome_studente = input("inserire nome studente ")
    
    if nome_studente  == ("stop") :
        break
    else:
        pass
    
    valore_lancio = int(input("inserire valore lancio dello studente "))
    
    list_val.append(valore_lancio)

print("il valore più alto registrato oggi è..." )
print(max(list_val)) #stampa il valore massimo della lista
