import itertools
import random
actions = ['Click', 'Scroll', 'Exit']
sample_space = list(itertools.product(actions, repeat=2))
print("Sample Space S:")
print(sample_space)
event_E = [outcome for outcome in sample_space if 'Click' in outcome]
prob_E = len(event_E) / len(sample_space)
print("\nProbability that customer clicks at least once:", prob_E)
rolls = [(random.randint(1,6), random.randint(1,6)) for _ in range(1000)]
sum_7 = [roll for roll in rolls if sum(roll) == 7]
experimental_prob = len(sum_7) / 1000
print("\nExperimental probability of sum = 7 in 1000 dice rolls:", experimental_prob)