import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()} \nVida: {self.get_vida()} \nNivel: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

    def atacar(self, alvo):
        ataque = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(ataque)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {ataque} de dano")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nHbilidade: {self.get_habilidade()}\n"
    
    def habilidade_especial(self, alvo):
        ataque_especial = random.randint(self.get_nivel() * 4, self.get_nivel() * 7)
        alvo.receber_ataque(ataque_especial)
        print(f"O heroi atacou com sua habilidade especial {self.get_habilidade()} e causou {ataque_especial} de dano")
    
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
    
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()} \nTipo: {self.get_tipo()}\n"

class Jogo:
    """ Classe que ira orquestrar o jogo """

    def __init__(self) -> None:
        self.heroi = Heroi("Mario", 100, 5, "Flor de Fogo")
        self.inimigo = Inimigo("Bowser", 75, 4, "Fogo")

    def iniciar_batalha(self):
        """Faz a gestao da batalha de turnos"""
        print("Iniciando batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0: 
            print("\nDetalhes dos personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Precione Enter para atacar")
            escolha = input("Escolha: (1- Ataque normal) (2- Ataque especial):\n ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.habilidade_especial(self.inimigo)
            else:
                print("escolha invalida, escolha novamente")
            
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("\nParabens, voce venceu a batalha!")
        else:
            print("\nVoce foi derrotado!")

jogo = Jogo()
jogo.iniciar_batalha()