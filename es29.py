print ("digita stop per terminare il ciclo e ricevere il risultato finale ")
lista_nomi_città = []
lista_esc_term = []
contatore = 0


escursione_termica = int(input("Definisci il massimo valore che vuoi prestabilire all' escursione termica "))
    
while True:

    nomi_città = input("inserire nome città ")
    
    if nomi_città == "stop" :
        break
    
    temp_max_2 = int(input("digitare la temperatura massima della città "))
    temp_min_2 = int(input("digitare la temperatura minima della città "))
    escursione_termica_2 = (temp_max_2 - temp_min_2)
    
    if escursione_termica < escursione_termica_2 :
        contatore += 1
    else:
        pass
    

    
    lista_nomi_città.append(nomi_città)
    lista_esc_term.append(escursione_termica_2)
   
    
print ("le città che hanno avuto un'escursione termica maggiore rispetto alla prefissata sono", contatore)
print("lista delle città:", lista_nomi_città)
print("escursioni termiche per ogni città:", lista_esc_term)