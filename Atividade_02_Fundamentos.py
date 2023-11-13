#1 Exercicio

a = 4
b = 10
c = 5.0
d = 1
f = 5

avaliacoes = (a == c), (a < b), (d > b), (c != f), (a == b), (c < d), (b > a), (c >= f), (f >= c), (c <= c), (c <= f)
    print("Valores das contas : ", avaliacoes)

   
    x = True
    y = False
    z = True
#2 Exercicio

avaliacao_2 = (x and x),(y and y),(not z),(not y),(not x),(x and y),(y and z),(x or z),(y or z),(z or x),(z or y),(z or z),(y or y)
    print("Esses sao os valores da avaliacao 2 :", avaliacao_2)


#3 Exercicio

salario = 1500 

    if salario <= 1200:
    print("Voce nao pagara impostos")
    else:
        print("Voce pagara impostos ")


#5 Exercicio

disciplina1 = float(input("Qual a sua nota na discilplina 1 : ))
disciplina2 = float(input("Qual a sua nota na discilplina 2 : ))
disciplina3 = float(input("Qual a sua nota na discilplina 3 : ))

    if discilplina1 >= 7 and disciplina2 >= and disciplina3 >=7:
        print ("Voce foi aprovdo parabens")
    else:
        print("Voce nao foi aprovado mas tudo bem =( ")
