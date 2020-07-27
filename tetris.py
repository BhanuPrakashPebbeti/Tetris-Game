import pygame
import random
pygame.init()

red=(255,0,0)
red1=(255,51,51)
orange=(255,128,0)
orange1=(255,153,51)
yellow=(255,255,0)
green=(128,255,0)
green1=(0,255,0)
green2=(0,255,128)
blue=(0,255,255)
dblue=(0,128,255)
dblue1=(102,102,255)
violet=(127,0,255)
pink=(255,0,255)
dpink=(255,0,127)
white=(255,255,255)
dblack=(0,0,0)
black=(96,96,96)
grey=(192,192,192)
dgrey=(160,160,160)
brown=(102,51,0)
speed1=(204,255,255)
speed2=(204,255,204)
speed3=(255,255,204)
speed4=(255,204,153)
speed5=(255,153,153)

#title and logo
pygame.display.set_caption("TETRIS")
icon=pygame.image.load('tetris.png')
pygame.display.set_icon(icon)

#paused and game over logo and score logo
start_logo = pygame.image.load('tetris_start_logo.jpg')
paused_logo = pygame.image.load('paused logo.png')
score_logo = pygame.image.load('scorelogo.png')

# score board background
bg = pygame.image.load('tetris background.jpg')


#game screen creation
screen=pygame.display.set_mode((600,700))
clock=pygame.time.Clock()


#creating grid

grid = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]



#colours and shapes
colour = [dblack,dgrey,speed1,speed2,speed3,speed4,speed5,red,orange,yellow,blue,dpink,green1,dblue1]
top_left_x=0
top_left_y=50
class piece():
    def __init__(self):
        self.x = 7
        self.y = 0
        self.colour = random.randint(7,13)
        O = [[1,1],
             [1,1]]
        T = [[1,1,1],
             [0,1,0]]
        I = [[1,1,1,1]]
        L = [[1,0],
             [1,0],
             [1,1]]
        J = [[0,1],
             [0,1],
             [1,1]]
        S = [[0,1,1],
             [1,1,0]]
        Z = [[1,1,0],
             [0,1,1]]
        self.shape = random.choice([O,T,I,L,J,S,Z])
        self.height = len(self.shape)
        self.width = len(self.shape[0])
        self.next_shape = random.choice([O,T,I,L,J,S,Z])

        
    #creating shape
    def get_shape(self,grid):
        can_draw = True
        global can_use
        global game_finish
        for i in range(self.height):
            for j in range(self.width):
                if grid[i][self.x+j] != 0:
                    pygame.time.delay(800)
                    can_draw = False
                    can_use = False
                    break

        if can_draw:
            for i in range(self.height):
                for j in range(self.width):
                    if self.shape[i][j] == 1:
                        grid[self.y+i][self.x+j] = self.colour
            return grid
        else:
            game_finish = True


    #movement
    def move_left(self,grid):
        result = True
        for y in range(self.height):
            for x in range(self.width):
                if x == 0:
                    if self.shape[y][x] == 1:
                        if grid[self.y+y][self.x+(x-1)] != 0:
                            result = False
                else:
                    if self.shape[y][x] == 1 and self.shape[y][x-1] == 0:
                        if grid[self.y+y][self.x+(x-1)] != 0:
                            result = False
        if result:
            if self.x>0:
                game.erase(grid)
                self.x -= 1

    def move_right(self,grid):
        result = True
        for y in range(self.height):
            for x in range(self.width):
                if x == self.width-1:
                    if self.shape[y][x] == 1:
                        if grid[self.y+y][self.x+(x+1)] != 0:
                            result = False
                else:
                    if self.shape[y][x] == 1 and self.shape[y][x+1] == 0:
                        if grid[self.y+y][self.x+(x+1)] != 0:
                            result = False
        if result:
            if self.x<14:
                game.erase(grid)
                self.x += 1

    def erase(self,grid):
        for y in range(self.height):
            for x in range(self.width):
                if self.shape[y][x] == 1:
                    grid[self.y+y][self.x+x] = 0

    def can_move(self,grid):
        result = True
        for y in range(self.height):
            for x in range(self.width):
                if y<self.height-1 :
                    if self.shape[y][x] == 1 and self.shape[y+1][x] == 0:
                        if (grid[self.y+(y+1)][self.x+x]!=0):
                            result = False
                            break
                else:
                    if self.shape[y][x] == 1:
                        if (grid[self.y+(y+1)][self.x+x]!=0):
                            result = False
                            break
        return result

    def rotate(self,grid):
        self.erase(grid)
        rotate = True
        new_shape=[]
        for x in range(len(self.shape[0])):
            new_row=[]
            for y in range(len(self.shape)-1,-1,-1):
                new_row.append(self.shape[y][x])
            new_shape.append(new_row)
        right_of_rotated_shape=self.x + len(new_shape[0])

        for x in range(len(new_shape[0])):
            for y in range(1,len(new_shape)):
                if new_shape[y][x]==1:
                    if grid[self.y+y][self.x+x]!=0:
                        rotate = False
                        break

        if right_of_rotated_shape<13 and rotate:
            self.shape = new_shape
            self.height=len(new_shape)
            self.width=len(new_shape[0])



def check_grid(grid):
    y = 24
    while y > 0:
        filled = True
        for x in range(14):
            if grid[y][x]==0:
                filled = False
                y -= 1
                break
        if filled :
            for i in range(y,0,-1):
                for j in range(14):
                    grid[i][j]=grid[i-1][j]
            global num_line
            num_line+=1


#drawing grid
def create_grid(grid):
    game.get_shape(grid)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            pygame.draw.rect(screen,colour[grid[j][i]],(top_left_x+(i*25)+3,top_left_y+(j*25)+3,20,20))

def message_to_screen(q,size,colour,x,y,style):
    message = pygame.font.Font(style,size)
    messages = message.render(q,True,colour)
    screen.blit(messages,(x,y))

def score():
    message = pygame.font.Font('freesansbold.ttf',22)
    no_lines = message.render(str(num_line),True,white)
    scores = message.render(str(num_line*10),True,white)
    screen.blit(no_lines,(364,328))
    screen.blit(scores,(364,253))

def frame():

    pygame.draw.rect(screen,dblue,(0,0,350,50))
    pygame.draw.line(screen,yellow,(0,0),(350,0),10)
    pygame.draw.line(screen,yellow,(0,47),(350,47),5)
    message_to_screen("TETRIS",40,white,100,10,'freesansbold.ttf')
    screen.blit(bg,(350,-110))
    screen.blit(score_logo,(381,125))
    message_to_screen("SCORE :",23,white,361,225,'freesansbold.ttf')
    message_to_screen("LINES :",24,white,361,300,'freesansbold.ttf')
    message_to_screen("*Use Ctrl to change shape",15,white,361,53,"C:\Windows\Fonts\Arial.ttf")
    message_to_screen("*Use arrows to move",15,white,361,70,"C:\Windows\Fonts\Arial.ttf")
    message_to_screen("*Use Spacebar to pause",15,white,361,87,"C:\Windows\Fonts\Arial.ttf")
    pygame.draw.lines(screen,white,True,((361,250),(550,250),(550,275),(361,275)),1)
    pygame.draw.lines(screen,white,True,((361,325),(550,325),(550,350),(361,350)),1)


    for i in range(0,375,25):
        for j in range(0,725,25):
            pygame.draw.line(screen,white,(i,50),(i,700),1)
            if j>25:
                pygame.draw.line(screen,white,(0,j),(350,j),1)

def pause_frame():
    pygame.draw.rect(screen,dblue,(0,0,350,50))
    pygame.draw.line(screen,yellow,(0,0),(350,0),10)
    pygame.draw.line(screen,yellow,(0,47),(350,47),5)
    message_to_screen("TETRIS",40,white,100,10,'freesansbold.ttf')
    screen.blit(bg,(350,-110))
    screen.blit(score_logo,(381,125))
    message_to_screen("SCORE :",23,white,361,225,'freesansbold.ttf')
    message_to_screen("LINES :",24,white,361,300,'freesansbold.ttf')
    message_to_screen("*Use Ctrl to change shape",15,white,361,53,"C:\Windows\Fonts\Arial.ttf")
    message_to_screen("*Use arrows to move",15,white,361,70,"C:\Windows\Fonts\Arial.ttf")
    message_to_screen("*Use Spacebar to pause",15,white,361,87,"C:\Windows\Fonts\Arial.ttf")
    pygame.draw.lines(screen,white,True,((361,250),(550,250),(550,275),(361,275)),1)
    pygame.draw.lines(screen,white,True,((361,325),(550,325),(550,350),(361,350)),1)
    pygame.draw.rect(screen,dblack,(26,50,299,625))
    pygame.draw.line(screen,yellow,(0,0),(0,700),10)
    pygame.draw.line(screen,yellow,(350,0),(350,700),5)
    message_to_screen("PAUSED",64,white,50,250,'freesansbold.ttf')
    screen.blit(paused_logo,(120,100))
    message_to_screen("press spacebar to continue",20,white,50,500,'freesansbold.ttf')
    message_to_screen("press q to quit",20,white,100,532,'freesansbold.ttf')
    clock.tick(15)
    pygame.display.update()

def pause():
    paused = True
    while paused:
        pause_frame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                if event.key == pygame.K_SPACE:
                    paused = False
                    pygame.draw.rect(screen,dblack,(0,50,350,650))
        
        
def game_over():
    gameover = pygame.font.Font('freesansbold.ttf',45)
    game_overs = gameover.render('GAME OVER',True,white)
    frame()
    pygame.draw.rect(screen, dblack, (26, 50, 299, 625))
    screen.blit(game_overs,(35,250))
    screen.blit(paused_logo,(120,100))
    message_to_screen("press q to quit", 20, white, 100, 532,'freesansbold.ttf')
    pygame.display.update()

def change_border(grid,m):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (j==0 or j==13) and i != 25:
                grid[i][j] = m
            elif i == 25:
                grid[i][j] = m
    return grid

def start_game():
    screen.blit(start_logo,(-60,25))
    pygame.draw.rect(screen,dblue,(0,0,350,50))
    pygame.draw.line(screen,yellow,(0,0),(350,0),10)
    pygame.draw.line(screen,yellow,(0,47),(350,47),5)
    message_to_screen("TETRIS",40,white,100,10,'freesansbold.ttf')
    screen.blit(bg,(350,-110))
    screen.blit(score_logo,(381,125))
    message_to_screen("SCORE :",23,white,361,225,'freesansbold.ttf')
    message_to_screen("LINES :",24,white,361,300,'freesansbold.ttf')
    message_to_screen("*Use Ctrl to change shape",15,white,361,53,"C:\Windows\Fonts\Arial.ttf")
    message_to_screen("*Use arrows to move",15,white,361,70,"C:\Windows\Fonts\Arial.ttf")
    message_to_screen("*Use Spacebar to pause",15,white,361,87,"C:\Windows\Fonts\Arial.ttf")
    pygame.draw.lines(screen,white,True,((361,250),(550,250),(550,275),(361,275)),1)
    pygame.draw.lines(screen,white,True,((361,325),(550,325),(550,350),(361,350)),1)
    pygame.draw.line(screen,yellow,(0,0),(0,700),10)
    pygame.draw.line(screen,yellow,(350,0),(350,700),5)
    message_to_screen('press "s" to start game',20,white,75,590,'freesansbold.ttf')
    clock.tick(15)
    pygame.display.update()

# Score
num_line = 0
game=piece()
running = True
game_finish = False
can_use = True
delay = 550
start = True

while running:
    screen.fill(dblack)
    while game_finish == True:
        game_over()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    pygame.quit()
    while start == True:
        start_game()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    start = False
                    pygame.draw.rect(screen,dblack,(0,50,350,650))
        
    if game.y == 24-game.height+1 :
        game = piece()
        check_grid(grid)

    elif game.can_move(grid):
        game.erase(grid)
        pygame.time.delay(delay)
        game.y += 1

    else:
        game = piece()
        check_grid(grid)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()
            elif event.key == pygame.K_LEFT:
                game.move_left(grid)
            elif event.key == pygame.K_RIGHT:
                game.move_right(grid)
            elif event.key == pygame.K_LCTRL:
                if can_use:
                    game.rotate(grid)
            elif event.key == pygame.K_DOWN:
                while game.can_move(grid):
                    game.y+=1

    if num_line>10 and num_line<=18 :
        delay = 450
        change_border(grid,2)
    elif num_line>28 and num_line<=36 :
        delay = 350
        change_border(grid,3)
    elif num_line>46 and num_line<=54 :
        delay = 275
        change_border(grid,4)
    elif num_line>64 and num_line<=72 :
        delay = 225
        change_border(grid,5)
    elif num_line>82 and num_line<=90 :
        delay = 175
        change_border(grid,6)
    else:
        delay = 550
        change_border(grid,1)


    create_grid(grid)
    frame()
    score()
    clock.tick(20)
    pygame.display.update()