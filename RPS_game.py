from RPS import player



#we define a bot that always play rock
def simple_bot(prev_player, opponent_history=[]):
    return 'R'

#we define a bot that always play paper
def paper_bot(prev_play, opponent_history=[]):
    return 'P'

#we define a pattern robot that plays R, P, S in order
def pattern_bot(prev_play, opponent_history=[]):
    pattern = ['R', 'P', 'S']

    if prev_play:
        opponent_history.append(prev_play)

    index = len(opponent_history) % 3
    return pattern[index]



#function to play a match
def play(player1, player2, rounds=5, verbose=True):
    p1_score = 0
    p2_score = 0
    moves = ['R', 'P', 'S']

    for i in range(rounds):
        move1 = player1('' if i==0 else move2)
        move2 = player2('' if i==0 else move1)

        if move1 == move2:
            result = 'Tie'
        elif (move1 == 'R' and move2 == 'S') or (move1 == 'P' and move2 == 'R') or (move1 == 'S' and move2 == 'P'):
            result = 'Player 1 wins'
            p1_score += 1   
        else:
            result = 'Player 2 wins'
            p2_score += 1   
        if verbose:
            print(f"Round {i+1}: Player1 plays {move1}, Player2 plays {move2}. Result: {result}")
    print(f"Final Score: Player1: {p1_score}, Player2: {p2_score}")

