import pygame

class Menu:
    def __init__(self, tamanho_tela):
        self.largura, self.altura = tamanho_tela
        self.fonteTitulo = pygame.font.SysFont(None, 64)
        self.fonteTexto = pygame.font.SysFont(None, 32)

        self.etImg = pygame.image.load("assets/etVitoria.png")
        self.etImg = pygame.transform.scale(self.etImg, (220, 220))
        self.etRect = self.etImg.get_rect(center=(self.largura // 2, 180))

    def gameOver(self, tela, pontuacao, motivo):
        tela.fill((20, 20, 20))

        titulo = self.fonteTitulo.render("GAME OVER", True, (255, 60, 60))
        motivo_txt = self.fonteTexto.render(motivo, True, (255, 150, 150))
        pontos = self.fonteTexto.render(f"SCORE FINAL: {pontuacao}", True, (255, 255, 0))
        sair = self.fonteTexto.render("Pressione ESC para sair", True, (200, 200, 200))

        tela.blit(titulo, titulo.get_rect(center=(self.largura//2, 260)))
        tela.blit(motivo_txt, motivo_txt.get_rect(center=(self.largura//2, 320)))
        tela.blit(pontos, pontos.get_rect(center=(self.largura//2, 380)))
        tela.blit(sair, sair.get_rect(center=(self.largura//2, 460)))

    def telaVitoria(self, tela, pontuacao):
        tela.fill((15, 30, 15))

        tela.blit(self.etImg, self.etRect)

        titulo = self.fonteTitulo.render("Muito obrigado parceiro!", True, (60, 255, 120))
        pontos = self.fonteTexto.render(f"Seus FRAMES acumulados: {pontuacao}", True, (255, 255, 0))
        sair = self.fonteTexto.render("Pressione ESC para sair", True, (200, 200, 200))

        tela.blit(titulo, titulo.get_rect(center=(self.largura//2, 300)))
        tela.blit(pontos, pontos.get_rect(center=(self.largura//2, 380)))
        tela.blit(sair, sair.get_rect(center=(self.largura//2, 450)))
