import Mochila
import  Objetos
import Dibujar

import pygame


WIDTH, HEIGHT = 1800, 1000

def main():
    mochila = Mochila.Mochila(100, (6, 6))
    mochila.CrearObjetos()
    # imprime las matrices de los objetos en la mochila
    for obj in mochila.ConjObjetos:
        for i in range(obj.tamano[0]):
            for j in range(obj.tamano[1]):
                print(obj.matriz[i][j], end=' ')
            print()
        print()
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('MochilaJogo')

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        Dibujar.dibujar_mochila(screen, mochila)


        pygame.time.Clock().tick(60)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()