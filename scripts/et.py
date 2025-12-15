import pygame

class ET:
    def __init__(self, tamanhoTela, margem=10):
        self.imagem = pygame.image.load("assets/et.png")
        self.imagem = pygame.transform.scale(self.imagem, (180, 180))
        self.rect = self.imagem.get_rect()

        largura_tela = tamanhoTela[0]
        self.rect.topright = (largura_tela - margem, margem)

        self.fonte = pygame.font.SysFont(None, 22)
        self.mensagem = ""  

    def atualizarMensagem(self, desempenho, temperatura, consumo):
        temperatura = int(temperatura)
        consumo = int(consumo)

        if temperatura > 105:
            self.mensagem = "VAI DERRETER"
        elif consumo > 330:
            self.mensagem = "A CONTA DE LUZ!"
        elif desempenho > 100:
            self.mensagem = "LISO LISO"
        elif desempenho > 60:
            self.mensagem = "Jogável..."
        else:
            self.mensagem = "SECO SECO"

    def desenhar(self, tela):
  
        tela.blit(self.imagem, self.rect)

        if not self.mensagem:
            return

        textoImg = self.fonte.render(self.mensagem, True, (0, 0, 0))
        padding = 10

        balao = pygame.Rect(
            self.rect.left - textoImg.get_width() - padding * 2 - 15,
            self.rect.top + 30,
            textoImg.get_width() + padding * 2,
            textoImg.get_height() + padding * 2
        )

        pygame.draw.rect(tela, (255, 255, 255), balao, border_radius=12)
        pygame.draw.rect(tela, (0, 0, 0), balao, 2, border_radius=12)

        tela.blit(
            textoImg,
            (balao.x + padding, balao.y + padding)
        )

