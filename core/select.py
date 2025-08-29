from settings import windowSize, math

def flag_space(board, mousePos):
    position = board.mouse_to_space(mousePos)
    if not position in board.flaggedSpaces:
        board.flaggedSpaces.append(position)
    else:
        board.flaggedSpaces.remove(position)

def reveal_neighbors(board, position):
    pass

def reveal_space(board, mousePos):
    position = board.mouse_to_space(mousePos)
    if not position in board.flaggedSpaces:
        if position in board.mineSpaces: board.lost = True
        if position in board.hiddenSpaces:
            board.hiddenSpaces.remove(position)