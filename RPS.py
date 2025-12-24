import random

def player(prev_play, opponent_history=[]):
    # Save opponent move
    if prev_play:
        opponent_history.append(prev_play)

    # First move
    if not opponent_history:
        return "R"

    predicted_move = None

    # ---- PATTERN DETECTION (last 3 moves) ----
    if len(opponent_history) >= 3:
        last_three = opponent_history[-3:]

        if last_three == ['R', 'P', 'S']:
            predicted_move = 'R'
        elif last_three == ['P', 'S', 'R']:
            predicted_move = 'P'
        elif last_three == ['S', 'R', 'P']:
            predicted_move = 'S'

    # ---- COUNTER PATTERN IF FOUND ----
    if predicted_move == 'R':
        my_move = 'P'
    elif predicted_move == 'P':
        my_move = 'S'
    elif predicted_move == 'S':
        my_move = 'R'
    else:
        # ---- FREQUENCY STRATEGY ----
        rock = opponent_history.count('R')
        paper = opponent_history.count('P')
        scissors = opponent_history.count('S')

        if rock >= paper and rock >= scissors:
            my_move = 'P'
        elif paper >= rock and paper >= scissors:
            my_move = 'S'
        else:
            my_move = 'R'

    # ---- RANDOMNESS (anti-exploit) ----
    if random.random() < 0.2:
        my_move = random.choice(['R', 'P', 'S'])

    return my_move


    
