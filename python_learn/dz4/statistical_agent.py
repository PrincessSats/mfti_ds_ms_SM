
# Agent that tracks opponent's moves and beats the most frequent one
def statistical_agent(observation, configuration):
    import random
    if observation.step == 0:
        statistical_agent.action_histogram = {}
        return random.randrange(0, configuration.signs)
    else:
        opponent_action = observation.lastOpponentAction
        histogram = statistical_agent.action_histogram
        histogram[opponent_action] = histogram.get(opponent_action, 0) + 1
        most_common = max(histogram, key=histogram.get)
        # Play the move that beats the opponent's most frequent move
        return (most_common + 1) % configuration.signs
