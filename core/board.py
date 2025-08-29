from settings import random, pygame, pixelLetters, windowSize, math

class Board:
    def __init__(self, size, seed, mineAmount):

        self.lost = False

        self.size = size
        self.seed = seed
        self.mineAmount = mineAmount
        
        self.flaggedSpaces = []
        self.mineSpaces = []
        self.safeSpaces = []
        self.hiddenSpaces = []

        if not None: random.seed(seed)
        while mineAmount > 0:
            position = (random.randint(1, 16), random.randint(1, 16))
            if not position in self.mineSpaces:
                self.mineSpaces.append(position)
                mineAmount -= 1
    
        for i in range(1, size[0] + 1):
            for j in range(1, size[1] + 1):
                position = (i, j)
                self.hiddenSpaces.append(position)
                if not position in self.mineSpaces:
                    self.safeSpaces.append(position)
    
    def draw_mines(self, surface):
        for mine in self.mineSpaces:
            pygame.draw.circle(surface,
                               "#424242",
                               ((windowSize[0]/self.size[0])*mine[0] - (windowSize[0]/self.size[0])/2, (windowSize[1]/self.size[1])*mine[1] - (windowSize[0]/self.size[0])/2),
                               (windowSize[0]/self.size[0])/2 * .66)
            pygame.draw.circle(surface,
                               "#000000",
                               ((windowSize[0]/self.size[0])*mine[0] - (windowSize[0]/self.size[0])/2, (windowSize[1]/self.size[1])*mine[1] - (windowSize[0]/self.size[0])/2),
                               (windowSize[0]/self.size[0])/2 * .66,
                               width=4)
    
    def draw_grid(self, surface):
        for i in range(1, self.size[0] + 1):
            for j in range(1, self.size[1] + 1):
                rect = pygame.Rect((windowSize[0]/self.size[0])*i - (windowSize[0]/self.size[0]),
                                   (windowSize[1]/self.size[1])*j - (windowSize[1]/self.size[1]),
                                   (windowSize[0]/self.size[0]),
                                   (windowSize[0]/self.size[0]))
                pygame.draw.rect(surface,
                                pygame.Color(200, 200, 200, 255),
                                rect)
                pygame.draw.rect(surface,
                                pygame.Color(150, 150, 150, 255),
                                rect,
                                width = 2)
                
    def get_mine_relative_amount(self, position):
        bombRelatives = 0
        for bomb in self.mineSpaces:
            distance = math.dist(position, bomb)
            if distance < math.sqrt(2.5): bombRelatives += 1
        return bombRelatives
                
    def draw_numbers(self, surface):
        for space in self.safeSpaces:
            bombRelatives = self.get_mine_relative_amount(space)
            if bombRelatives != 0:
                text_surface = pixelLetters.render(str(bombRelatives), True, (255, 255, 255))
                surface.blit(text_surface, pygame.Rect((windowSize[0]/self.size[0])*(space[0]-.65), (windowSize[0]/self.size[0])*(space[1]-.8), 255, 255))

    def draw_flagged_spaces(self, surface):
        for space in self.flaggedSpaces:
            pygame.draw.rect(surface,
                            'red',
                            pygame.Rect((windowSize[0]/self.size[0])*(space[0]-1), (windowSize[1]/self.size[1])*(space[1]-1), 50, 50))
            
    def hide_hidden_spaces(self, surface):
        for space in self.hiddenSpaces:
            rect = pygame.Rect((windowSize[0]/self.size[0])*space[0] - (windowSize[0]/self.size[0]),
                                   (windowSize[1]/self.size[1])*space[1] - (windowSize[1]/self.size[1]),
                                   (windowSize[0]/self.size[0]),
                                   (windowSize[0]/self.size[0]))
            pygame.draw.rect(surface,
                            pygame.Color(170, 170, 170, 255),
                            rect)
            pygame.draw.rect(surface,
                            pygame.Color(150, 150, 150, 255),
                            rect,
                            width=2)

    def mouse_to_space(self, mousePos):
        size = self.size
        position = (math.floor(mousePos[0]/(windowSize[0]/size[0])+1),
                    math.floor(mousePos[1]/(windowSize[1]/size[1])+1))
        return position
