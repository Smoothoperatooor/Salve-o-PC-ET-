import pygame, random

import pygame

class PC:
    def __init__(self, x, y):
        self.imagem = pygame.image.load("assets/pc.png")
        self.imagem = pygame.transform.scale(self.imagem, (280, 610))
        self.rect = self.imagem.get_rect(topleft=(x, y))

        self.cooldown_overclock = 1200   
        self.cooldown_undervolt = 1000   

        self.ultimo_overclock = 0
        self.ultimo_undervolt = 0

        self.desempenho = 90      
        self.temperatura = 55     
        self.consumo = 220        

        self.tempMin = 20
        self.tempMax = 130
        self.consumoMin = 20
        self.consumoMax = 360
        
        self.fonte = pygame.font.SysFont(None, 24)


    def overclock(self):
        agora = pygame.time.get_ticks()

        if agora - self.ultimo_overclock < self.cooldown_overclock:
            return  

        self.ultimo_overclock = agora

        self.desempenho += 15
        self.temperatura += 6
        self.consumo += 40

    def undervolt(self):
        agora = pygame.time.get_ticks()

        if agora - self.ultimo_undervolt < self.cooldown_undervolt:
            return

        self.ultimo_undervolt = agora

        self.consumo -= 45
        self.temperatura -= 10


    def atualizarDesempenho(self):
    
        if self.temperatura < 50:
            base = 120
        elif self.temperatura < 70:
            base = 90
        elif self.temperatura < 85:
            base = 60
        elif self.temperatura < 100:
            base = 30
        else:
            base = 10

        base += self.nivel_overclock * 15

        self.desempenho = max(5, min(base, 900))

    def atualizarConsumo(self):
    
        alvo = 120 + self.desempenho * 1.2

        if self.temperatura > 80:
            alvo += (self.temperatura - 80) * 2.5

        self.consumo += (alvo - self.consumo) * self.consumoSobe

        self.consumo = int(self.consumo)

    def atualizar(self):
   
        self.temperatura += self.aquecimento

        self.consumo += self.consumoSobe

        if self.temperatura > 90:
            self.desempenho -= 0.2

        self.desempenho = max(5, min(200, self.desempenho))
        self.temperatura = max(self.tempMin, min(self.tempMax, self.temperatura))
        self.consumo = max(self.consumoMin, min(self.consumoMax, self.consumo))

    def verificarResfriamento(self, ventilador):
        if self.rect.colliderect(ventilador.rect):
            self.temperatura -= 0.15


    def desenhar(self, tela, tamanhoTela):

        tela.blit(self.imagem, self.rect)

        largura, altura = tamanhoTela

        espacamento = 35
        linha = 0

        corFps = (255, 60, 60)
        fpsTexto = self.fonte.render(f"FRAMES: {int(self.desempenho)} fps", True, corFps)
        fpsRect = fpsTexto.get_rect(center=(largura - 600, altura - 500 + linha * espacamento))
        tela.blit(fpsTexto, fpsRect)

 

        corEnergia = (255, 60, 60) if self.consumo > 300 else (60, 200, 255)
        energiaTexto = self.fonte.render(f"CONSUMO: {int(self.consumo)} W", True, corEnergia)
        energiaRect = energiaTexto.get_rect(center=(largura - 600, altura - 550 + linha * espacamento))
        tela.blit(energiaTexto, energiaRect)

   

        if self.temperatura > 85:
            corTemp = (255, 60, 60)
        elif self.temperatura > 75:
            corTemp = (255, 200, 60)
        else:
            corTemp = (60, 255, 120)

        tempTexto = self.fonte.render(f"TEMP: {int(self.temperatura)}°C", True, corTemp)
        tempRect = tempTexto.get_rect(center=(largura - 600, altura - 600 + linha * espacamento))
        tela.blit(tempTexto, tempRect)


    def aplicarDificuldade(self, fase):
        if fase == 1:
            self.aquecimento = 0.08
            self.consumoSobe = 0.08
        elif fase == 2:
            self.aquecimento = 0.12
            self.consumoSobe = 0.12
        elif fase == 3:
            self.aquecimento = 0.15
            self.consumoSobe = 0.15

    def gameOver(self):
        return (
            self.temperatura > 120 or
            self.temperatura < 35 or
            self.consumo > 350 or
            self.consumo < 35 or
            self.desempenho < 15
        )