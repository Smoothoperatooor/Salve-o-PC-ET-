import pygame

class ET:
    def __init__(self, largura_tela, margem=10):
        self.imagem = pygame.image.load("assets/et.png").convert_alpha()
        self.imagem = pygame.transform.scale(self.imagem, (180, 180))

        self.rect = self.imagem.get_rect()
        self.rect.topright = (largura_tela - margem, margem)

        self.fonte = pygame.font.SysFont(None, 22)
 

    def atualizar_mensagem(self, temperatura):
        if temperatura > 85:
            self.mensagem = "Tá muito quente! vamos perder os frames!"
        elif temperatura > 75:
            self.mensagem = "Tá quentinho..."
        elif temperatura > 40:
            self.mensagem = "Tranquilo"
        else:
            self.mensagem = "Tá gelado demais! deixa esquentar!"

    def desenhar(self, tela):
        # Desenha ET
        tela.blit(self.imagem, self.rect)

        # Render texto
        texto_img = self.fonte.render(self.mensagem, True, (0, 0, 0))
        padding = 10

        # Balão (retângulo)
        balao_rect = pygame.Rect(
            self.rect.left - texto_img.get_width() - padding * 2 - 10,
            self.rect.top + 20,
            texto_img.get_width() + padding * 2,
            texto_img.get_height() + padding * 2
        )

        # Fundo do balão
        pygame.draw.rect(tela, (255, 255, 255), balao_rect, border_radius=10)
        pygame.draw.rect(tela, (0, 0, 0), balao_rect, 2, border_radius=10)

        # Texto
        tela.blit(
            texto_img,
            (balao_rect.x + padding, balao_rect.y + padding)
        )

        # “Rabinho” do balão
        pygame.draw.polygon(
            tela,
            (255, 255, 255),
            [
                (balao_rect.right, balao_rect.centery - 5),
                (balao_rect.right + 10, balao_rect.centery),
                (balao_rect.right, balao_rect.centery + 5)
            ]
        )
