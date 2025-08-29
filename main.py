from settings import pygame, windowSize
from core.select import *
from core.board import Board

display = pygame.display
window = display.set_mode((windowSize[0], windowSize[1]))

display.set_caption("game")

board = Board(
    (16, 16),
    None,
    40
)

running = True

while running:
    window.fill('white')

    mousePos = pygame.mouse.get_pos()

    board.draw_grid(window)
    board.draw_mines(window)
    board.draw_numbers(window)
    board.hide_hidden_spaces(window)
    board.draw_flagged_spaces(window)

    if board.lost: running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                reveal(board, mousePos)

            elif event.button == pygame.BUTTON_RIGHT:
                flag_space(board, mousePos)

    display.update()

pygame.quit()