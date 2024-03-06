import pygame
from pygame.locals import *
import random
import base64
import base64encode_decode


class Game:
    @staticmethod
    def draw_button(screen, x, y, width, height, text):
        button_font = pygame.font.Font(None, 36)
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, (0, 255, 0), button_rect)
        
        text_surface = button_font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)
        
        return button_rect
   
    

    def starting_game(self,colour):
        
       
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dodge the Obstacles")
        font = pygame.font.Font(None, 36)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        running = True
        colour_click = pygame.mixer.Sound("colour_click.mp3")
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.draw_button(screen, 350, 400, 100, 50, "Play").collidepoint(event.pos):
                        self.game(colour)
                        pygame.mixer.Sound.play(colour_click)
                    if self.draw_button(screen,350,460,150,50,"Costomise").collidepoint(event.pos):
                        colour = self.costomise()
                        pygame.mixer.Sound.play(colour_click)
            
            screen.fill(WHITE)
            text = font.render("Welcome to Dodge the Obstacles ", True, BLACK)
            screen.blit(text, (210, 240))
            self.draw_button(screen, 350, 400, 100, 50, "Play")
            self.draw_button(screen,325,460,150,50,"Costomise")
            
            pygame.display.update()
    def costomise(self):
        coin_file = open("coinscore.txt","r")
        temp = str(coin_file.read())
        ttemp = base64encode_decode.decode(temp)
        colour_file = open("colour_checker.txt","r")
        Colour_list_hold = []
        for line in colour_file:
            Colour_list_hold.append(line.strip())
        print (Colour_list_hold)
        colour_file.close()
        coin_file.close()
        
        
        coin_score = ttemp

        int(coin_score)
        pygame.init()
        
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dodge the Obstacles")
        font = pygame.font.Font(None, 36)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        running = True
        clock = pygame.time.Clock()
        colour = "Black"
        colour_click = pygame.mixer.Sound("colour_click.mp3")
        cost11 = 0
        cost22 = 5
        cost33 = 10
        cost44 = 25
        cost55 = 50
        cost66 = 100
        cost77 = 1000
        colour_index = 0
        while running:
            coin_file = open("coinscore.txt","w")
            hold = base64encode_decode.encode(coin_score)
            coin_file.write(hold)
            coin_file.close()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.draw_button(screen, 50, 400, 100, 50, "Black").collidepoint(event.pos) and coin_score >= 0 :
                        colour_index = 0
                        colour_file = open("colour_checker.txt","r")
                        Colour_list_hold = []
                        for line in colour_file:
                            Colour_list_hold.append(line.strip())
                       
                        colour_file.close()
                        if int(Colour_list_hold[colour_index]) == 0:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Black"
                            coin_score -= cost11
                            colour_file = open("colour_checker.txt","r+")
                            colour_file.seek(colour_index)
                            colour_file.write(str(1))
                            colour_file.close()
                        elif Colour_list_hold[colour_index] == 1:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Black"
                        else:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Black"
                       
                            
                    if self.draw_button(screen, 170,400,100,50, "Blue").collidepoint(event.pos) and coin_score >= 5:
                        colour_file = open("colour_checker.txt","r")
                        Colour_list_hold = []
                        for line in colour_file:
                            Colour_list_hold.append(line.strip())
                    
                        colour_file.close()
                        
                        colour_index = 1
                        if int(Colour_list_hold[colour_index]) == 0:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Blue"
                            coin_score -= cost22
                            colour_file = open("colour_checker.txt","r+")
                            colour_file.seek(colour_index+2)
                            colour_file.write(str(1))
                            colour_file.close()
                        elif int(Colour_list_hold[colour_index]) == 1:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Blue"
                        
                            
                        
                    if self.draw_button(screen, 290, 400, 100, 50, "Green").collidepoint(event.pos) and coin_score >= 10:
                        colour_file = open("colour_checker.txt","r")
                        Colour_list_hold = []
                        for line in colour_file:
                            Colour_list_hold.append(line.strip())
                     
                        colour_file.close()
                        colour_index = 2
                        if int(Colour_list_hold[colour_index]) == 0:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Green"
                            coin_score -= cost33
                            colour_file = open("colour_checker.txt","r+")
                            colour_file.seek(colour_index+4)
                            colour_file.write(str(1))
                            colour_file.close()
                        elif int(Colour_list_hold[colour_index]) == 1:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Green"
                          
                   
                    if self.draw_button(screen, 410,400,100,50, "Red").collidepoint(event.pos) and coin_score >= 25:
                        colour_file = open("colour_checker.txt","r")
                        Colour_list_hold = []
                        for line in colour_file:
                            Colour_list_hold.append(line.strip())
                      
                        colour_file.close()
                        colour_index = 3
                        if int(Colour_list_hold[colour_index]) == 0:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Red"
                            coin_score -= cost44
                            colour_file = open("colour_checker.txt","r+")
                            colour_file.seek(colour_index+6)
                            colour_file.write(str(1))
                            colour_file.close()
                        elif int(Colour_list_hold[colour_index]) == 1:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Red"
                          
                       
                    if self.draw_button(screen, 530, 400, 100, 50, "Pink").collidepoint(event.pos) and coin_score >= 50:
                        colour_file = open("colour_checker.txt","r")
                        Colour_list_hold = []
                        for line in colour_file:
                            Colour_list_hold.append(line.strip())
                    
                        colour_file.close()
                        colour_index = 4
                        if int(Colour_list_hold[colour_index]) == 0:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Pink"
                            colour_file = open("colour_checker.txt","r+")
                            colour_file.seek(colour_index+8)
                            colour_file.write(str(1))
                            colour_file.close()
                        elif int(Colour_list_hold[colour_index]) == 1:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Pink"
                          
                       
                    if self.draw_button(screen, 650,400,100,50, "Yellow").collidepoint(event.pos) and coin_score >= 100:
                       
                        colour_file = open("colour_checker.txt","r")
                        Colour_list_hold = []
                        for line in colour_file:
                            Colour_list_hold.append(line.strip())
                       
                        colour_file.close()
                        colour_index = 5
                        if int(Colour_list_hold[colour_index]) == 0:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Yellow"
                            coin_score -= cost66
                            colour_file = open("colour_checker.txt","r+")
                            colour_file.seek(colour_index+10)
                            colour_file.write(str(1))
                            colour_file.close()
                        elif int(Colour_list_hold[colour_index]) == 1:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Yellow"
                         
                        colour_index = 18
                    if self.draw_button(screen, 350, 470, 100, 50, "Orange").collidepoint(event.pos) and coin_score >= 1000 or self.draw_button(screen, 350, 470, 100, 50, "Orange").collidepoint(event.pos) and int(Colour_list_hold[colour_index]) == 1:
                        colour_file = open("colour_checker.txt","r")
                        Colour_list_hold = []
                        for line in colour_file:
                            Colour_list_hold.append(line.strip())
                        
                        colour_file.close()
                        colour_index = 6
                        if int(Colour_list_hold[colour_index]) == 0:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Orange"
                            coin_score -= cost77
                            colour_file = open("colour_checker.txt","r+")
                            colour_file.seek(colour_index+12)
                            colour_file.write(str(1))
                            colour_file.close()
                        elif int(Colour_list_hold[colour_index]) == 1:
                            
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Orange"
                        else:
                            pygame.mixer.Sound.play(colour_click)
                            colour = "Orange"
                            
                       
                    if self.draw_button(screen,700,15,90,50,"Return").collidepoint(event.pos):
                        pygame.mixer.Sound.play(colour_click)
                        return colour
            
            
            cost1 = 0
            cost2 = 5
            cost3 = 10
            cost4 = 25
            cost5 = 50
            cost6 = 100
            cost7 = 1000          
            
            screen.fill(WHITE)
            text = font.render("Welcome to the cosmetics store", True, BLACK)
            text2 = font.render("Pick your colour",True,BLACK)
            cost1 = font.render(f"Cost:{cost1}",True,BLACK)
            cost2 = font.render(f"Cost:{cost2}",True,BLACK)
            cost3 = font.render(f"Cost:{cost3}",True,BLACK)
            cost4 = font.render(f"Cost:{cost4}",True,BLACK)
            cost5 = font.render(f"Cost:{cost5}",True,BLACK)
            cost6 = font.render(f"Cost:{cost6}",True,BLACK)
            cost7 = font.render(f"Cost:{cost7}",True,BLACK)
            
            screen.blit(text, (210, 240))
            screen.blit(text2,(310,300))
            self.draw_button(screen, 50, 390, 100, 50, "Black")
            screen.blit(cost1,(62,444))
            self.draw_button(screen,170,390,100,50,"Blue")
            screen.blit(cost2,(170+12,444))
            self.draw_button(screen, 290, 390, 100, 50, "Green")
            screen.blit(cost3,(290+7,444))
            self.draw_button(screen,410,390,100,50,"Red")
            screen.blit(cost4,(410+7,444))
            self.draw_button(screen, 530, 390, 100, 50, "Pink")
            screen.blit(cost5,(537,444))
            self.draw_button(screen,650,390,100,50,"Yellow")
            screen.blit(cost6,(650,444))
            self.draw_button(screen, 350, 470, 100, 50, "Orange")
            screen.blit(cost7,(342,470+54))
            
            self.draw_button(screen,700,15,90,50,"Return")
            
            coin_surface = font.render("Coins: " + str(coin_score), True, BLACK)
            screen.blit(coin_surface, (10, 10))
            pygame.display.update()
            

    def game(self,colour):
        # Initialize Pygame
        pygame.init()
        GameDataFile = open("gamedata.txt","r")
        temp = str(GameDataFile.read())
        temp = base64encode_decode.decode(temp)
        
        highscore = temp
        int(highscore)
        GameDataFile.close()
        
        coin_file = open("coinscore.txt","r")
        temp = str(coin_file.read())
        ttemp = base64encode_decode.decode(temp)
        
       
        coin_score = ttemp
      
        int(coin_score)
        
        
        

        # Set up display
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dodge the Obstacles")

        # Set up colors
        past_self = ""
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        BROWN = (139, 69, 19)
        GREEN = (0, 128, 0)
        PINK = (232,37,212)
        ORANGE = (255,165,0)
        YELLOW = (255,255,0)
        BLUE = (8,221,253)
        if colour == "Red":
            past_self = colour
            colour = RED
        elif colour == "Blue":
            past_self = colour
            colour = BLUE
        elif colour == "Green":
            past_self = colour
            colour = GREEN
        elif colour == "Pink":
            past_self = colour
            colour = PINK
        elif colour == "Yellow":
            past_self = colour
            colour = YELLOW
        elif colour == "Orange":
            past_self = colour
            colour = ORANGE
        else:
            past_self = colour
            colour = BLACK
        # Set up fonts
        font = pygame.font.Font(None, 36)

        # Set up game variables
        
        player_x = 400
        player_y = 500
        player_width = 50
        player_height = 50
        player_alive = True
        not_been_played = True
        grass_has_been_drawn = random.randint(2,6)
        
        
        obstacle_width = 50
        obstacle_height = 50
        obstacle_x = random.randint(0, 750)
        obstacle_y = 0
        obstacle_speed = 20
        
        coin_number = 0
        coin_y = 510
        coin_x = 300
        placed = False
        coin_width = 36
        coin_radius = coin_width/2
        
        
        score = 0

        cloud_random_number = random.randint(0,2)
        if cloud_random_number == 0:
            cloud = pygame.image.load("clouds1.png")
        elif cloud_random_number == 1:
            cloud = pygame.image.load("clouds2.png")
        elif cloud_random_number == 2:
            cloud = pygame.image.load("clouds3.png")
        # Load tree image and grass
        tree_image = pygame.image.load("tree.png")
        num = random.randint(100,400)
        grass = pygame.image.load("grass.png")
        #load coin image
        coin = pygame.image.load("coin.png")
        #sound and music
        
        background_music = pygame.mixer.music.load('song_background.mp3')
        pygame.mixer.music.play(-1)
        sound_effects_death_sound = pygame.mixer.Sound('rock_sound.mp3')
        enemy_die = pygame.mixer.Sound('test_ground_hit.mp3')
        
        
        # Main game loop
        running = True
        clock = pygame.time.Clock()
        
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and player_alive == False:
                    if self.draw_button(screen, 350, 400, 100, 50, "Return").collidepoint(event.pos):
                        
                        
                        if score > int(highscore):
                            GameDataFile = open("gamedata.txt", "w")
                            
                            highscore = score
                            
                            hold = base64encode_decode.encode(highscore)
                            
                            GameDataFile.write(hold)
                            GameDataFile.close()
                        coin_file = open("coinscore.txt","w")
                        hold = base64encode_decode.encode(coin_score)
                        coin_file.write(hold)
                        coin_file.close()
                        self.starting_game(past_self)
                                        
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= 17
            if keys[pygame.K_RIGHT] and player_x < 750:
                player_x += 17
            if keys[pygame.K_a] and player_x > 0:
                player_x -= 17
            if keys[pygame.K_d] and player_x < 750:
                player_x += 17
            
            screen.fill(WHITE)
            pygame.draw.circle(screen,YELLOW,(10,10),80)
            # Draw background trees and clouds and grass
            for i in range(0, 800, num):
                screen.blit(tree_image, (i, 500))
            
            if cloud_random_number == 0:    
                screen.blit(cloud,(0,-150))
            elif cloud_random_number == 1:    
                screen.blit(cloud,(50,-80))
            elif cloud_random_number == 2:    
                screen.blit(cloud,(-150,-150))
            
            for i in range(0,800,grass_has_been_drawn):
                screen.blit(grass,(i,539))
                
                
            
            # Draw grass
            pygame.draw.rect(screen, GREEN, (0, 550, 800, 10))
            
            # Draw ground
            pygame.draw.rect(screen, BROWN, (0, 560, 800, 40))
    
            
            # Draw player
            if player_alive == True:
                pygame.draw.rect(screen, colour, (player_x, player_y, player_width, player_height))
            
            # Draw obstacle
                pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
            
            # Update obstacle position and speed based on score
            obstacle_y += obstacle_speed
            
            if obstacle_y >450 and not_been_played ==True :
                pygame.mixer.Sound.play(enemy_die)
                not_been_played = False
            if obstacle_y > 505 and player_alive == True:
                
                obstacle_y = 0
                obstacle_x = random.randint(0, 750)
                score += 1
                obstacle_speed = 20 + score // 2  # Increase speed every 5 points
                not_been_played = True
            if placed == False:
                coin_number = random.randint(1,180)
                if coin_number == 125:
                    coin_x = random.randint(50,700)
                    
                    
                    placed = True
            if placed  == True:
                
                screen.blit(coin,(coin_x,coin_y))
                if player_x < coin_x+ coin_radius and player_x +player_width> coin_x and player_alive == True:
                    placed = False
                    
                    
                    coin_score += 1
                    
                    
            # Check collision
            if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
                pygame.mixer.Sound.play(sound_effects_death_sound)
                obstacle_y = 0
                obstacle_x = random.randint(0, 750)
                obstacle_speed = 0
                player_alive = False
            if player_alive == False:
                pygame.mixer.music.stop()
            # Check for new high score
                
                if score >int(highscore):
                    end_surface3 = font.render("You have a new highscore! Congratulations!!!", True, BLACK)
                    screen.blit(end_surface3, (140, 290))
                
                    
                elif score < int(highscore):
                    end_surface2 = font.render(f"Try to beat your highscore of {highscore}", True, BLACK)
                    screen.blit(end_surface2, (230, 290))
                elif score == int(highscore):
                    end_surface2 = font.render(f"You tied the highscore of {highscore}. Don't Give Up!!!", True, BLACK)
                    screen.blit(end_surface2, (140, 290))
                
                    
                end_surface = font.render(f"You Died! Your score was {score}", True, BLACK)
                screen.blit(end_surface, (240, 240))
                
                self.draw_button(screen, 350, 400, 100, 50, "Return")
                
                
                
                    
                

                    
            
            # Display score
            score_surface = font.render("Score: " + str(score), True, BLACK)
            screen.blit(score_surface, (10, 10))
            
            pygame.display.flip()

            clock.tick(30)
        
        pygame.quit()
        
                
if __name__ == '__main__':
    colour = "black"
    game_instance = Game()
    
    game_instance.starting_game(colour)
    
