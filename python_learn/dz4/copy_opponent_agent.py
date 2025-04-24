
# Agent that copies the opponent's last move
def copy_opponent_agent(observation, configuration):
    import random
    if observation.step > 0:
        return observation.lastOpponentAction
    else:
        return random.randrange(0, configuration.signs)
