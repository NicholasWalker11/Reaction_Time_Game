import pygame
import sys
import random
import time

# All code before the 'while loop' sets up the game window, imports variables, initializes pygame, and sets fps cap to limit advanced systems from breaking the game.
pygame.init()
from classes_and_variables import *
from leaderboard_storage import *

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Time Game")


# Setting up clock for fps control
clock = pygame.time.Clock()
FPS = 60

# Load saved leaderboard scores
reaction_times_list = load_leaderboard()

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
            if event.key == pygame.K_RETURN: # Enter key
                if game_state == "menu":
                    game_state = "countdown"
                    countdown_number = 3
                    countdown_start_time = time.time()
                elif game_state == "ready":
                    reaction_time = time.time() - green_screen_start_time
                    # Recording reaction time to leaderboard
                    reaction_times_list.append(reaction_time)
                    reaction_times_list.sort()
                    if len(reaction_times_list) > MAX_LEADERBOARD_ENTRIES:
                        reaction_times_list = reaction_times_list[:MAX_LEADERBOARD_ENTRIES]
                    save_leaderboard()  # Save after adding new score
                    game_state = "result"

                elif game_state == "result":
                    game_state = "menu"
                    reaction_time = None

                elif game_state == "rules":
                    game_state = "menu"
                    
                elif game_state == "leaderboard":
                    game_state = "menu"

        # Checks to see if the buttons are clicked
        if event.type == pygame.MOUSEBUTTONDOWN and game_state == "menu":
            if event.button == 1:
                if rules_button.collidepoint(event.pos):
                    game_state = "rules"

                if leaderboard_button.collidepoint(event.pos):
                    game_state = "leaderboard"

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

    elif game_state == "result":
        screen.fill(LIGHT_GREEN)
        #convert reaction time to ms
        ms = int(reaction_time * 1000) if reaction_time is not None else 0
        #reaction_time display
        result_text = title_font.render("RESULT", True, BLACK)
        result_text_rect = result_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 180))
        screen.blit(result_text, result_text_rect)
        #reaction time result in seconds
        result_display = title_font.render(f"{reaction_time:.3f}s", True, BLACK)
        result_rect = result_display.get_rect(center=(WIDTH//2, HEIGHT//2-40))
        screen.blit(result_display, result_rect)
        #instruction to return to menu
        return_text = instruction_font.render("Press Enter to return to menu", True, BLACK )
        return_rect = return_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 140))
        screen.blit(return_text, return_rect)

    elif game_state == "rules":
        screen.fill(LIGHT_GREEN)
        # Display rules title
        rules_title = title_font.render("Rules", True, BLACK)
        rules_title_rect = rules_title.get_rect(center=(WIDTH//2, rules_title_y))
        screen.blit(rules_title, rules_title_rect)
        
        # Display rules text
        y_offset = rules_text_start_y
        for rule in rules_text:
            rule_surface = instruction_font.render(rule, True, BLACK)
            rule_rect = rule_surface.get_rect(center=(WIDTH//2, y_offset))
            screen.blit(rule_surface, rule_rect)
            y_offset += rules_text_spacing
        
        # Display instruction to return to menu
        return_text = instruction_font.render("Press Enter to return to menu", True, BLACK)
        return_rect = return_text.get_rect(center=(WIDTH//2, HEIGHT - rules_return_y_offset))
        screen.blit(return_text, return_rect)

    elif game_state == "leaderboard":
        screen.fill(LIGHT_GREEN)
        # Display leaderboard title
        leaderboard_title = title_font.render("Top 10 Fastest Times", True, BLACK)
        leaderboard_title_rect = leaderboard_title.get_rect(center=(WIDTH//2, leaderboard_title_y))
        screen.blit(leaderboard_title, leaderboard_title_rect)
        
        # Display leaderboard entries
        if len(reaction_times_list) == 0:
            no_scores_text = instruction_font.render("No scores yet! Play to set a record.", True, BLACK)
            no_scores_rect = no_scores_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(no_scores_text, no_scores_rect)
        else:
            y_offset = leaderboard_start_y
            for i, time_val in enumerate(reaction_times_list, 1):
                entry_text = instruction_font.render(f"{i}. {time_val:.3f}s", True, BLACK)
                entry_rect = entry_text.get_rect(center=(WIDTH//2, y_offset))
                screen.blit(entry_text, entry_rect)
                y_offset += leaderboard_entry_spacing
        
        # Display instruction to return to menu
        return_text = instruction_font.render("Press Enter to return to menu", True, BLACK)
        return_rect = return_text.get_rect(center=(WIDTH//2, HEIGHT - leaderboard_return_y_offset))
        screen.blit(return_text, return_rect)


    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()
sys.exit()
