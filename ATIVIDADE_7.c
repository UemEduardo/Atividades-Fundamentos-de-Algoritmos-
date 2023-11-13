// 7) Projete uma função que receba a altura (em metros) e o gênero de uma pessoa (‘M’ – para masculino e ‘F’ – para feminino) e calcule o peso ideal
// dessa pessoa,sabendo-se que o peso ideal segue as seguintes fórmulas:
// Para os homens: (72.7 * h) – 58 e Para as mulheres: (62.1 * h) – 44.7
 
// Analise:Projetar uma funçao que calcule o peso ideal para a pessoa

// Tipo de Dados:
// entrada com dois dados altura e genero, saida peso ideal para a pessoa

 double peso{
     char genero_p
     double altura_p
};

// Especificaçao:

  double peso(double altura_p,double genero_p)

 //Assinatura:
    double peso(double altura_p,double genero_p)
      double peso_ideal
      if (genero == M){
      peso_ideal = (72.7 * altura)-58;
      } else if (genero == F){
      peso_ideal = (62.1 * altura) - 44.7;
      }
      return peso;
    }

 //Proposito:
 //Calcular o peso ideal para pessoa dependendo do seu genero e altura
 //Exemplos:
   check_expect(peso(1.80, 'M'),72.86);
   check_expect(peso(1.76, 'F'),64.59);
   check_expect(peso(1.60, 'F'),54.66);
   check_expect(peso(1.71, 'M'),66.31);

*/


 #include <iostream>
 #include "bscpp.hpp"
 using namespace std;

 double peso(double altura_p, char genero_p){
     double peso_i
     if (genero_p == 'M'){
      peso_i = (72.7 * altura_p)-58;
     } else if (genero_p == 'F'){
      peso_i = (62.1 * altura_p) - 44.7;
     }
 return peso_i,
 }

 // Professora nao consegui usar a bibliotecxa pois esta dando erro, mas deixei os exemplos pois petrendo testar no computador do LIN

 exemplos {
   check_expect(peso(1.80, 'M'),72.86);
   check_expect(peso(1.76, 'F'),64.59);
   check_expect(peso(1.60, 'F'),54.66);
   check_expect(peso(1.71, 'M'),66.31);
}

int main (){
 run_tests ();
}