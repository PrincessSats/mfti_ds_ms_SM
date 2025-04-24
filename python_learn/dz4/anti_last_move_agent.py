
# Agent that plays the move that loses to the opponent's last move
def anti_last_move_agent(observation, configuration):
    import random
    if observation.step > 0:
        return (observation.lastOpponentAction + 2) % configuration.signs
    else:
        return random.randrange(0, configuration.signs)
