import pygame
import evnts
import maps

WINDOW_SIZE = (0,0)
UseAlts = True

def write(msg, color):
    myfont = pygame.font.SysFont("None", 34, 128)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext

IvyBorderDict = {"TopLeft":pygame.image.load("img/Ivy/ivy_top_left.png"),
                 "TopRight":pygame.image.load("img/Ivy/ivy_top_right.png"),
                 "BottomLeft":pygame.image.load("img/Ivy/ivy_bottom_left.png"),
                 "BottomRight":pygame.image.load("img/Ivy/ivy_bottom_right.png"),
                 "Left":pygame.image.load("img/Ivy/ivy_left.png"),
                 "Right":pygame.image.load("img/Ivy/ivy_right.png"),
                 "Top":pygame.image.load("img/Ivy/ivy_top.png"),
                 "Bottom":pygame.image.load("img/Ivy/ivy_bottom.png")
                 }

GoldenBorderDict = {#Corners
                "cTopLeft":pygame.image.load("img/Golden/corner_top_left.png"),
                "cTopLeftAlt":pygame.image.load("img/Golden/corner_top_left1.png"),
                "cTopRight":pygame.image.load("img/Golden/corner_top_right.png"),
                "cTopRightAlt":pygame.image.load("img/Golden/corner_top_right1.png"),
                "cBottomLeft":pygame.image.load("img/Golden/corner_bottom_left.png"),
                "cBottomLeftAlt":pygame.image.load("img/Golden/corner_bottom_left1.png"),
                "cBottomRight":pygame.image.load("img/Golden/corner_bottom_right.png"),
                "cBottomRightAlt":pygame.image.load("img/Golden/corner_bottom_right1.png"),
                #Middles
                "mLeftMiddle":pygame.image.load("img/Golden/left_middle.png"),
                "mLeftMiddleAlt":pygame.image.load("img/Golden/left_middle1.png"),
                "mRightMiddle":pygame.image.load("img/Golden/right_middle.png"),
                "mRightMiddleAlt":pygame.image.load("img/Golden/right_middle1.png"),
                "mTopMiddle":pygame.image.load("img/Golden/top_center.png"),
                "mTopMiddleAlt":pygame.image.load("img/Golden/top_center1.png"),
                "mBottomMiddle":pygame.image.load("img/Golden/bottom_center.png"),
                "mBottomMiddleAlt":pygame.image.load("img/Golden/bottom_center1.png"),
                #Fillers - will change from left to right after they get to the middle
                "fTopLeft":pygame.image.load("img/Golden/top_left.png"),
                "fTopRight":pygame.image.load("img/Golden/top_right.png"),
                "fLeftTop":pygame.image.load("img/Golden/left_top.png"),
                "fLeftBottom":pygame.image.load("img/Golden/left_bottom.png"),
                "fBottomLeft":pygame.image.load("img/Golden/bottom_left.png"),
                "fBottomRight":pygame.image.load("img/Golden/bottom_right.png"),
                "fRightTop":pygame.image.load("img/Golden/right_top.png"),
                "fRightBottom":pygame.image.load("img/Golden/right_bottom.png")
                }


class IvyBorder(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.surface = pygame.Surface(WINDOW_SIZE)
        #self.surface.blit(IvyBorderDict["TopLeft"], (0,0))

    def update(self, fScreen):
        fScreen.blit(IvyBorderDict["TopLeft"], (0,0))
        fScreen.blit(IvyBorderDict["TopRight"], (WINDOW_SIZE[0]-IvyBorderDict["TopRight"].get_width(), 0))
        fScreen.blit(IvyBorderDict["BottomLeft"], (0, WINDOW_SIZE[1]-IvyBorderDict["BottomLeft"].get_height()))
        fScreen.blit(IvyBorderDict["BottomRight"], (WINDOW_SIZE[0]-IvyBorderDict["TopRight"].get_height(), WINDOW_SIZE[1]-IvyBorderDict["BottomLeft"].get_width()))

        for h in xrange(IvyBorderDict["TopLeft"].get_height(), WINDOW_SIZE[1]-IvyBorderDict["TopLeft"].get_height(), IvyBorderDict["Left"].get_height()):
            fScreen.blit(IvyBorderDict["Left"], (0, h))
            fScreen.blit(IvyBorderDict["Left"], (WINDOW_SIZE[0]-IvyBorderDict["Left"].get_width(), h))
        for w in xrange(IvyBorderDict["TopLeft"].get_width(), WINDOW_SIZE[0]-IvyBorderDict["TopLeft"].get_width(), IvyBorderDict["Top"].get_width()):
            fScreen.blit(IvyBorderDict["Top"], (w, 0))
            fScreen.blit(IvyBorderDict["Bottom"], (w, WINDOW_SIZE[1]-IvyBorderDict["Top"].get_height()))


class HUD_Object():
    def __init__(self, text, func=['aPass'], vars=[False]):
        self.text = text
        self.functions = func
        self.fVars = vars


MenuDict = {"MainMenu":[HUD_Object("Move", ["ChangeMenu", "MovementSwitch"], ["MovementMenu", False]), HUD_Object("Camp")],
            "MovementMenu":[HUD_Object("Exit", ["ChangeMenu", "MovementSwitch"], ["MainMenu", True])]}


class hHUD(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #this part of the hud will go on the bottom
        self.surface = pygame.Surface((WINDOW_SIZE[0] - (IvyBorderDict["Left"].get_width()*3), IvyBorderDict["TopLeft"].get_height()))
        self.HudList = MenuDict['MainMenu']
        self.HudListSelectedIndex = 0
        self.surface.fill((0,0,0))

    def update(self, fScreen):
        oW = 0
        self.surface.fill((0,0,0))
        for o in self.HudList:
            if self.HudList.index(o) == self.HudListSelectedIndex:
                color = (255,255,0)
            else:
                color = (255,255,255)
            if self.HudList.index(o) == 0:
                oW = 5
            self.surface.blit(write(o.text, color), (oW,7))
            oW = oW + write(o.text, color).get_width() + 10
        fScreen.blit(self.surface, (30, 409))

    def change_selected(self, right=True):
        if right:
            if self.HudListSelectedIndex + 1 >= len(self.HudList):
                self.HudListSelectedIndex = 0
            else:
                self.HudListSelectedIndex += 1
        else:
            if self.HudListSelectedIndex - 1 < 0:
                self.HudListSelectedIndex = len(self.HudList) - 1
            else:
                self.HudListSelectedIndex -= 1

    def execute_command(self, vars=[]):
        for o in self.HudList:
            if self.HudList.index(o) == self.HudListSelectedIndex:
                for f in xrange(len(o.functions)):
                    getattr(self, o.functions[f])(o.fVars[f])
                break

#Functions -- These things do stuff, everything else that isnt this is only the engine driving the
            #below functions.
    def aPass(self, vars):
        print "Pass"

    def ChangeMenu(self, vars):
        self.HudList = MenuDict[vars]

    def MovementSwitch(self, vars):
        global UseAlts
        if vars:
            evnts.state = "Menu"
            UseAlts = True
        if not vars:
            evnts.state = "Movement"
            UseAlts = False
            
            
class StandardOut(pygame.sprite.Sprite):
    def __init__(self, fTheMap):
        pygame.sprite.Sprite.__init__(self)
        self.BorderSurface = pygame.Surface((WINDOW_SIZE[0]/2-4, WINDOW_SIZE[1]/2-5))
        self.BorderSurface.fill((20,30,40))
        self.DisplaySurfaceSize = (self.BorderSurface.get_width()-GoldenBorderDict["cTopRight"].get_width(), self.BorderSurface.get_height()-GoldenBorderDict["cTopRight"].get_width())
        self.TheMap = fTheMap

    def update(self, fScreen):
        global UseAlts
        if UseAlts:
            UseAlts = "Alt"
        else:
            UseAlts = ""

        #Draw Border
        self.BorderSurface.blit(GoldenBorderDict["cTopLeft"+UseAlts], (0,0))
        self.BorderSurface.blit(GoldenBorderDict["cTopRight"+UseAlts], (self.BorderSurface.get_width() - GoldenBorderDict["cTopRight"].get_width(), 0))
        self.BorderSurface.blit(GoldenBorderDict["cBottomLeft"+UseAlts], (0, self.BorderSurface.get_height()-GoldenBorderDict["cBottomLeft"].get_height()))
        self.BorderSurface.blit(GoldenBorderDict["cBottomRight"+UseAlts], (self.BorderSurface.get_width()-GoldenBorderDict["cTopRight"].get_height(), self.BorderSurface.get_height()-GoldenBorderDict["cBottomLeft"].get_width()))

        for h in xrange(GoldenBorderDict["cTopLeft"].get_height(), self.BorderSurface.get_height()-GoldenBorderDict["fLeftBottom"].get_height()*2, GoldenBorderDict["fLeftBottom"].get_height()):
            self.BorderSurface.blit(GoldenBorderDict["fRightBottom"], (0, h))
            self.BorderSurface.blit(GoldenBorderDict["fLeftBottom"], (self.BorderSurface.get_width()-GoldenBorderDict["fRightBottom"].get_width(), h))
        for w in xrange(GoldenBorderDict["cBottomLeft"].get_width(), self.BorderSurface.get_width()-GoldenBorderDict["fLeftBottom"].get_width()*2, GoldenBorderDict["fLeftBottom"].get_width()):
            self.BorderSurface.blit(GoldenBorderDict["fTopLeft"], (w, 0))
            self.BorderSurface.blit(GoldenBorderDict["fTopRight"], (w, self.BorderSurface.get_height()-GoldenBorderDict["fLeftTop"].get_height()))

        #Draw Within Border
        self.BorderSurface.blit(self.TheMap.GetSurface(), (GoldenBorderDict["cTopRight"].get_width()/2 , GoldenBorderDict["cTopRight"].get_width()/2))
        fScreen.blit(self.BorderSurface, (30, 30))
