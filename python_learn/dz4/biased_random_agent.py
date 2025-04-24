
# Agent that plays Rock more frequently
def biased_random_agent(observation, configuration):
    import random
    choice = random.random()
    if choice < 0.6:
        return 0  # Rock
    elif choice < 0.8:
        return 1  # Paper
    else:
        return 2  # Scissors
