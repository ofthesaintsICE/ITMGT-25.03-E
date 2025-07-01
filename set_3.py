'''Programming Set 3

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    if (from_member in social_graph[to_member]['following']) and (to_member in social_graph[from_member]['following']):
        return 'friends'
    elif from_member in social_graph[to_member]['following']:
        return 'followed by'
    elif to_member in social_graph[from_member]['following']:
        return 'follower'
    else:
        return 'no relationship'

def tic_tac_toe(board):
    board_size = len(board)

    for row in board:
        if row[0] != '' and all(cell == row[0] for cell in row):
            return row[0]

    for column in range(board_size):
        if board[0][column] != '' and all(board[row][column] == board[0][column] for row in range(board_size)):
            return board[0][column]

    if board[0][0] != '' and all(board[i][i] == board[0][0] for i in range(board_size)):
        return board[0][0]

    if board[0][board_size - 1] != '' and all(board[i][board_size - 1 - i] == board[0][board_size - 1] for i in range(board_size)):
        return board [0][board_size - 1]

    return 'NO WINNER'


def eta(first_stop, second_stop, route_map):
    time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), data in route_map.items():
            if start == current_stop:
                time += data['travel_time_mins']
                current_stop = end
                break

    return time