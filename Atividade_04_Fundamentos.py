# 1) Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O
# programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.

# Atividade 1
# x = 10
# while x >= 1:
#    print(x)
#    x = x - 1
# print ("FOGOOOOOO!!!")


# Atividade 2

# deposito = float(input("Qual o valor do Depósito : "))
# taxa = float(input("Qual seria a taxa de juros : "))
# mes = 1
# saldo = deposito

# while mês <= 24:
#    saldo = saldo + (saldo * (taxa / 100))
#    print(f"Saldo do mês é de R$",saldo)
#    mes = mes + 1

# juros_total = saldo - deposito
# print ("Este é o valor de juros ", juros_total)


# Atividade 03

#contador = 0
#n = 0

#while True:
#    numeros = int(
#        input(
#            "Digite um número, caso nao queira colocar mnais nenhum numero escreva 0: "
#        )
#    )
#    if numeros == 0:
#        break
#    contador = contador + 1
#    n = n + numeros
#media = n / contador

#print("Voce digitou", contador)
#print("O valo da media seria", media)
#print("Esta seria a soma de todos os numeros", n)



#ATIVIDADE 04

#apagar = 0
#while True:
#        codigo = int(input('Qual seria o codigo do produro, digite (0) para sair  : '))
#        preco = 0
#        if codigo == 0:
#           break 
#        elif codigo == 1:
#              preco = 0.50
#        elif codigo == 2:
#              preco = 1.00
#        elif codigo == 3:
#              preco = 4.00
#        elif codigo == 5:
#              preco = 7.00
#        elif codigo == 9:
#              preco = 8.00 
#        else:
#              print('Codigo invalido')
#        if preco != 0:  
#              quantidade = int(input('Qual seria a quantidade : '))
#              apagar = apagar + (preco * quantidade)

#print ('Total a pagar : R$ ', apagar)


#ATIVIDADE 07

n = int(input('Digite um numero : '))
b = 2
    
while (n - (b * b)) > 0.00001: 
    p = (b + (n / b)) / 2    
    b = p
print (p)