//10) Projete uma função que receba três notas de um aluno e seus respectivos pesos, calcule e mostre a média ponderada 
//dessas notas e o conceito atribuído a ele, seguindo a tabela a seguir. Defina um tipo enumerado 
//para representar os conceitos e uma estrutura que contenha a média do aluno e o conceito (enum), como resposta da função.

//Média ponderada no intervalo  Conceito
//[8,0; 10,0]                                         A
//[7,0; 8,0)                                          B
//[5,0; 7,0)                                          C
//[0,0; 5,0)                                          D

//Analise: 
//Calcular a media ponderada de um aluno e dar os respectivos conceitos.

//Tipo de Dados: 
//entrada de tres numeros reais, que representam as notas obtidas por um aluno.
//saida é um valor da situaçao do aluno, A,B,C,D. 

//Representa a situaçao que o aluno esta:
    enum NOTA{
         A 
         B
         C
         D
    };

//Espercificaçao:

Notas nota_aluno( double n1,double n2,double n3);{
  return Notas; 
}

//Proposito:
//determinar a nota do aluno obteve de media

exemplos { 
    check_expect(Notas(3.0, 5.5, 4.8),D);
    check_expect(Notas(3.0, 6.5, 4.8),C);
    check_expect(Notas(8.0, 7.0, 4.8),B);
    check_expect(Notas(8.0, 7.0, 7.0),A);
};

#include <iostream>
#include "bscpp.hpp"

using namespace std;

     enum NOTA {
         A 
         B
         C
         D
     };

//implementaçao 
    Notas nota_aluno(double n1, double n2, double n3){
      double media = ((n1*5)+(n2*2)+(n3*2))/9
//sabendo que cada nota tem seu peso n1 5, n2 2, n3 2
      Notas not:
      if (media 0.0=<5.0) 
         not = D: 
      else if (media 5.0=<7.0)
         not = C;
      else if (media 7.0=<8.0)
         not = B;
      else if (media 8.0=<10.0)    
         not = A; 
    reutrn not;
 }


// Professora nao consegui usar a bibliotecxa pois esta dando erro, mas deixei os exemplos pois petrendo testar no computador do LIN

examples { 
    check_expect(Notas(3.0, 5.5, 4.8),D);
    check_expect(Notas(3.0, 6.5, 4.8),C);
    check_expect(Notas(8.0, 7.0, 4.8),B);
    check_expect(Notas(8.0, 7.0, 7.0),A);
}

int main (){
   run_tests ();
}
