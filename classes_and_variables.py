import pygame


# Game Variables
WIDTH, HEIGHT = 1600, 800
countdown_number = 3
countdown_start_time = 0
red_screen_start_time = 0
random_delay = 0
green_screen_start_time = 0
reaction_time = None


# Set all colors here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_GREEN = (50, 205, 50)


# Setting fonts for texts
title_font = pygame.font.SysFont('Arial', 80)
instruction_font = pygame.font.SysFont('Arial', 40)
rules_button_font = pygame.font.SysFont('Arial', 50)
leaderboard_button_font = pygame.font.SysFont('Arial', 30)


# Setting up all buttons
rules_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 60)
rules_button_text = rules_button_font.render("Rules", True, BLACK)

leaderboard_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 60)
leaderboard_button_text = leaderboard_button_font.render("Leaderboard", True, BLACK)


# Rules Text
rules_text = [
    "1. When you click 'Start', the screen will turn red after a short delay.",
    "2. Wait for the screen to turn green.",
    "3. As soon as the screen turns green, click ENTER as fast as you can!",
    "4. Your reaction time will be recorded and displayed.",
    "5. Try to beat your best time and climb the leaderboard!"
]


# Rules screen positioning
rules_title_y = 100
rules_text_start_y = 250
rules_text_spacing = 80
rules_return_y_offset = 100


# Leaderboard screen positioning
leaderboard_title_y = 100
leaderboard_start_y = 200
leaderboard_entry_spacing = 60
leaderboard_return_y_offset = 100
