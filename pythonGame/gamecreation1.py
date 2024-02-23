import pygame
import random
from time import sleep
def game():
    # Initialize Pygame
    pygame.init()
    GameDataFile = open("gamedata.txt","r")
    highscore = int(GameDataFile.read())
    GameDataFile.close()

    # Set up display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Dodge the Obstacles")

    # Set up colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BROWN = (139, 69, 19)
    GREEN = (0, 128, 0)
    GRAY = (220,220,220)

    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Set up game variables
    player_x = 400
    player_y = 500
    player_width = 50
    player_height = 50
    player_alive = True


    obstacle_width = 50
    obstacle_height = 50
    obstacle_x = random.randint(0, 750)
    obstacle_y = 0
    obstacle_speed = 10

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
    # Main game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= 10
        if keys[pygame.K_RIGHT] and player_x < 750:
            player_x += 10
        
        screen.fill(WHITE)
        pygame.draw.circle(screen,(255,255,0),(10,10),80)
        # Draw background trees and clouds and grass
        for i in range(0, 800, num):
            screen.blit(tree_image, (i, 500))
        for i in range(0,800,4):
            screen.blit(grass,(i,539))
        if cloud_random_number == 0:    
            screen.blit(cloud,(0,-150))
        elif cloud_random_number == 1:    
            screen.blit(cloud,(50,-80))
        elif cloud_random_number == 2:    
            screen.blit(cloud,(-150,-150))
        # Draw grass
        pygame.draw.rect(screen, GREEN, (0, 550, 800, 10))
        
        # Draw ground
        pygame.draw.rect(screen, BROWN, (0, 560, 800, 40))
   
        
        # Draw player
        if player_alive == True:
            pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))
        
        # Draw obstacle
            pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        
        # Update obstacle position and speed based on score
        obstacle_y += obstacle_speed
        if obstacle_y > 505 and player_alive == True:
            obstacle_y = 0
            obstacle_x = random.randint(0, 750)
            score += 1
            obstacle_speed = 10 + score // 2  # Increase speed every 5 points
        
        # Check collision
        if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
            obstacle_y = 0
            obstacle_x = random.randint(0, 750)
            obstacle_speed = 0
            player_alive = False
        if player_alive == False:
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
    game()


