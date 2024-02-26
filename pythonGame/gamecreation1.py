import pygame
from pygame.locals import *
import random

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
        clock = pygame.time.Clock()
        
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.draw_button(screen, 350, 400, 100, 50, "Play").collidepoint(event.pos):
                        self.game(colour)
                    if self.draw_button(screen,350,460,150,50,"Costomise").collidepoint(event.pos):
                        colour = self.costomise()
            
            screen.fill(WHITE)
            text = font.render("Welcome to Dodge the Obstacles ", True, BLACK)
            screen.blit(text, (210, 240))
            self.draw_button(screen, 350, 400, 100, 50, "Play")
            self.draw_button(screen,325,460,150,50,"Costomise")
            
            pygame.display.update()
    def costomise(self):
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Dodge the Obstacles")
        font = pygame.font.Font(None, 36)
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        running = True
        clock = pygame.time.Clock()
        colour = "Black"
        
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.draw_button(screen, 50, 400, 100, 50, "Red").collidepoint(event.pos):
                        colour = "Red"
                    if self.draw_button(screen, 170,400,100,50, "Blue").collidepoint(event.pos):
                        colour = "Blue"
                    if self.draw_button(screen, 290, 400, 100, 50, "Green").collidepoint(event.pos):
                        colour = "Green"
                    if self.draw_button(screen, 410,400,100,50, "Black").collidepoint(event.pos):
                        colour = "Black"
                    if self.draw_button(screen, 530, 400, 100, 50, "Pink").collidepoint(event.pos):
                        colour = "Pink"
                    if self.draw_button(screen, 650,400,100,50, "Yellow").collidepoint(event.pos):
                        colour = "Yellow"
                    if self.draw_button(screen, 350, 470, 100, 50, "Orange").collidepoint(event.pos):
                        colour = "Orange"
                    if self.draw_button(screen,700,15,90,50,"Return").collidepoint(event.pos):
                        return colour
                    
                        
            
            screen.fill(WHITE)
            text = font.render("Welcome to the cosmetics store", True, BLACK)
            text2 = font.render("Pick your colour",True,BLACK)
            screen.blit(text, (210, 240))
            screen.blit(text2,(310,300))
            self.draw_button(screen, 50, 400, 100, 50, "Red")
            self.draw_button(screen,170,400,100,50,"Blue")
            self.draw_button(screen, 290, 400, 100, 50, "Green")
            self.draw_button(screen,410,400,100,50,"Black")
            self.draw_button(screen, 530, 400, 100, 50, "Pink")
            self.draw_button(screen,650,400,100,50,"Yellow")
            self.draw_button(screen, 350, 470, 100, 50, "Orange")
            
            
            self.draw_button(screen,700,15,90,50,"Return")
            
            pygame.display.update()
            

    def game(self,colour):
        # Initialize Pygame
        pygame.init()
        GameDataFile = open("gamedata.txt","r")
        highscore = int(GameDataFile.read())
        GameDataFile.close()

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
                        
                        
                        if score > highscore:
                            GameDataFile = open("gamedata.txt", "w")
                            highscore = score
                            GameDataFile.write(str(highscore))
                            GameDataFile.close()
                        self.starting_game(past_self)
                                        
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= 22
            if keys[pygame.K_RIGHT] and player_x < 750:
                player_x += 22
            
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
                obstacle_speed = 28 + score // 2  # Increase speed every 5 points
                not_been_played = True
            
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
                
                if score >highscore:
                    end_surface3 = font.render("You have a new highscore! Congratulations!!!", True, BLACK)
                    screen.blit(end_surface3, (140, 290))
                    
                    
                elif score < highscore:
                    end_surface2 = font.render(f"Try to beat your highscore of {highscore}", True, BLACK)
                    screen.blit(end_surface2, (230, 290))
                elif score == highscore:
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
        print(highscore)
        if score > highscore:
            GameDataFile = open("gamedata.txt", "w")
            highscore = score
            GameDataFile.write(str(highscore))
            GameDataFile.close()
        print(highscore)
                
if __name__ == '__main__':
    colour = "black"
    game_instance = Game()
    try:
        game_instance.starting_game(colour)
    except pygame.error:
        print("error that i don't know how to fix.\n help if you can")
        


