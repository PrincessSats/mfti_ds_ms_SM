
# Agent that cycles through the moves in order
def rotate_moves_agent(observation, configuration):
    return observation.step % configuration.signs
