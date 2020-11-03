import pygame

def main():
    pygame.init()
    WIDTH = 1500
    HEIGHT = 1000
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.update()

    wcolor = pygame.Color("white")
    BORDER = 15

    #top
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (WIDTH, BORDER)))
    #left
    pygame.draw.rect(screen, wcolor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
    #bottom
    #pygame.draw.rect(screen, wcolor, pygame.Rect((0, HEIGHT-BORDER), (WIDTH, HEIGHT)))
    pygame.display.update()
    running = True

    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == "__main__":
    main()
