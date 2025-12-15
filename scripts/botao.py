import pygame

class Botao:
    def __init__(self, x, y, texto):
        self.rect = pygame.Rect(x, y, 180, 50)
        self.texto = texto
        self.fonte = pygame.font.SysFont(None, 28)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (200,200,200), self.rect, border_radius=8)
        txt = self.fonte.render(self.texto, True, (0,0,0))
        tela.blit(txt, txt.get_rect(center=self.rect.center))

    def clicado(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(evento.pos)
        )

class BotaoUndervolt:
    def __init__(self, x, y, texto):
        self.rect = pygame.Rect(x, y, 180, 50)
        self.texto = texto
        self.fonte = pygame.font.SysFont(None, 28)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (200,200,200), self.rect, border_radius=8)
        txt = self.fonte.render(self.texto, True, (0,0,0))
        tela.blit(txt, txt.get_rect(center=self.rect.center))

    def clicado(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and self.rect.collidepoint(evento.pos)
        )