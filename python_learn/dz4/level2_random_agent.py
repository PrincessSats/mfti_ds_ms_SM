
# Agent that uses a predefined sequence
def level2_random_agent(observation, configuration):
    sequence = [0, 1, 2, 0, 1, 2]
    return sequence[observation.step % len(sequence)]
