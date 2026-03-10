import numpy as np
scores = np.random.randint(50, 101, size=(5, 3))
mean_scores = np.mean(scores, axis=0)
centered_scores = scores - mean_scores
print("Original Scores:\n", scores)
print("\nMean Scores (per subject):\n", mean_scores)
print("\nCentered Scores:\n", centered_scores)