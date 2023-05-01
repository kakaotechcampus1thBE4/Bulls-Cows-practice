def answer(list, solution):
    bulls = 0
    cows = 0
    for i, k in enumerate(solution):
        if list[i] in solution:
            if list[i] == k:
                bulls += 1
            else:
                cows += 1
    return [bulls, cows]
