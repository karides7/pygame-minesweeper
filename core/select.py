from settings import windowSize, math

def flag_space(board, mousePos):
    position = board.mouse_to_space(mousePos)
    if not position in board.flaggedSpaces:
        board.flaggedSpaces.append(position)
    else:
        board.flaggedSpaces.remove(position)

def __reveal_neighbors(board, position):
    for i in range(1, board.size[0] + 1):
        for j in range(1, board.size[1] + 1):
            space = (i, j)
            if not space in board.hiddenSpaces: continue
            if math.dist(position, space) < math.sqrt(2.5):
                relativeMineAmount = board.get_mine_relative_amount(space)
                board.hiddenSpaces.remove(space)
                if relativeMineAmount == 0:
                    __reveal_neighbors(board, space)

def reveal(board, mousePos):
    position = board.mouse_to_space(mousePos)
    if not position in board.flaggedSpaces:
        if position in board.mineSpaces: board.lost = True
        if position in board.hiddenSpaces:
            board.hiddenSpaces.remove(position)
            if board.get_mine_relative_amount(position) == 0:
                __reveal_neighbors(board, position)