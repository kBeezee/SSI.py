import pygame


def createblock(fWidth, fHeight, fColor):
        tmpblock = pygame.Surface((fWidth, fHeight))
        tmpblock.fill(fColor)
        tmpblock.convert()
        return tmpblock

def GetMap0():
    return ["xxxxxxxxxxxxxxxxxxxxxxx",
             "......................x",
             "xxxx..........xx......x",
             "x......x....x..x......x",
             "x......x.......x......x",
             "x...x..x.....x.x......x",
             "x...xxxxxx.....x......x",
             "x......x..............x",
             "xxxxxxxx.......xxxxxxxx",
             "xxxxxxxx....x.........x",
             "x......x..............x",
             "x...x.xx..............x",
             "x..........xx.xx...xxxx",
             "x..x...x...x..........x",
             "xxxxxxxxxxxxxxxxxxxxxxx"]


class Map(pygame.sprite.Sprite):
    def __init__(self, fDisplaySurfaceSize):
        pygame.sprite.Sprite.__init__(self)
        self.m0 = GetMap0()

        self.MapSurface = pygame.Surface(fDisplaySurfaceSize)
        self.MapSurface.fill((50,60,70))
        self.rows = len(self.m0)
        self.columns = len(self.m0[0])
        self.CellWidth = self.MapSurface.get_width() / self.columns
        self.CellHeight = self.MapSurface.get_height() / self.rows

        self.playerx = 5
        self.playery = 5

        self.PlayerBlock = createblock(self.CellHeight, self.CellHeight, (255, 0, 0))
        self.WallBlock = createblock(self.CellWidth, self.CellHeight, (0, 0, 0))


        for y in xrange(self.rows):
            for x in xrange(self.columns):
                if self.m0[y][x] == "x":
                    self.MapSurface.blit(self.WallBlock, (self.CellWidth*x, self.CellHeight*y))

        #self.MapSurface.blit(self.PlayerBlock, (self.playerx, self.playery))

    def GetSurface(self):
        self.MapSurface.fill((50,60,70))
        for y in xrange(self.rows):
            for x in xrange(self.columns):
                if self.m0[y][x] == "x":
                    self.MapSurface.blit(self.WallBlock, (self.CellWidth*x, self.CellHeight*y))
        self.MapSurface.blit(self.PlayerBlock, (self.CellWidth*self.playerx, self.CellHeight*self.playery))
        print "asd"
        return self.MapSurface


# -- Functions used with Events
    def MovePlayer(self, vars):
        if vars == "u":
            if self.m0[self.playery-1][self.playerx] == ".":
                self.playery -= 1
        elif vars == "d":
            if self.m0[self.playery+1][self.playerx] == ".":
                self.playery += 1
        elif vars == "l":
            if self.m0[self.playery][self.playerx-1] == ".":
                self.playerx -= 1
        elif vars == "r":
            if self.m0[self.playery][self.playerx+1] == ".":
                self.playerx += 1