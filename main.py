import pygame
import sys
import random
import time

# All code before the 'while loop' creates the pygame window and sets the fps for the game.
pygame.init()
from classes_and_variables import *


WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Time Game")


# Setting up clock for fps control
clock = pygame.time.Clock()
FPS = 60


# This is where all the game code will go
running = True
game_state = "menu"

while running:

    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:  # Enter key
                if game_state == "menu":
                    game_state = "countdown"
                    countdown_number = 3
                    countdown_start_time = time.time()
                elif game_state == "ready":
                    reaction_time = time.time() - green_screen_start_time
                    print(f"Reaction time: {reaction_time:.3f} seconds")
                    game_state = "menu"
        
        # Checks to see if the buttons are clicked
        if event.type == pygame.MOUSEBUTTONDOWN and game_state == "menu":
            if event.button == 1:  # Left click
                if rules_button.collidepoint(event.pos):
                    print("Rules button clicked!")
                    # Add rules logic here
                    
                if leaderboard_button.collidepoint(event.pos):
                    print("Leaderboard button clicked!")
                    # Add leaderboard logic here

    # Update countdown
    if game_state == "countdown":
        elapsed_time = time.time() - countdown_start_time
        if elapsed_time >= 1:
            countdown_number -= 1
            countdown_start_time = time.time()
            if countdown_number < 0:
                game_state = "game"
                red_screen_start_time = time.time()
                random_delay = random.uniform(1.5, 4.0)
    
    # Check if random delay is over and turn screen green
    if game_state == "game":
        elapsed_red_time = time.time() - red_screen_start_time
        if elapsed_red_time >= random_delay:
            game_state = "ready"
            green_screen_start_time = time.time()
    
    # Render based on game state
    if game_state == "menu":
        screen.fill(LIGHT_GREEN)
        screen.blit(title_font.render("Reaction Time Game", True, BLACK), (WIDTH//2 - 300, 50))
        
        # Drawing instruction to press Enter
        instruction_text = instruction_font.render("Press ENTER to start", True, BLACK)
        instruction_rect = instruction_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 150))
        screen.blit(instruction_text, instruction_rect)
        
        # Drawing Start button
        pygame.draw.rect(screen, WHITE, rules_button)
        pygame.draw.rect(screen, BLACK, rules_button, 3)
        text_rect = rules_button_text.get_rect(center=rules_button.center)
        screen.blit(rules_button_text, text_rect)
        
        # Drawing Leaderboard button
        pygame.draw.rect(screen, WHITE, leaderboard_button)
        pygame.draw.rect(screen, BLACK, leaderboard_button, 3)
        text_rect = leaderboard_button_text.get_rect(center=leaderboard_button.center)
        screen.blit(leaderboard_button_text, text_rect)
    
    elif game_state == "countdown":
        screen.fill(LIGHT_GREEN)
        if countdown_number > 0:
            countdown_text = title_font.render(str(countdown_number), True, BLACK)
            countdown_rect = countdown_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(countdown_text, countdown_rect)
    
    elif game_state == "game":
        screen.fill(RED)
        red_screen_text = title_font.render("Wait...", True, WHITE)
        red_screen_rect = red_screen_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(red_screen_text, red_screen_rect)
    
    elif game_state == "ready":
        screen.fill(LIGHT_GREEN)
        ready_text = title_font.render("GO!", True, BLACK)
        ready_rect = ready_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(ready_text, ready_rect)



    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()
