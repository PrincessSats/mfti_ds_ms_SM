
# Agent that plays the move that beats the opponent's last move
def beat_last_move_agent(observation, configuration):
    import random
    if observation.step > 0:
        return (observation.lastOpponentAction + 1) % configuration.signs
    else:
        return random.randrange(0, configuration.signs)
