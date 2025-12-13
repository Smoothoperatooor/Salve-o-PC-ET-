import pygame

class Botao:
    def __init__(self, x, y, texto):
        self.rect = pygame.Rect(x, y, 180, 50)
        self.texto = texto
        self.fonte = pygame.font.SysFont(None, 28)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (200, 50, 50), self.rect, border_radius=8)
        pygame.draw.rect(tela, (0, 0, 0), self.rect, 2, border_radius=8)

        img = self.fonte.render(self.texto, True, (255,255,255))
        tela.blit(
            img,
            (self.rect.centerx - img.get_width() // 2,
             self.rect.centery - img.get_height() // 2)
        )

    def foi_clicado(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(evento.pos)
        )
