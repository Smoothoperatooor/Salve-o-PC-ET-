import pygame

class Ventilador:
    def __init__(self, x, y):
        self.imagem = pygame.image.load("assets/ventilador.png")
        self.imagem = pygame.transform.scale(self.imagem, (120, 180))
        self.rect = self.imagem.get_rect(topleft=(x, y))
        
        self.arrastando = False
        self.offset_x = 0
        self.offset_y = 0
    
    def manipularEventos(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.arrastando = True
                self.offset_x = self.rect.x - evento.pos[0]
                self.offset_y = self.rect.y - evento.pos[1]
        
        elif evento.type == pygame.MOUSEBUTTONUP:
            self.arrastando = False
        
        elif evento.type == pygame.MOUSEMOTION and self.arrastando:
            self.rect.x = evento.pos[0] + self.offset_x
            self.rect.y = evento.pos[1] + self.offset_y
    
    
    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)