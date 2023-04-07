#Aqui emportamos as classes.
from Classe import Jogadores
from Classe import Jogo
#Em seguida, foram criados três objetos da classe 'Jogadores'.
dudalisboa = Jogadores("Duda Lisboa", 1.8, 6, 5, 10, 6, 7)
anapatricia = Jogadores("Ana Patrícia", 1.94, 5, 7, 6, 5, 6)
alana = Jogadores("Alana", 1.63, 9, 4, 5, 7, 4 )
#As variáveis "Jogador" e "Jogador2" são criadas e são atribuídas aos objetos "dudalisboa" e "anapatricia".
Jogador = dudalisboa
Jogador2 = anapatricia
#Os métodos "detalhesJogador" da classe "Jogadores" são chamados para imprimir os detalhes do objeto "Jogador" e "Jogador2.
#Por último, os métodos "Rodada1" e "Rodada2" da classe "Jogo" são chamados, passando como argumentos os objetos "Jogador" e "Jogador2".
Jogadores.detalhesJogador(Jogador)
Jogo.Rodada1(Jogador)
Jogadores.detalhesJogador(Jogador2)
Jogo.Rodada2(Jogador2)
#pontosJogador = 0
#pontosComputador = 0
