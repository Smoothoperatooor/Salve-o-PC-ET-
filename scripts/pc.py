import pygame, random

class PC:
    def __init__(self, x, y):
        self.imagem = pygame.image.load("assets/pc.png")
        self.imagem = pygame.transform.scale(self.imagem, (280, 610))
        self.rect = self.imagem.get_rect(topleft=(x, y))

        # Temperatura
        self.temperatura = 50
        self.temp_max = 130
        self.temp_min = 20

        self.aquecimento = 0.05
        self.resfriamento = 0.1

        # Fonte (criada uma vez)
        self.fonte = pygame.font.SysFont(None, 45)

        self.desempenho = 100
        self.desempenho_min = 10
        self.em_falha = False

        self.fonte = pygame.font.SysFont(None, 24)

        self.timer_falha = random.randint(300, 600)  # 5–10s

    def atualizar(self):
        self.timer_falha -= 1
        if self.timer_falha <= 0 and not self.em_falha:
            self.em_falha = True
            self.desempenho = self.desempenho_min

    def ativar_overclock(self):
        self.em_falha = False
        self.desempenho = 60
        self.timer_falha = random.randint(300, 600)

    def verificar_resfriamento(self, ventilador):
        # Esquenta naturalmente
        self.temperatura += self.aquecimento

        # Resfriamento com ventilador
        if self.rect.colliderect(ventilador.rect):
            self.temperatura -= self.resfriamento

        # Limites
        self.temperatura = max(
            self.temp_min,
            min(self.temp_max, self.temperatura)
        )

    def desenhar(self, tela, largura_tela, altura_tela):
    # Desenha o PC
        tela.blit(self.imagem, self.rect)

        # Desempenho (FRAMES)
        cor = (255, 60, 60) if self.em_falha else (60, 255, 120)
        perf_txt = self.fonte.render(f"FRAMES: {self.desempenho}fps", True, cor)

        perf_rect = perf_txt.get_rect(
            center=(largura_tela // 2, altura_tela // 2)
        )
        tela.blit(perf_txt, perf_rect)

        # Temperatura
        if self.temperatura > 85:
            cor_texto = (255, 60, 60)
        elif self.temperatura > 75:
            cor_texto = (255, 200, 60)
        else:
            cor_texto = (60, 255, 120)

        temp_txt = self.fonte.render(
            f"Temp: {int(self.temperatura)}°C", True, cor_texto
        )

        temp_rect = temp_txt.get_rect(
            midtop=(self.rect.centerx, self.rect.top + 90)
        )
        tela.blit(temp_txt, temp_rect)

    def em_game_over(self):
        return self.temperatura > 110 or self.temperatura < 35
