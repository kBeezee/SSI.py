import pygame
import evnts
import drw
import maps

def write(msg="pygame is cool"):
    myfont = pygame.font.SysFont("None", 34, 128)
    mytext = myfont.render(msg, True, (0, 0, 0))
    mytext = mytext.convert_alpha()
    return mytext

# Initialize pygame
pygame.init()
pygame.key.set_repeat(100, 100)

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = (640, 480)
drw.WINDOW_SIZE = WINDOW_SIZE
DisplaySurfaceSize = (WINDOW_SIZE[0]/2-4-drw.GoldenBorderDict["cTopRight"].get_width(),
                      WINDOW_SIZE[1]/2-5-drw.GoldenBorderDict["cTopRight"].get_width())

screen = pygame.display.set_mode(WINDOW_SIZE)

#hide mouse cursor
pygame.mouse.set_visible(True)

# Set title of screen
pygame.display.set_caption("March of the Ants of The Northern Colony")

# Loop until the user clicks the close button.
Running = True

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Make a few variables
screen_GlobalSprites = pygame.sprite.Group()
screen_GlobalSprites.add(drw.IvyBorder())
screen_GlobalSprites.add(drw.hHUD())
aMap = maps.Map(DisplaySurfaceSize)
screen_GlobalSprites.add(aMap)
screen_GlobalSprites.add(drw.StandardOut(aMap))
screen.fill((20, 30, 40)) # color of background

# -------- Main Program Loop -----------
while Running:
    # Handle Events
    TheEvents = pygame.event.get()
    Running = evnts.CheckQuit(TheEvents)
    Updates = evnts.Updates(TheEvents)

    if len(TheEvents) != 0:
        # Update your stuff
        for up in Updates:
            for obs in screen_GlobalSprites:
                if obs.__class__.__name__.upper() == up[0].upper():
                    for method in dir(obs):
                        #print "Executing %s method from the %s class with the variables %s" % (up[1], obs.__class__.__name__, up[2])
                        if method.title().upper() == up[1].upper():
                            getattr(obs, up[1])(up[2])

        # Draw Everything
        screen.fill((20, 30, 40))
        if pygame.mouse.get_focused():
            screen.blit(write(str(pygame.mouse.get_pos())), (90, 335))  # Mouse Cords

        # Limit to 60 frames per second
        clock.tick(60)

        # update the screen with what we've drawn.
        screen_GlobalSprites.update(screen)
        pygame.display.flip()

#print
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()