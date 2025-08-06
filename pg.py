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
playfield_offset_v = 100
playfield_offset_h = 50


def plot_playfield_box(screen):
    color = pygame.Color("gray")

    coords =  (playfield_offset_h - pixel_margin , 
               playfield_offset_v - pixel_margin, 
               playfield_offset_h + 20 * pixel_width + pixel_margin , 
               playfield_offset_v + 10 * pixel_width + pixel_margin )
    print( f"Box: {coords}")

    pygame.draw.rect( screen, color, coords)



def plot_playfield(screen, r, c, v):
    color = pygame.Color(colors[v])

    coords =  (c*pixel_width + playfield_offset_h , 
               r*pixel_width+ playfield_offset_v, 
               (c+1)*pixel_width - pixel_margin + playfield_offset_h, 
               (r+1) * pixel_width - pixel_margin  + playfield_offset_v)
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

        screen.fill("black")
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
        textRect.center = (200,20)


        screen.blit(text, textRect)

        # Do logical updates here.
        # ...

        #screen.fill("purple")  # Fill the display with a solid color

        # Render the graphics here.
        # ...

        pygame.time.wait(100)
        pygame.display.flip()  # Refresh on-screen display
        clock.tick(60)         # wait until next frame (at 60 FPS)

# Questo blocco si esegue solo quando il file viene eseguito direttamente
if __name__ == "__main__":
    run()
