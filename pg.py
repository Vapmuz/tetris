import pygame

from gioco import Gioco



colors = {
        '': pygame.Color("black"),
        'b': pygame.Color("blue"),
        'r': pygame.Color("red"),
        'y': pygame.Color("yellow"),
        'o': pygame.Color("orange"),
        'g': pygame.Color("green"),
        'p': pygame.Color("purple"),
    }
    

pixel_width = 10
pixel_margin = 0
playfield_offset_v = 250
playfield_offset_h = 500


def plot_playfield_box(screen):
    color = pygame.Color("gray")

    coords =  (515, 
               100, 
                250,500)
    print( f"Box: {coords}")

    pygame.draw.rect( screen, color, coords)



def plot_playfield(screen, r, c, v):
    color = pygame.Color(colors[v])

    coords =  (c*pixel_width + playfield_offset_h+90 , 
               r*pixel_width+ playfield_offset_v, 
               10,10)
    #print( f"({r},{c}) = {coords}")

    pygame.draw.rect( screen, color, coords)




def run():
    gg = Gioco()
    pygame.init()
    screen = pygame.display.set_mode((1280,720))
    clock = pygame.time.Clock()
    font = pygame.font.Font('freesansbold.ttf', 20)

    
    # assigning values to X and Y variable
    X = 400
    Y = 400

    while gg.playing:
        # Process player inputs.
        cmd = ""
        for event in pygame.event.get():
            #print ("Event: " + str(event))
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cmd = "l"
                elif event.key == pygame.K_RIGHT:
                    cmd = "r"
                elif event.key == pygame.K_DOWN:
                    cmd = "x"
                
        gg.command(cmd)
        gg.iterations += 1

        screen.fill("green")
        plot_playfield_box(screen)

        for r in range(20):
            for c in range(10):
                color = gg.pf.val_at((r,c))
                plot_playfield(screen, r, c, color)
               
        # create a text surface object,
        # on which text is drawn on it.
        t0 = f"Loop: {gg.iterations} - Score {gg.score} - Lines {gg.lines}"
        print(t0)

        text = font.render( t0 , True, 
                        pygame.Color("red"), pygame.Color("blue"))

        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()
        # set the center of the rectangular object.
        textRect.center = (playfield_offset_h+140,20)


        screen.blit(text, textRect)

        # Do logical updates here.
        # ...

        #screen.fill("purple")  # Fill the display with a solid color

        # Render the graphics here.
        # ...

        pygame.time.wait(150)
        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)

# Questo blocco si esegue solo quando il file viene eseguito direttamente
if __name__ == "__main__":
    run()
