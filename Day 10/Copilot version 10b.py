import re
from itertools import product

def generate_with_sum(n, depth, limits):
    """
    Yield all n-tuples (c1, c2, ..., cn) such that:
        0 <= ci <= limits[i]
        sum(ci) = depth
    """
    if n == 1:
        if depth <= limits[0]:
            yield (depth,)
        return

    for x in range(min(depth, limits[0]) + 1):
        for rest in generate_with_sum(n - 1, depth - x, limits[1:]):
            yield (x,) + rest

def prune_dominated(button_dictionary, joltage_dictionary):
    """
    Remove button_dictionary entries that are strictly dominated by others.
    A button A dominates B if A covers >= B in all labels and > in at least one.
    """
    labels = sorted(joltage_dictionary.keys())
    names = list(button_dictionary.keys())
    keep = set(names)

    for i in range(len(names)):
        for j in range(len(names)):
            if i == j:
                continue
            A, B = names[i], names[j]
            a = button_dictionary[A]
            b = button_dictionary[B]

            # Count contributions
            vecA = {x: a.count(x) for x in labels}
            vecB = {x: b.count(x) for x in labels}

            # Check dominance
            if all(vecA[x] >= vecB[x] for x in labels) and any(vecA[x] > vecB[x] for x in labels):
                if B in keep:
                    keep.remove(B)
    return {k: button_dictionary[k] for k in keep}

def min_buttons(button_dictionary, joltage_dictionary, max_limit=200):
    """
    Optimized brute-force solver with:
    - dominance pruning
    - feasibility pruning
    - depth-by-depth search
    """
    button_dictionary = prune_dominated(button_dictionary, joltage_dictionary)

    labels = sorted(joltage_dictionary.keys())

    # Precompute contribution vectors
    contrib = {}
    for name, button in button_dictionary.items():
        vec = {label: 0 for label in labels}
        for x in button:
            if x in vec:
                vec[x] += 1
        contrib[name] = vec

    button_names = list(button_dictionary.keys())
    n = len(button_names)

    # Compute a lower bound on depth:
    # For each label, compute min blocks needed if using the best button for that label.
    lower_bound = 0
    for label in labels:
        best = max(contrib[name][label] for name in button_names)
        if best == 0:
            raise ValueError(f"No button can produce label {label}")
        lower_bound = max(lower_bound, (joltage_dictionary[label] + best - 1) // best)

    # Depth-by-depth search
    for depth in range(lower_bound, max_limit + 1):

        # Generate all combinations of button counts summing to depth
        # Use a restricted search: only allow counts up to joltage_dictionary[label] for relevant labels
        ranges = []
        for name in button_names:
            # Upper bound for each button type:
            # You never need more of a button than the max requirement of any label it contributes to.
            max_use = max((joltage_dictionary[l] for l in labels if contrib[name][l] > 0), default=0)
            ranges.append(range(min(depth, max_use) + 1))

        limits = [r.stop - 1 for r in ranges]  # max allowed per block
        for counts in generate_with_sum(len(button_names), depth, limits):
            # Feasibility pruning: check if even max possible coverage meets joltage_dictionary
            cover = {label: 0 for label in labels}
            for name, cnt in zip(button_names, counts):
                for label in labels:
                    cover[label] += contrib[name][label] * cnt

            if all(cover[label] >= joltage_dictionary[label] for label in labels):
                return depth

    raise RuntimeError("No solution found within max_limit")

# -------------------------
# Example usage
# -------------------------

button_dictionary = {
    "A": [3],
    "B": [1, 3],
    "C": [2],
    "D": [2, 3],
    "E": [0, 2],
    "F": [0, 1],
}

joltage_dictionary = {0: 3, 1: 5, 2: 4, 3: 7}

best_total = min_buttons(button_dictionary, joltage_dictionary)

print(best_total)

# -------------------------
# My own code
# -------------------------

with open('Anna\'s solutions//Day 10//Day 10 input.txt') as raw:
    raw_input = raw.read().splitlines()

buttons = [[[int(x) for x in re.findall(r'\d+', button)] for button in line] for line in [re.findall(r'\(\S+\)', line) for line in raw_input]]
joltage_levels = [[int(x) for x in re.findall(r'\d+', str(re.findall(r'{\S+}', line)))] for line in raw_input]

how_many_blocks = []

for i in range(len(buttons)):
    button_dictionary = {chr(ord('A')+j): buttons[i][j] for j in range(len(buttons[i]))}
    joltage_dictionary = {k: joltage_levels[i][k] for k in range(len(joltage_levels[i]))}
    how_many_blocks.append(min_buttons(button_dictionary, joltage_dictionary))

print(sum(how_many_blocks))
