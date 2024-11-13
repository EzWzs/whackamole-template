import pygame
import random
import math


def main():
    pygame.init()
    mole_image = pygame.image.load("mole.png")
    # initialize clock and screen objects
    screen = pygame.display.set_mode((640, 512))
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    moleLocation = (10,10)
    counter = 0
    counterText = font.render(f"Times moled: {counter}", True, "black")
    print("mole game, how high can you go, don't miss or you will reset to 0.")
    #drawing lines
    vertical_lines = {
        #vertical lines
        (40,0): (40,512),
        (80,0): (80,512),
        (120, 0): (120, 512),
        (160, 0): (160, 512),
        (200, 0): (200, 512),
        (240, 0): (240, 512),
        (280, 0): (280, 512),
        (320, 0): (320, 512),
        (360, 0): (360, 512),
        (400, 0): (400, 512),
        (440, 0): (440, 512),
        (480, 0): (480, 512),
        (520, 0): (520, 512),
        (560, 0): (560, 512),
        (600, 0): (600, 512)
    }

    horizontal_lines = {
        (0, 40): (640, 40),
        (0, 80): (640, 80),
        (0, 120): (640, 120),
        (0, 160): (640, 160),
        (0, 200): (640, 200),
        (0, 240): (640, 240),
        (0, 280): (640, 280),
        (0, 320): (640, 320),
        (0, 360): (640, 360),
        (0, 400): (640, 400),
        (0, 440): (640, 440),
        (0, 480): (640, 480)


    }
    try:
        # You can draw the mole with this snippet:
        running = True
        while running:
            for event in pygame.event.get():
                # user clicks x to exit
                screen.fill("light green")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #use distance formula to check how away sqrt(x^2-x^1)^2
                    distance = math.sqrt((event.pos[0] - moleLocation[0])**2 + (event.pos[1] - moleLocation[1])**2)
                    #print(distance)
                    if distance <= 40:
                        randomTuple = (random.randrange(1, 601), random.randrange(1, 481))
                        moleLocation = (round(randomTuple[0]/40) * 40, round(randomTuple[1]/40) * 40)
                        print(moleLocation, "Counter: ", counter)
                        counter += 1
                    else:
                        counter = 0
                if event.type == pygame.K_c:
                    pass
                if event.type == pygame.QUIT:
                    running = False
            #screen.fill("light green")
            #draw lines and top left mole start position
            for start, end in vertical_lines.items():
                pygame.draw.line(screen, "black", start, end)
            for start, end in horizontal_lines.items():
                pygame.draw.line(screen, "black", start, end)
            screen.blit(mole_image, mole_image.get_rect(topleft=moleLocation))
            pygame.display.flip()
            #fps limit
            clock.tick(60)
    # except:
    #     print("Error occurred.")
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
