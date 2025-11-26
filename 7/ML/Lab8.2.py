from itertools import product
import math


def assignments(vars):
    for vals in product([True, False], repeat=len(vars)):
        dict(zip(vars, vals))


def P_B(b):
    return 0.5 if b else 0.5


def P_R_given_B(r, b):
    return (
        0.3 if (r and b) else 0.8 if (r and not b) else (0.7 if (not r and b) else 0.2)
    )


def P_A_given_B(a, b):
    return (
        0.1 if (a and b) else 0.5 if (a and not b) else (0.9 if (not a and b) else 0.5)
    )


def P_S_given_R_A(s, r, a):
    if r and a:
        return 0.0 if s else 1.0
    if r and not a:
        return 0.8 if s else 0.2
    if not r and a:
        return 0.6 if s else 0.4
    if not r and not a:
        return 1.0 if s else 0.0


def joint_prob(b, r, a, s):
    return P_B(b) * P_R_given_B(r, b) * P_A_given_B(a, b) * P_S_given_R_A(s, r, a)


def marginal(var, evidence={}):
    vars = ["B", "R", "A", "S"]
    total_true = 0.0
    total = 0.0
    for assign in assignments(vars):
        ok = True
        for k, v in evidence.items():
            if assign[k] != v:
                ok = False
                break
        if not ok:
            continue
        p = joint_prob(assign["B"], assign["R"], assign["A"], assign["S"])
        total += p

        if assign[var]:
            total_true += p
    if total == 0:
        return None
    return total_true / total


print(
    "P(S) =",
    round(marginal("S"), 4),
    "P(S | B=T) =",
    round(marginal("S", {"B": True}), 4),
    "P(S | A=T) =",
    round(marginal("S", {"A": True}), 4),
    "P(R | S=T) =",
    round(marginal("R", {"S": True}), 4),
    "P(B | S=T) =",
    round(marginal("B", {"S": True}), 4),
)
