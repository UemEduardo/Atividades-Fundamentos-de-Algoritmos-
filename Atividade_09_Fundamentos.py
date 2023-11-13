#1) Faça uma função que receba 3 números inteiros como parâmetro, representando horas,
#   minutos e segundos, e os converta em segundos.

horas = 56              #int(input('Digite um valor inteiro em horas(EX: 26h): '))
minutos = 256           #int(input('Digite um valor inteiro em minutos(EX: 106m): '))
segundos = 45684        #int(input('Digite um valor inteiro em segundos(EX: 4526s): '))
                        
                        # 1-hora = 60 minutos = 3600 segundos
                        # 1-minuto = 60 segundos 

converte_horas = horas * 3600
converte_minutos = minutos * 60
print (converte_horas,converte_minutos)
soma_convercoes = (segundos + converte_minutos + converte_horas) 
print(f'Este seria o valor total da converçao de horas,minutos em segundos, somados entre eles: ',soma_convercoes)


#2) Faça uma função que receba uma temperatura em graus Celsius e retorne-a convertida
#   em graus Fahrenheit. A fórmula de conversão é: F = C (9.0/5.0) + 32.0, sendo F a ∗
#   temperatura em Fahrenheit e C a temperatura em Celsius.

temperatura_c = 20

temperatura_f = temperatura_c * (9.0/5.0) + 32.0
print(f'Esta seria a temperatura {temperatura_c} convertida em Fahrenheit',temperatura_f)


#3) Faça uma função que receba dois números e retorne qual deles é o maior.


valor_1 = 20
valor_2 = 22

if valor_1 > valor_2:
  print('O primeiro valor é maior que o segundo')
else:
  print('O segundo valor é maior que o primeiro ')
  

#4) Faça uma função que receba a distância em Km e a quantidade de litros de gasolina
#   consumidos por um carro em um percurso, calcule o consumo em Km/l e escreva uma
#   mensagem de acordo com a tabela abaixo:


distancia = 250
litros_gasolinas = 15

consumo = distancia / litros_gasolinas
print(consumo)

if consumo <= 8:
  print('Venda o carro!')
elif consumo <= 14:
  print('Economico!')
elif consumo > 12:
  print('Super economico!')   
  
  
#5) Faça uma função chamada DesenhaLinha. Ele deve desenhar uma linha na tela usando
#   vários sı́mbolos de igual (Ex: ========). A função recebe por parâmetro quantos sinais
#   de igual serão mostrados.


def desenha_linha(quantidade_de_iguais):
  for i in range(quantidade_de_iguais):
    print("=", end='')
  print()
  

#6) Faça uma função que receba três números e retorne qual deles é o maior.


valor_1 = 20
valor_2 = 22
valor_3 = 25

if valor_1 > valor_2:
  print('O primeiro valor é maior que o segundo')
elif valor_2 > valor_3:
  print('O segundo valor é maior que o terceiro')
else:
  print('O segundo valor é menor que o terceiro')
  

#7) Escreva uma função para determinar a quantidade de números primos abaixo de N.


def numeros_primos_ate_n(n):
  numeros_primos = []
  n=10
  for i in range(2, n + 1):
    primo = True
    for a in range(2, int(i ** 0.5) + 1):
      if i % a == 0:
        primo = False
        break
    if primo:
      numeros_primos.append(i)
  return len(numeros_primos)