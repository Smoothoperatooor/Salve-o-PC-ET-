import pygame

class Fases:
    def __init__(self):
        self.faseAtual = 1
        self.totalFases = 3

        self.tempoFase = 15000  # 30 segundos
        self.inicioFase = pygame.time.get_ticks()

        self.pontuacoes = []

    def resetarTimer(self):
        self.inicioFase = pygame.time.get_ticks()

    def tempoEsgotado(self):
        agora = pygame.time.get_ticks()
        return agora - self.inicioFase >= self.tempoFase

    def avancarFase(self, framesFinal):
        self.pontuacoes.append(int(framesFinal))
        self.faseAtual += 1
        self.resetarTimer()

    def acabou(self):
        return self.faseAtual > self.totalFases

    def pontuacaoFinal(self):
        return sum(self.pontuacoes)
