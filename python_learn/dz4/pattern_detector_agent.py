
# Agent that tries to detect patterns in the opponent's moves
def pattern_detector_agent(observation, configuration):
    import random
    if observation.step < 2:
        pattern_detector_agent.last_moves = []
        return random.randrange(0, configuration.signs)
    else:
        opponent_action = observation.lastOpponentAction
        pattern_detector_agent.last_moves.append(opponent_action)
        # Simple pattern detection: if the opponent repeats the same move
        if pattern_detector_agent.last_moves[-1] == pattern_detector_agent.last_moves[-2]:
            # Assume the opponent will repeat again
            predicted_move = opponent_action
        else:
            predicted_move = random.randrange(0, configuration.signs)
        # Play the move that beats the predicted move
        return (predicted_move + 1) % configuration.signs
