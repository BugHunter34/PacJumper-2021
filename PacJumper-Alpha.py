import pygame, sys, random, time
#
def draw_bg_image():
    screen.blit(bg_image,(bg_x_pos, bg_y_pos))
    screen.blit(bg_image,(bg_x_pos + 1534, bg_y_pos))

def draw_floor_image():
    screen.blit(floor,(floor_x_pos, floor_y_pos))
    screen.blit(floor,(floor_x_pos + 1534, floor_y_pos))

def create_prekazka():
    random_prekazka_pos = random.choice(prekazka_height)
    new_prekazka = prekazka_surface.get_rect(midtop = (1534,random_prekazka_pos))
    return new_prekazka

def move_prekazky(prekazky): 
    for prekazka in prekazky:
            prekazka.centerx -= 2
    return prekazky
  
def draw_prekazky(prekazky):
    for prekazka in prekazky:
            screen.blit(prekazka_surface,prekazka)  
    
 
def check_collision(prekazky):
    for prekazka in prekazky:
		        if player_rect.colliderect(prekazka):  
                            player_death.play() 
                            return False   
    if player_rect.top <= -200 or player_rect.bottom >= 1000:
                            player_death.play()
                            return False
    return True

#def rotate_player(player):
    #new_player = pygame.transform.rotozoom(player,-player_movement * 0,1)
    #return new_player

def score_display(game_state):
    if game_state == 'game_main':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (767, 50))
        screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score:{(int(score))}',True,(255,255,255))
        score_rect = score_surface.get_rect(center = (767, 50))
        screen.blit(score_surface,score_rect)
    




        #high_score_surface = game_font.render(f'high score:{(int(score))}',True,(255,255,255))
        #high_score_rect = high_score_surface.get_rect(center = (500, 100))
        #screen.blit(high_score_surface,high_score_rect)
 
#def update_score(score, high_score):
    #if score > high_score:
        #high_score = score
    #return high_score

def PLAYCONGRATULATION():
    congratulation.play()


def tajuplne_heslo():
         if tajne_heslo == 121: 
            screen.blit(tajne_heslo_obrazek,tajne_heslo_rect)
            
            PLAYCONGRATULATION()
            
            aktualni_cas()

            high_score_surface = game_font.render(str(int(winer_score)),True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (767, 350))
            screen.blit(high_score_surface,high_score_rect)

            high_score_surface = game_font.render(str(int(winer_score)),True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (767, 400))
            screen.blit(high_score_surface,high_score_rect)

            high_score_surface = game_font.render(str(int(winer_score)),True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (767, 450))
            screen.blit(high_score_surface,high_score_rect)

            high_score_surface = game_font.render(str(int(winer_score)),True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (767, 500))
            screen.blit(high_score_surface,high_score_rect)

            high_score_surface = game_font.render(str(int(winer_score)),True,(255,255,255))
            high_score_rect = high_score_surface.get_rect(center = (767, 550))
            screen.blit(high_score_surface,high_score_rect)

        

def aktualni_cas():
    time_surface = game_font2.render(f'you win in {(aktualni_cas_1)} time',True,(255,0,0))
    time_rect = time_surface.get_rect(center = (767, 90))
    screen.blit(time_surface,time_rect)
        
def ukoncit_hru():
    if konec_hry >= 2: 
        pygame.quit()
        sys.exit()




    


#
#pygame.mixer.pre_init(frequency = 48100, size = 16, channels = 1, buffer = 512)
pygame.init()

#
screen = pygame.display.set_mode((1534, 800))
clock = pygame.time.Clock()

game_font = pygame.font.Font('text_font/Anita semi square.ttf',40)

game_font2 = pygame.font.Font('text_font/Anita semi square.ttf',40)
#SCORETIMER = pygame.USEREVENT
#pygame.time.set_timer(SCORETIMER,100)

#
gravity = 0.10
player_movement = 0
game_active = True 
score = 0
winer_active = True
high_score = 0
hlasitost_hudby = 1
winer_score = 9999999999999999999999999999999999999999999999
aktualni_cas_1 = time.strftime("%d/%m/%Y %H:%M:%S")
rychlost_spawnovani_prekazky = 1500
tik_hry = 300
konec_hry = 0
 

#
floor = pygame.image.load('obrazky_pygame/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
floor_y_pos = 400

bg_image = pygame.image.load('obrazky_pygame/water1.png').convert()
bg_image = pygame.transform.scale2x(bg_image)
bg_x_pos = 0
bg_y_pos = 0

player = pygame.image.load('obrazky_pygame/pacman1.png').convert_alpha()
player_rect = player.get_rect(center = (100,295))

bg_music1 = pygame.mixer.Sound('music_pygame/Foster the People-music.mp3')
bg_music2 = pygame.mixer.Sound('music_pygame/Cartoon  On  On feat Daniel Levi NCS Release.mp3')
bg_music3 = pygame.mixer.Sound('music_pygame/Warriyo  Mortals feat Laura Brehm NCS Release.mp3')
bg_music4 = pygame.mixer.Sound('music_pygame/Jarico  Island NCS BEST OF.mp3')
bg_music5 = pygame.mixer.Sound('music_pygame/ElectroLight  Symbolism NCS Release.mp3')
bg_music6 = pygame.mixer.Sound('music_pygame/Debris  Jonth  Game Time NCS Release.mp3')








player_jump_sound = pygame.mixer.Sound('music_pygame/Mario Jump Sound Effect.mp3')

player_death = pygame.mixer.Sound('music_pygame/Roblox Death Sound Effect.mp3')

congratulation = pygame.mixer.Sound('music_pygame/congratulations-sound-effect.mp3')




  


prekazka_surface = pygame.image.load('obrazky_pygame/prekazka1.png')
prekazka_surface = pygame.transform.scale2x(prekazka_surface)
prekazka_list = []
SPAWNPREKAZKA = pygame.USEREVENT
pygame.time.set_timer(SPAWNPREKAZKA,rychlost_spawnovani_prekazky)
prekazka_height = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800]

tajne_heslo_obrazek = pygame.image.load('obrazky_pygame/you_win.png').convert()
tajne_heslo_rect = tajne_heslo_obrazek.get_rect(center = (768,220))


game_over_surface = pygame.transform.scale2x (pygame.image.load('obrazky_pygame/game_over1.png').convert())
game_over_rect = game_over_surface.get_rect(center = (768,220))


tajne_heslo = 0
#
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:

            

            

            if event.key == pygame.K_LSHIFT:
                    bg_music1.stop()
                    bg_music2.stop()
                    bg_music3.stop()
                    bg_music4.stop()
                    bg_music5.stop()
                    bg_music6.stop()

            if event.key == pygame.K_ESCAPE:
                    konec_hry += 1

            if event.key == pygame.K_F1:
                bg_music1.play()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
            if event.key == pygame.K_F2:
                bg_music1.stop()
                bg_music2.play()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
            if event.key == pygame.K_F3:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.play()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
            if event.key == pygame.K_F4:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.play()
                bg_music5.stop()
                bg_music6.stop()
            if event.key == pygame.K_F5:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.play()
                bg_music6.stop()
            if event.key == pygame.K_F6:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.play()


                   

            
                   

            if event.key == pygame.K_1:
                tajne_heslo += 1
            if event.key == pygame.K_2:
                tajne_heslo += 2
            if event.key == pygame.K_3:
                tajne_heslo += 3
            if event.key == pygame.K_4:
                tajne_heslo += 4
            if event.key == pygame.K_5:
                tajne_heslo += 5
            if event.key == pygame.K_6:
                tajne_heslo += 6
            if event.key == pygame.K_7:
                tajne_heslo += 7
            if event.key == pygame.K_8:
                tajne_heslo += 8
            if event.key == pygame.K_9:
                tajne_heslo += 9
            if event.key == pygame.K_0:
                tajne_heslo += 0
            if event.key == pygame.K_DELETE:
                tajne_heslo = 0

            if event.key == pygame.K_SPACE and game_active:
                    #player_jump_sound.play()
                    player_movement = 0
                    player_movement -= 3

            if event.key == pygame.K_LALT and game_active == False:
                    game_active = True
                    
                    prekazka_list.clear()
                    score = 0
                    player_rect.center = (100,295)
                    player_movement = 0
                    rychlost_spawnovani_prekazky = 1200
                    tik_hry = 300
                

            
                    
            
        if event.type == SPAWNPREKAZKA and game_active: 
                prekazka_list.append(create_prekazka())
                #rychlost_spawnovani_prekazky += 10
                #tik_hry += 1



        
                
        

 

        #if event.type == SCORETIMER and game_active:
                #score += 1


    #bacground
    draw_bg_image()
    if bg_x_pos <= -1534:
        bg_x_pos = 0
    bg_x_pos -= 1
  

    # floor
    #draw_floor_image()
    if floor_x_pos <= -1534:
        floor_x_pos = 0
    floor_x_pos -= 1

    
    


    if game_active:
        # player
        player_movement += gravity
        #rotated_player = rotate_player(player)
        player_rect.centery += player_movement
        screen.blit(player,player_rect)#(rotated_player)
        game_active = check_collision(prekazka_list)


        #prekazky
        prekazka_list = move_prekazky(prekazka_list) 
        draw_prekazky(prekazka_list)
    
        #score
        score_display('game_main')
        score += 0.01
    else:
        screen.blit(game_over_surface,game_over_rect)
        #high_score = update_score(score, high_score)
        score_display('game_over')

    
    tajuplne_heslo()
    
    ukoncit_hru()  
    
    
        





    #
    pygame.display.update()
    clock.tick(tik_hry)