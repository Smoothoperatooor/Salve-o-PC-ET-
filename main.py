import pygame
from scripts.menu import Menu
from scripts.fases import Fases
from scripts.et import ET
from scripts.pc import PC
from scripts.ventilador import Ventilador
from scripts.botao import Botao, BotaoUndervolt

pygame.init()

tamanhoTela = (1200, 800)
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("Salve o PC, ET!")
relogio = pygame.time.Clock()

fundo = pygame.image.load("assets/fundo.png")
fundo = pygame.transform.scale(fundo, tamanhoTela)

JOGANDO = 0
GAMEOVER = 1
VITORIA = 2

def main():
    menu = Menu(tamanhoTela)
    estado = JOGANDO
    pontuacao = 0

    ventilador = Ventilador(100, 350)
    pc = PC(900, 150)
    et = ET(tamanhoTela)

    botaoOverclock = Botao(250, 720, "OVERCLOCK")
    botaoUndervolt = BotaoUndervolt(20, 720, "UNDERVOLT")

    fases = Fases()
    pc.aplicarDificuldade(fases.faseAtual)

    rodando = True
    while rodando:
        relogio.tick(60)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                if estado != JOGANDO:
                    rodando = False

            if estado == JOGANDO:
                ventilador.manipularEventos(evento)

                if botaoOverclock.clicado(evento):
                    pc.overclock()

                if botaoUndervolt.clicado(evento):
                    pc.undervolt()

        if estado == JOGANDO:
            pc.verificarResfriamento(ventilador)
            pc.atualizar()
            et.atualizarMensagem(
                pc.desempenho,
                pc.temperatura,
                pc.consumo
            )

            if fases.tempoEsgotado():
                fases.avancarFase(pc.desempenho)

                if fases.acabou():
                    pontuacao = fases.pontuacaoFinal()
                    estado = VITORIA
                else:
                    pc.aplicarDificuldade(fases.faseAtual)

            if pc.gameOver():
                pontuacao = fases.pontuacaoFinal()

                if pc.temperatura > 100:
                    motivo_game_over = "O PC derreteu!"
                elif pc.consumo > 350:
                    motivo_game_over = "A conta de luz venceu você!"
                else:
                    motivo_game_over = "Predeu muitos frames!"

                estado = GAMEOVER

        if estado == JOGANDO:
            tela.blit(fundo, (0, 0))

            pc.desenhar(tela, tamanhoTela)
            ventilador.desenhar(tela)
            et.desenhar(tela)

            botaoOverclock.desenhar(tela)
            botaoUndervolt.desenhar(tela)

            faseTexto = pc.fonte.render(f"FASE {fases.faseAtual}/3",True,(10, 10, 10))
            tela.blit(faseTexto, (20, 20))

        elif estado == GAMEOVER:
            menu.gameOver(tela, pontuacao, motivo_game_over)

        elif estado == VITORIA:
            menu.telaVitoria(tela, pontuacao)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
