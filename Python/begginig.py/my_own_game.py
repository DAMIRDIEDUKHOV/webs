import pygame
pygame.init()

PF_SIZE = PF_WIDTH, PF_HEIGHT = 32, 32

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('platform.png')
        self.rect = pygame.Rect(x, y, PF_WIDTH, PF_HEIGHT)

DISPLAY = WIN_WIDTH, WIN_HEIGHT = 800, 800
BG_COLOR = (50, 20, 200)

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0,0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           
    l = max(-(camera.width-WIN_WIDTH), l)   
    t = max(-(camera.height-WIN_HEIGHT), t) 
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

def main():
    pygame.init()
    mw = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('New Rocket League')
    bg = pygame.Surface(DISPLAY)
    bg.fill(BG_COLOR)
    clock = pygame.time.Clock()

    entities = pygame.sprite.Group()
    platforms = []


    level = [
        '-------------------------------------------------',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-         -----                                 -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-                 ---             ---------     -',
        '-                                               -',
        '-                                               -',
        '-                                               -',
        '-            ---------                          -',
        '-                                               -',
        '-                                               -',
        '-                        --                     -',
        '-                                               -',
        '-                                               -',
        '-                               ------          -',
        '-        ------------                           -',
        '-                                               -',
        '-                                               -',
        '-                        -----                  -',
        '-                                               -',
        '-                                    ----       -',
        '-                                               -',
        '-------------------------------------------------']

    x = y = 0
    for row in level:
        for symbol in row:
            if symbol == '-':
                pf = Platform.Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += Platform.PF_WIDTH
        x = 0
        y += Platform.PF_HEIGHT
        
    total_width = len(level[0])*Platform.PF_WIDTH
    total_height = len(level)*Platform.PF_HEIGHT
    camera = Camera(camera_configure, total_width, total_height)

     
    hero = Player.Player(50, total_height - 100)
    entities.add(hero)
    left = right = up = False
    Game = True
    while Game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                Game = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    up = True
                if e.key == pygame.K_a:
                    left = True
                if e.key == pygame.K_d:
                    right = True
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_w:
                    up = False
                if e.key == pygame.K_a:
                    left = False
                if e.key == pygame.K_d:
                    right = False

# Player A
MOVE_SPEED = 7
SIZE = WIDTH, HEIGHT = 22, 32
COLOR = (150,20,240)
JUMP_POWER = 10
GRAVITY = 0.3

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.onGround = False
        self.xvel = 0
        self.yvel = 0
        self.startx = x
        self.starty = y
        self.image = pygame.Surface(SIZE)
        self.image.fill(COLOR)
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                if left:
                    self.xvel = -MOVE_SPEED
                if right:
                    self.xvel = MOVE_SPEED
                    if not(left or right):
                            self.xvel = 0
                        if not self.onGround:
                                self.yvel += GRAVITY

        self.onGround = False
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, Platform)

        self.rect.y += self.yvel
        self.collide(0, self.yvel, Platform)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0
                    
mw.blit(bg, (0,0))
hero.update(left, right, up, platforms)
camera.update(hero)
for e in entities:
    mw.blit(e.image, camera.apply(e))
if True:
    pygame.display.update()
    clock.tick(60)
    