
# Agent that repeats its own last move
def mirror_self_agent(observation, configuration):
    import random
    if observation.step > 0:
        return observation.agentAction
    else:
        return random.randrange(0, configuration.signs)
