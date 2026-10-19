import random
moves = ["r", "p", "s"]
names = {"r": "Rock", "p": "Paper", "s": "Scissors"}
def reward(ai, human):
    if ai == human:
        return 0
    if (ai, human) in [("r", "s"), ("p", "r"), ("s", "p")]:
        return 1
    return -1
def counter(move):
    return {"r": "p", "p": "s", "s": "r"}[move]
counts = {m: {n: 1 for n in moves} for m in moves}
def probabilities(prev):
    total = sum(counts[prev].values())
    return {m: counts[prev][m] / total for m in moves}
def mdp():
    gamma = 0.9
    V = {m: 0 for m in moves}
    policy = {m: "r" for m in moves}
    for _ in range(100):
        newV = {}
        for state in moves:
            probs = probabilities(state)
            values = {}
            for action in moves:
                immediate = sum(
                    probs[h] * reward(action, h) for h in moves
                )
                future = sum(
                    probs[h] * V[h] for h in moves
                )
                values[action] = immediate + gamma * future
            policy[state] = max(values, key=values.get)
            newV[state] = values[policy[state]]
        V = newV
    return policy
mode = input("Choose mode (BAYES/MDP): ").upper()
rounds = int(input("Enter number of rounds: "))
prev = "r"
ai_wins = human_wins = ties = 0
for i in range(rounds):
    print("\nRound", i + 1)
    if mode == "BAYES":
        probs = probabilities(prev)
        prediction = max(probs, key=probs.get)
        ai = counter(prediction)
        print("Predicted human move:", names[prediction])
    elif mode == "MDP":
        policy = mdp()
        ai = policy[prev]
    else:
        print("Invalid mode!")
        break
    human = input("Enter move (r/p/s): ").lower()
    if human not in moves:
        print("Invalid move! Try again.")
        continue
    print("AI move:", names[ai])
    print("Human move:", names[human])
    result = reward(ai, human)
    if result == 1:
        print("AI wins!")
        ai_wins += 1
    elif result == -1:
        print("Human wins!")
        human_wins += 1
    else:
        print("Tie!")
        ties += 1
    counts[prev][human] += 1
    prev = human
print("\nFinal Score")
print("AI wins:", ai_wins)
print("Human wins:", human_wins)
print("Ties:", ties)
print("\nLearned CPT:")
for state in moves:
    print(names[state], probabilities(state))