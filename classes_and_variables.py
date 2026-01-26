import pygame
import sys
import random
import time


WIDTH, HEIGHT = 1920, 1080


# Game Variables
countdown_number = 3
countdown_start_time = 0
red_screen_start_time = 0
random_delay = 0
green_screen_start_time = 0


# Set all colors here
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_GREEN = (50, 205, 50)


# Setting fonts
title_font = pygame.font.SysFont('Arial', 80)
instruction_font = pygame.font.SysFont('Arial', 40)
rules_button_font = pygame.font.SysFont('Arial', 50)
leaderboard_button_font = pygame.font.SysFont('Arial', 30)


# Setting up all buttons
rules_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 60)
rules_button_text = rules_button_font.render("Rules", True, BLACK)

leaderboard_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 + 50, 200, 60)
leaderboard_button_text = leaderboard_button_font.render("Leaderboard", True, BLACK)