# ATIVIDADE 1

# lista = []
# for i in range(5):
#    valor = int(input("Digite o valor do elemento {}: ".format(i + 1)))
#    lista.append(valor)

# print("A lista é:", lista)

#----------------------------------------------------------------
# ATIVIDADE 2

# lista = [1, 2, 3, 4, 5]
# valor = int(input('Qual seria o valor de procura: '))

# for indice, valor in enumerate(lista):
#   while indice <= 0:
#      print ("Valor invalido: ")
#      break
# print (f"O Indice é : {indice}, Já o valor seria: {valor} ")

#------------------------------------------------------------------
# ATIVIDADE 3

#lista_A = []

#for i in range(6):
#    valor = int(input("Escreva o valor  {}: ".format(i + 1)))    
#    lista_A.append(valor)

#soma = lista_A[0] + lista_A[1] + lista_A[5]
#print ("A soma dos indices 0, 1, 5 sao : ",soma)

#lista_A.insert(4,100)

#print ("Estes sao os numeros da lista ",lista_A)

#------------------------------------------------------------------
# ATIVIDADE 4

#lista = []

#for i in range(5):  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
#    valor = int(input("Digite o valor {} :2".format(i + 1)))
#    lista.append(valor)
    
#maior = max(lista)
#menor = min(lista)

#print ('O menor valor è ',menor)
#print ('O maior valor è ',maior)


#--------------------------------------------------------------------
# ATIVIDADE 5

#lista = [1,6,4,8,42,8]

#print ("Esta è a lista em ordem normal: ",lista)

#lista.reverse()

#print ("Ja este seria a lista em ordem contraria :",lista)


#----------------------------------------------------------------------
# ATIVIDADE 7

#pares = []
#impares = []
#soma_pares = 0
#quantidade_impares = 0

#for i in range(6):
#  numero = int(input("Qual seria o valor {}: ".format(i + 1)))

#  if numero % 2 == 0:
#     pares.append(numero)
     
#     soma_pares += numero 
  
#  else:   
#     impares.append(numero)

#quantidade_impares += 1 

#print ("Numeros pares : ",pares)
#print ("Soma pares: ",soma_pares)
#print ("Numeros impares: ",quantidade_impares)
#print ("quantidade impares: ",quantidade_impares )


#--------------------------------------------------------------------------
# ATIVIDADE 8

lista = []

for i in range(10):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
   valor = int(input("Digite o valor {} :".format(i + 1)))
      
   if valor in lista:
       print ("Este valor ja esta escrito")
       valor = int(input("Digite o valor {} :".format(i + 1)))      
       lista.append(valor)
      
print (lista)      
   


















