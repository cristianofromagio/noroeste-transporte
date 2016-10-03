#Transporte - Canto noroeste

##Descrição

Programa escrito em Python, seguindo as recomendações da versão [3.4.3](https://www.python.org/downloads/release/python-343/), para o desenvolvimento de uma interface que auxiliasse a resolução de um problema de transporte apresentado na disciplina de Programação Linear.

##Restrições

O sistema deveria apresentar o resultado final do processamento na interface, ao mesmo tempo que apresentava os dados de cada etapa do processamento no console. O algoritmo utilizado na resolução não foi especificado. A opção escolhida para o desenvolvimento do programa foi o Método do Canto Noroeste que, embora não resulte na resposta mais ótima possível, apresenta resultados satisfatórios.

##Especificações

O programa é alimentado com uma matriz com os valores que representam os custos e/ou quantidades apresentados pelo problema de transporte. Por meio do algoritmo do canto noroeste ela é percorrida e preenchida com os valores da sua resolução, enquanto imprimi cada etapa do processo no console. O resultado final do processamento é finalmente apresentado na interface para o usuário. A interface foi desenvolvida utilizando Qt, compilada e traduzida utilizando [PyQt](https://www.riverbankcomputing.com/software/pyqt/intro), [v.4](https://www.riverbankcomputing.com/software/pyqt/download).

##Problema
Deseja-se transportar arroz de três armazéns (1, 2 e 3) a três centros consumidores distintos (A, B e C). Cada armazém apresentou os seguintes níveis de estoque de arroz em determinado mês:

| Armazém | Arroz disponível (kg) |
|     :---:      |     :---:      |
| 1 | 200 |
| 2 | 150 |
| 3 | 300 |

Cada centro consumidor estará apto a receber as seguintes quantidades de arroz naquele mês:

| Centro consumidor | Demanda (kg) |
|     :---:      |     :---:      |
| A | 100 |
| B | 300 |
| C | 250 |

Os custos unitários de transporte ($/kg) envolvidos são os seguintes:

| De/Para | A | B | C |
|     :---:      |     :---:      |     :---:      |     :---:      |
| 1 | $ 10 | $ 5 | $ 12 |
| 2 | $ 4 | $ 9 | $ 15 |
| 3 | $ 15 | $ 8 | $ 6 |

Qual será a quantidade de arroz a ser transportada entre cada armazém e cada centro consumidor, de tal forma que as demandas de cada centro sejam supridas e que o custo total de transporte seja mínimo?
