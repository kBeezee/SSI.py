import pygame

state = "Menu"

def CheckQuit(TheEvents):
    Running = True
    for event in TheEvents:  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            Running = False  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN:
            # Key Events which are system related, like exit will happen here, others specific to the game
            # will happen as part of the object?
            if event.key == pygame.K_ESCAPE:
                Running = False
    return Running

def Updates(TheEvents):
    OutEvents = []
    for event in TheEvents:  # User did something
        if event.type == pygame.KEYDOWN:
            # https://www.pygame.org/docs/ref/key.html
            if state == "Menu":
                if event.key == pygame.K_LEFT:
                    OutEvents.append(("hHUD", "change_selected", False))
                elif event.key == pygame.K_RIGHT:
                    OutEvents.append(("hHUD", "change_selected", True))
            elif state == "Movement":
                if event.key == pygame.K_LEFT:
                    #print "Moved Left"
                    OutEvents.append(("Map", "MovePlayer", "l"))
                elif event.key == pygame.K_RIGHT:
                    #print "Moved Right"
                    OutEvents.append(("Map", "MovePlayer", "r"))
                elif event.key == pygame.K_UP:
                    #print "Moved Up"
                    OutEvents.append(("Map", "MovePlayer", "u"))
                elif event.key == pygame.K_DOWN:
                    #print "Moved Down"
                    OutEvents.append(("Map", "MovePlayer", "d"))

            if event.key == pygame.K_RETURN:
                OutEvents.append(("hHUD", "execute_command", 0))
    return OutEvents

def write(msg="pygame is cool"):
    myfont = pygame.font.SysFont("None", 34, 128)
    mytext = myfont.render(msg, True, (0, 0, 0))
    mytext = mytext.convert_alpha()
    return mytext