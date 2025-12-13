import pygame
from scripts.pc import PC
from scripts.ventilador import Ventilador
from scripts.et import ET
from scripts.botao import Botao

pygame.init()

WIDTH, HEIGHT = 1200, 800
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Salve o PC, ET!")
clock = pygame.time.Clock()

# Fundo
fundo = pygame.image.load("assets/fundo.png").convert()
fundo = pygame.transform.scale(fundo, (WIDTH, HEIGHT))


def main():
    ventilador = Ventilador(100, 350)
    pc = PC(900, 150)
    et = ET(WIDTH)
    botao_overclock = Botao(500, 0, "OVERCLOCK")

    game_over = False
    rodando = True
    while rodando:
        clock.tick(60)
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            ventilador.manipular_eventos(evento)
        
        ventilador.atualizar()
        et.atualizar_mensagem(pc.temperatura)
        pc.verificar_resfriamento(ventilador)
        pc.atualizar()
        

        if pc.em_falha and botao_overclock.foi_clicado(evento):
            pc.ativar_overclock()
                
        if pc.em_game_over():
            game_over = True
        
        # Desenho
        tela.blit(fundo, (0, 0))
        ventilador.desenhar(tela)
        pc.desenhar(tela, WIDTH, HEIGHT)
        if pc.em_falha:
            botao_overclock.desenhar(tela)

        et.desenhar(tela)
        pygame.draw.rect(tela, (0, 0, 0), et.rect.inflate(6, 6), 3)

        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
