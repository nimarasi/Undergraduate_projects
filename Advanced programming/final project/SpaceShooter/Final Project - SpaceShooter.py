import pygame
import os
import random

pygame.init()
# page size
win_x, win_y = 750, 500
win = pygame.display.set_mode((win_x, win_y))
# caption for game
pygame.display.set_caption("Space shooter")
# make background in special size with special pic
bg = pygame.transform.scale(pygame.image.load("characters/background-black.png"), (win_x, win_y))

# load pics and save them in a variable
player_label = pygame.image.load("characters/playerShip2_green.png")
enemy_red_label = pygame.image.load("characters/ufoRed.png")
enemy_blue_label = pygame.image.load("characters/ufoBlue.png")
enemy_yellow_label = pygame.image.load("characters/ufoYellow.png")
fire_player_label = pygame.image.load("characters/fire01.png")
fire_enemy_label = pygame.image.load("characters/fire02.png")


# common class between Player and Enemies
class ship:
    COOLDOWN = 3
    def __init__(self, x, y, height, width, img, live=3):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 10
        self.ship_label = img
        self.fire_label = None
        self.fires = []
        self.live = live
        self.cool_down_counter = 0

    # a method to draw Player in window
    def draw(self, win):
        win.blit(self.ship_label, (self.x, self.y))  # draw player with with ship_label and in x & y place in window
        for fire in self.fires:
            fire.draw(win)
    # this method controls delay between fires
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter >= 0:
            self.cool_down_counter += 1
    # a method to shoot enemies and Player fires
    def shoot(self, score):
        if self.cool_down_counter >= self.COOLDOWN:# when cool_down_counter == 3(self.COOLDOWN) below lines will run
            if type(self) == enemy and 500>self.y>0:
                Fire = fire(self.x + 39 ,self.y + 70, 30,15,self.fire_label)
                self.fires.append(Fire)
            if len(self.fires) < score :# this if command controls numbers of fire that player can fire instead of score
                Fire = fire(self.x + 49, self.y + 3, 30, 15, self.fire_label)# make a Fire from fire class from mouth of ship
                self.fires.append(Fire)
        self.cooldown()




# a class for fires in Player and Enemeis
class fire:
    def __init__(self, x, y, height, width, img):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.img = img

    # a method to draw fires with special img and in special x&y
    def draw(self, win):
        win.blit(self.img, (self.x, self.y))
        # Line below makes visible our collision domain around fires
        # pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)

    # a method to move fire
    def move(self, vel):
        self.y += vel

    # a method to diagnosis that if the fire is out of screen please return True else return Falase
    def out_sreen(self, height):
        return not (self.y <= height and self.y >= 0)

    # a method to detect collision between fire and enemies with using def detectCollisions in lines below
    def collision(self, obj):
        # if there is collision between fire and enemy return True else return False
        return detectCollisions(self.x, self.y, self.width, self.height, obj.x, obj.y, obj.width, obj.height)


# a class for our Player
class player(ship):
    def __init__(self, x, y, height, width, img, live=3):
        super().__init__(x, y, height, width, img, live)
        self.fire_label = fire_player_label
        self.score = 0


    # a method to move Player fires
    def move_fire(self, vel, objs):

        # for loop to move Player fire
        for fire in self.fires:  # for each fires that are in self.fires = [] in ship class Perform the following operation
            fire.move(vel)  # use move method in fire class to move the fire
            if fire.out_sreen(win_y):  # check if the fire is out of screen remove it form self.fires = [] else do things below
                self.fires.remove(fire)
            else:
                for obj in objs:  # objs are our enemies move on enemies that are in enemies = []
                    if fire.collision(obj):  # check collision between fire and enemy if True do things below
                        if obj.live == 1:  # if enemy live == 0 do things below
                            self.fires.remove(fire)  # remove fire from self.fire = []
                            objs.remove(obj)  # remove enemy from enemies = []
                            Player.score += 5  # add 5 to Player score
                        if fire in self.fires:  # if fire is in self.fires = [] remove fire from self.fires = [] and decrease 1 from enemy live
                            self.fires.remove(fire)
                            obj.live -= 1

    def healthbar(self):
            pygame.draw.rect(win,(255,0,0),(Player.x + 22, Player.y + 80, Player.width - 30 , Player.height - 40),0)
            pygame.draw.rect(win, (0, 255 , 0), (Player.x + 22, Player.y + 80, (Player.width - 30) * (Player.live / 3), Player.height - 40), 0)





# a class for Enemies
class enemy(ship):
    # class attribute for enemies
    enemy_color = {"RED": enemy_red_label,
                   "BLUE": enemy_blue_label,
                   "YELLOW": enemy_yellow_label}

    def __init__(self, x, y, height, width, color, live=3):
        img = self.enemy_color[color]
        super().__init__(x, y, height, width, img, live)
        self.fire_label = fire_enemy_label
    def move_fire(self,vel,Playerobj):

        for fire in self.fires:
            if fire.img == fire_enemy_label:
                fire.move(vel)
                if fire.out_sreen(win_y):
                    self.fires.remove(fire)
                elif fire.collision(Playerobj):
                    Player.live -= 1
                    self.fires.remove(fire)
    # method to move enemy
    def move(self, vel):
        self.y += vel


def detectCollisions(x1, y1, w1, h1, x2, y2, w2, h2):
    # if point top left of obj1 is beetween square of obj2 which around obj2 return True
    if (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 >= y2):

        return True
    # elif point top right of obj1 is beetween square of obj2 which around obj2 return True
    elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 >= y2):

        return True
    # elif point bottom left of obj1 is beetween square of obj2 which around obj2 return True
    elif (x2 + w2 >= x1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

        return True
    # elif point bottom right of obj1 is beetween square of obj2 which around obj2 return True
    elif (x2 + w2 >= x1 + w1 >= x2 and y2 + h2 >= y1 + h1 >= y2):

        return True

    else:

        return False

# make our Player obj with self.x = 310 | self.y = 390 | self.height = 48 | self.width = 100 | self.img = player_label
Player = player(310, 390, 48, 100,player_label)


# main game def
def main():
    level = 0  # variable for level
    hour, minute, second = 0, 0, 0  # variables for time
    time_counter = 0  # a counter for time that we will use in our main loop
    main_font = pygame.font.SysFont("comicsans",40)  # define a font with comicscan style and size 40 and save in main_font
    lost_font = pygame.font.SysFont("comicsans",50)  # define a font with comicscan style and size 50 and save in lost_font
    lost = False  # from the beginning of game lost is False if lost equals True if game loop the game will finish
    lost_time = 0  # a timer that how many seconds game window does not closes after losing
    enemies = []  # a list for enemies that we will save them
    add_enemy = 0  # a variable to adding enemy in each level
    enemy_vel = 0  # set 0 velacity for our enemy at first
    fire_vel = 10  # our fire velacity is 4
    bgY = 0
    # draw BG and our Player and Enemies and Player bullets and Enemy bullets and Live_font and Time_font
    def drawgameWindow():
        # draw two BG that are sticked together and helps us to show that BG in moving
        win.blit(bg, (0, bgY))
        win.blit(bg, (0, bgY - 500))

        Player.draw(win)  # use draw method in player class to draw our player
        # Line below makes visible our collision domain around our Player
        # pygame.draw.rect(win, (255, 0, 0), (Player.x + 6, Player.y + 28, Player.width, Player.height), 1)
        if not lost:
            Player.healthbar()
        else:
            pygame.draw.rect(win, (255, 0, 0), (Player.x + 22, Player.y + 80, Player.width - 30, Player.height - 40), 0)
        # for loop to draw enemies that are in enemies = []
        for enemy_move in enemies:
            enemy_move.draw(win)  # use draw method that is in class enemy
        score_label = main_font.render(f"Score : {Player.score}", 1,
                                       (255, 255, 255))  # choose a format and color and font to our score_label
        time_label = main_font.render("Time : {:02}:{:02}:{:02}".format(hour, minute, second), 1,(255, 255, 255))  # choose a format and color and font to our time_label
        win.blit(time_label,(win_x - time_label.get_width() - 10, 5))  # time_label.get_width() calculate our time_label size
        win.blit(score_label, (5, 5))

        if lost:  # if lost is True print lost_label
            lost_label = lost_font.render(f"You Lose!!...", 1, (255, 255, 255))
            win.blit(lost_label, (270, 220))

    run = True  # run is True

    # main while loop for our game
    while run:
        pygame.time.delay(30)  # make a delay in game to control speed of game we can increase or decrease it
        win.fill((0, 0, 0))
        bgY += 3  # move our BG
        if bgY > 500:  # if first BG is out of screen put 0 in bgY and restart to move first BG from y = 0
            bgY = 0
        time_counter += 1  # in each time loop runs add 1 to time_counter
        if time_counter == 16:  # if while run loop runs 16 time

            if lost:  # check that Player is loser or not if is True stop timer below lines with continue command
                continue
            time_counter = 0  # put 0 to time_counter
            # lines below to make a simple time counter
            if second > 59:
                second = 0
                minute += 1
            if minute > 59:
                minute = 0
                hour += 1
            second += 1

        drawgameWindow()  # use a def drawgameWindow to draw things that we define in it

        # for loop to move move enemies that have made before in lines below and are in enemies = []
        for enemyy in enemies:
            if level == 1:
                enemyy.move(1.5)  # use move that is in enemy class to move enemy
            if level > 1:
                enemyy.move(level/2)
            if random.randrange(0, 30) == 1:
                    enemyy = random.choice(enemies)
                    enemyy.shoot(Player.score)

            enemyy.move_fire(level/2 + 2,Player)
            # Line below makes visible our collision domain for enemy
            # pygame.draw.rect(win, (255, 0, 0), (enemyy.x + 5, enemyy.y + 6, enemyy.width, enemyy.height), 1)
            if detectCollisions(enemyy.x + 5, enemyy.y + 6, enemyy.width, enemyy.height, Player.x + 6, Player.y + 28,Player.width,
                                Player.height):  # check collision between enemy and our Player
                # if there is collision between our enemy and Player decrease 1 from our Player.live an remove enemy from enemies = []
                Player.live -= 1
                enemies.remove(enemyy)
            elif enemyy.y + enemyy.height > win_y:  # elif enemy is out of screen decrease 1 from our Player.live and remove enemy from enemies = []
                Player.live -= 1
                enemies.remove(enemyy)


        Player.move_fire(-fire_vel,enemies)  # use move_fire method in player class to move fire and check there is collision between our fire and enemy or not

        pygame.display.update()  # update new events that occurs in our screen to see them
        if Player.live <= 0:  # if Player.live is 0 put True in lost and increase 1 to lost_time
            lost = True
            lost_time += 1
        if lost:  # if lost True
            if lost_time > 200:  # if lost time is greater than 200 run == False to quit the loop else continue
                exit(0)
            else:
                continue

        if len(enemies) == 0:  # if the enemies = [] is empty add 1 to level and add 1 to enemeis
            level += 1
            add_enemy += 1
            for i in range(add_enemy):  # make enemy as many as add_enemy
                Enemy = enemy(random.randrange(5, win_x - 100), random.randrange(-800, -100), 81, 81,
                              random.choice(["RED", "BLUE",
                                             "YELLOW"]))  # (choose a random x, choose random y , choose random color)
                enemies.append(Enemy)  # add Enemy which is object from enemy class to enemies = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(-1)

        keys = pygame.key.get_pressed() # get the state of all keyboard buttons
        if keys[pygame.K_a] and Player.x  >= Player.vel:  # move Player to left
            Player.x -= Player.vel
        if keys[pygame.K_d] and Player.x + Player.width + 12 < win_x:  # move Player to right
            Player.x += Player.vel
        if keys[pygame.K_w] and Player.y >= Player.vel:  # move Player to up
            Player.y -= Player.vel
        if keys[pygame.K_s] and Player.y + Player.height + 30 < win_y:  # move Player to down
            Player.y += Player.vel
        if keys[pygame.K_SPACE]:#if user press space shoot fire from Player with using shoot method in ship class
            if Player.score == 0:
                Player.shoot(1)
            else:
                Player.shoot(Player.score//5)

def main_menu():
    """
    game starts with mouse click of user
    """
    start_font = pygame.font.SysFont("comicsans", 60)
    run = True
    while run:
        win.blit(bg, (0,0))
        start_label = start_font.render("Press Mouse to begin...",1, (255,255,255))
        win.blit(start_label, (160, 220))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
            elif event.type == pygame.QUIT:
                exit(0)


main_menu()
