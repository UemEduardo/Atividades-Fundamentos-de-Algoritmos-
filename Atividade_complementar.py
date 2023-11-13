import math

def calcular_pi_termos(n_termos):
    pi = 0
    for i in range(n_termos):
        pi += ((-1)**i) * (4 / (2*i + 1))
    return pi

def calcular_pi_precisao(precisao):
    pi = 0
    i = 0
    while abs(pi - math.pi) > 10**(-precisao):
        pi += ((-1)**i) * (4 / (2*i + 1))
        i += 1
    return round(pi, precisao)

def main():
  
    print("Calculo dovalor de π, usando serie numérica inifinita")
    print()
    print("Escolha uma opção:")
    print("1. Calcular π para um dado número de termos.")
    print("2. Calcular π com a precisão desejada.")
    opcao = int(input("Opção (1 ou 2): "))  
    if opcao == 1:
        n_termos = int(input("Informe o numero de elementos (N): "))
        pi_calculado = calcular_pi_termos(n_termos)
        print(f"Valor aproximado de π para {n_termos} elementos: {pi_calculado}")
    elif opcao == 2:
        precisao = int(input("Digite quantas casas decimais deseja de precisão (entre 1 e 5): "))
        pi_calculado = calcular_pi_precisao(precisao)
        print(f"Foram gerados 999 elementos para obter a precisao de {precisao} casas decimais")
        print(f"Valor aproximado de π: {pi_calculado}")
    else:
        print("Opção inválida. Por favor, digite 1 ou 2.")
main()