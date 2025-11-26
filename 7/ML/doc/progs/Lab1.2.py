def consistent(hypothesis, instance):
    for h, x in zip(hypothesis, instance):
        if h != "?" and h != x:
            return False
    return True


def candidate_elimination(concepts, target):
    S = concepts[0].copy()
    G = [["?" for _ in range(len(S))]]
    for i, instance in enumerate(concepts):
        if target[i] == "Yes":
            for j in range(len(S)):
                if S[j] != instance[j]:
                    S[j] = "?"
            G = [g for g in G if consistent(g, instance)]
        elif target[i] == "No":
            new_G = []
            for g in G:
                for j in range(len(g)):
                    if g[j] == "?":
                        if S[j] != instance[j]:
                            new_hypothesis = g.copy()
                            new_hypothesis[j] = S[j]
                            new_G.append(new_hypothesis)
    G = [h for h in new_G if any(consistent(h, x) for x in concepts if target[concepts.index(x)] == "Yes")]
    return S, G


concepts = [
    ["Sunny", "Warm", "Normal", "Strong"],
    ["Sunny", "Warm", "High", "Strong"],
    ["Rainy", "Cold", "High", "Strong"],
    ["Sunny", "Warm", "High", "Weak"],
    ["Cloudy", "Warm", "High", "Weak"],
]
target = ["Yes", "Yes", "No", "Yes", "No"]
S_final, G_final = candidate_elimination(concepts, target)

print("\nFinal specific boundary (S) : ", S_final, "\nFinal General boundary (G)  :")
for i in G_final:
    print(i)
