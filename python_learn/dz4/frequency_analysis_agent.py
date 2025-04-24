
# Agent that predicts the opponent's next move based on frequency analysis
def frequency_analysis_agent(observation, configuration):
    import random
    if observation.step == 0:
        frequency_analysis_agent.action_histogram = {}
        return random.randrange(0, configuration.signs)
    else:
        opponent_action = observation.lastOpponentAction
        histogram = frequency_analysis_agent.action_histogram
        histogram[opponent_action] = histogram.get(opponent_action, 0) + 1
        # Predict opponent's next move
        predicted_move = max(histogram, key=histogram.get)
        # Play the move that beats the predicted move
        return (predicted_move + 1) % configuration.signs
