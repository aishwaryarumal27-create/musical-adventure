prob_heads = 0.5
prob_six = 1/6
prob_heads_and_six = prob_heads * prob_six
print("Probability of Heads AND rolling a 6:", prob_heads_and_six)
total_marbles = 10
red_marbles = 5
prob_first_red = red_marbles / total_marbles
prob_second_red = (red_marbles - 1) / (total_marbles - 1)
prob_two_red = prob_first_red * prob_second_red
print("Probability of drawing 2 Red marbles without replacement:", prob_two_red)
print("\nReflection: The denominator changed for the second draw because one marble was already removed, reducing the total numbr of marbles in the bag.")