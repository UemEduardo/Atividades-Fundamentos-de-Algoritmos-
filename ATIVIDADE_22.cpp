/*22. Rotacionar um arranjo n posições a esquerda significa mover os primeiros n elementos do arranjo para
as últimas n posições do arranjo. Por exemplo, rotacionar o arranjo {5, 3, 4, 1, 7} duas posições a
esquerda produz o arranjo {4, 1, 7, 5, 3}. Projete uma função que rotacione um arranjo n posições
a esquerda.


• Análise (oque deve ser feito ) 
Fazer uma funçao que rotacion um arranjon posicoes a esquerda.

• Definição dos tipos de dados 
-Entrada: Um arranjo que deve ser rotacionado,esse arranjo sera com numeros inteiros  

-Saida: Sera o arranjo ja rotacionado 

• Especificação 

-Assinatuta: vector<int> rotacionar(vector <int> vet, int n ){ 
}

-Proposito: Rotacionar o arranjo em uma determinada posiçao a esquerda

-Exemplos 
check_expect(rotacionar ({5,3,4,6,8 },3) , (vector<int> {6,8,5,3,4}))
check_expect(rotacionar ({2,5,4,9,10},4) , (vector<int> {2,5,4,9,10}))
check_expect(rotacionar ({4,3,2,5,7,5},2) ,(vector<int> {2,5,7,5,3,4}))

*/

//• Implementação
#include <iostream>
#include <vector>
#include "bscpp.hpp"

using namespace std ;

 vector <int> rotacionar(vector <int> array, int n ){ 
 vector <int> rotacionaNovo = {};
  
  for (int i=n; i < array.size(); i= i+1){
    resultado.push_back(array[i]);
    }
  for (int i=0; i < n; i= i+1){
    resultado.push_back(array[i]);  
    }
return rotacinaNovo;
}


int main () { 
    
    run_tests();
}