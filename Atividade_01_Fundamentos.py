
#Atividade 1


valor = input ("digite um valor :")
valor = int(valor)
milimetros = valor * 1000
print("O valor em milimeotros é: ", milimetros)

#Atividade 2


dia = input('Digite uma quantidade de dias: ')
horas = input("Digite um valor em horas: ")
minutos = input('Digite um valor em minutos: ')
segundos= input('Digite um valor em segundos:  ')

dia = float(dia)
horas = float(horas)
minutos = float(minutos)
segundos = float(segundos)

soma_total = (dia * 24 * 3600 + horas * 3600 + minutos * 60 + segundos)

print('Estee seria o todos os valores conertido em segundos: ', soma_total )



#Atividade 3


salario = input('Digite seu salario: ')
porcentagem = input('Quantos porcentos aumentou: ')

salario = float(salario)
porcentagem = float(porcentagem)
novo_salario = (salario * porcentagem / 100)

print('Valor do salario reajustado: ', salario + novo_salario)



#Atividade 4


p_mercadoria = input('Qual o preço da mercadoria: ')
porcentagem = input('Qual a porcentagem de desconto: ')

p_mercadoria = float(p_mercadoria)
porcentagem = float(porcentagem)

valor_desconto = (p_mercadoria * porcentagem) / 100
preco_a_pagar = (p_mercadoria - valor_desconto)

print('Este seia o valor do desconto:', valor_desconto)
print('Já este seria o valor que sera pago na mercadoria: ', preco_a_pagar)



#Atividade 5


distancia = input('Qual a distancia a ser percorrida em km: ')
velocidade = input('Qual a velocidade media da viagem em km/h: ')

distancia = float(distancia)
velocidade = float(velocidade)

tempo_gasto = ( distancia / velocidade)

print('O tempo a ser gasto em horas é de : ', tempo_gasto)



#Atividade 6


temperatura = input('Escreve uma temperatura em grau Celsius: ')

temperatura = int(temperatura)

converter = (9 * temperatura / 5) + 32

print('Esta é a temperatura em Fahrenheit: ', converter)



#Atividade 7


quilometros = input('Diga a qauntidade de km percorridos: ')
dias_alugados = input('Quantos dias o carro foi alugado: ')

quilometros = float(quilometros)
dias_alugados = float(dias_alugados)

custo_dist = (0,15 * quilometros)
custo_dia = (60 * dias_alugados)
custo_total = custo_dia + custo_dist

print('Este seria o custo do carro alugado: ', custo_total)