# EXERCICIO 1

vel = float(input("Qual a velocidade seria a sua velocidade? "))
if vel > 80:
   multa = (vel - 80) * 5
    print("Voce sera multado por ultrapassar o limite de velocidade, este sera o valor da multa: ", multa )
else:
    print("Voce nao sera multado")




# EXERCICIO 2

salario = float(input('Digite o seu salario: '))

if salario > 1250:
    superior = salario + (salario * 10 / 100)
    print ('Você teve um aumento de 10%. Novo Salario R$ ', superior )

elif salario <= 1250:
    inferior = salario + (salario * 15 / 100)
print ('Você teve um aumento de 15%. Novo Salario R$ ', inferior)




# EXERCICIO 3

distancia = float(input('Qual ser a distancia que deja percorrer em km ?'))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"ste sera o seu valor a pagar na passagem",preco)




# EXERCICIO 4

kwh = float(input("Qual é a quantidade de kWh que voce consome: "))
instalacao = input("Qual é seu tipo de instalaçao R=Residencia I=Industria C=Comercio: ")

if instalacao == "R":
    if kwh <= 500:
        preco = kwh * 0.40
    else:
        preco = kwh * 0.65
        print("O preco da sua conta sera de : ",preco)
elif instalacao == "C":
    if kwh <= 1000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
else:
    if kwh <= 5000:
        preco = kwh * 0.55
    else:
        preco = kwh * 0.60
print (f"Este sera o valor que voce ira para na sua conta de energia: ", preco)

        


    







