#1) Escreva um programa que calcule a soma dos valores inteiros digitados 
#  pelo usuário até que ele digite o valor 0.

# EXERCICIO 1

lista = []

for i in range(9999999999999999999999999999999999999999999999999999999999999999999999999):
  valores = int(input("Adicione quanto valores voce quiser, para parar basta digita 0: "))
  lista.append(valores)
  if valores == 0:
    break
soma = sum(lista)

print ("A soma dos valores digitados anteriormente é de: ",soma)


#2) Dado n, imprimir os n primeiros naturais ímpares.

#EXERCICIO 2

numeros = int(input("Digite um valor: ")) 
for i in range(1, numeros + 1):
    if i % 2 != 0:
        print(i)



#3) Refaça os exercícios da lista 05 usando o comando for.

#EXERCICIO 3

# R= Os exercicios da lista passada ja estao todos resolvidos em for