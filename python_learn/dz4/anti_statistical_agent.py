
# Agent that tracks opponent's moves and beats the least frequent one
def anti_statistical_agent(observation, configuration):
    import random
    if observation.step == 0:
        anti_statistical_agent.action_histogram = {}
        return random.randrange(0, configuration.signs)
    else:
        opponent_action = observation.lastOpponentAction
        histogram = anti_statistical_agent.action_histogram
        histogram[opponent_action] = histogram.get(opponent_action, 0) + 1
        least_common = min(histogram, key=histogram.get)
        # Play the move that beats the opponent's least frequent move
        return (least_common + 1) % configuration.signs
