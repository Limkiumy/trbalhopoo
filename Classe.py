import time
class Jogadores:
    def __init__(self, nomeJogador, alturaJogador, forcaJogador, velocidadeJogador, habilidadeJogador, pontariaJogador, tecnicaJogador ):
        self.nomeJogador = nomeJogador
        self.alturaJogador = alturaJogador
        self.forcaJogador = forcaJogador
        self.velocidadeJogador = velocidadeJogador
        self.habilidadeJogador = habilidadeJogador
        self.pontariaJogador = pontariaJogador
        self.tecnicaJogador = tecnicaJogador

    def detalhesJogador(self):
        print("A sua carta é:", self.nomeJogador, "--------> Altura:", self.alturaJogador)
        print("Força:", self.forcaJogador)
        print("Velocidade:", self.velocidadeJogador)
        print("Habilidade:", self.habilidadeJogador)
        print("Pontaria:", self.pontariaJogador)
        print("Técnica:", self.tecnicaJogador)
Emanuel = Jogadores("Emanuel Rego", 1.9, 7, 6, 9, 8, 10)
agatha = Jogadores("Ágatha", 1.82, 4, 8, 3, 4, 5)
andressa = Jogadores("Andressa Calvacanti", 1.75, 8, 9, 7, 3, 3)

class Jogo:
    def Rodada1(Jogador,):
        categoria_escolhida = input(" --> Escolha uma categoria para ser comparada:\n(Digite 1 para:força; Digite 2 para:velocidade; Digite 3 para:habilidade; Digite 4 para:pontaria; Digite 5 para:técnica): ")
        if categoria_escolhida == "1":
            Jogador = Jogador.forcaJogador
            AtrComputador = Emanuel.forcaJogador
            print(">> A categoria escolhida foi: 'Força'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesJogador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!! Você ganhou a rodada 1!!")
                #pontosJogador += 3
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                #pontosComputador += 3
        elif categoria_escolhida == "2":
            Jogador = Jogador.velocidadeJogador
            AtrComputador = Emanuel.velocidadeJogador
            print(">> A categoria escolhida foi: 'Velocidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesJogador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!! Você ganhou a rodada 1!!")
                #pontosJogador += 3
            else: 
                print("Infelizmente, você perdeu a rodada 1.")
                #pontosComputador += 3
        elif categoria_escolhida == "3":
            Jogador = Jogador.habilidadeJogador
            AtrComputador = Emanuel.habilidadeJogador
            print(">> A categoria escolhida foi: 'Habilidade'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesJogador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!! Você ganhou a rodada 1!!")
                #pontosJogador += 3
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                #pontosComputador += 3
        elif categoria_escolhida == "4":
            Jogador = Jogador.pontariaJogador
            AtrComputador = Emanuel.pontariaJogador
            print(">> A categoria escolhida foi: 'Pontaria'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesJogador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!!, você ganhou a rodada 1!!")
                #pontosJogador += 3
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                #pontosComputador += 3
        elif categoria_escolhida == "5":
            Jogador = Jogador.tecnicaJogador
            AtrComputador = Emanuel.tecnicaJogador
            print(">> A categoria escolhida foi: 'Técnica'")
            print("")
            print(">> A carta do computador é: ")
            time.sleep(2)
            Jogadores.detalhesJogador(Emanuel)
            if Jogador > AtrComputador:
                print("PARABÉNS!!, você ganhou a rodada 1!!")
                #pontosJogador += 3
            else:
                print("Infelizmente, você perdeu a rodada 1.")
                #pontosComputador += 3