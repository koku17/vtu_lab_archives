import pandas as pd
import numpy as np
from pgmpy.models import BayesianNetwork
from pgmpy.estimators import (
    HillClimbSearch,
    K2Score,
    MaximumLikelihoodEstimator,
)
from pgmpy.inference import VariableElimination

if not hasattr(np, "product"):
    np.product = np.prod

data = pd.DataFrame(
    {
        "Rain": [0, 1, 0, 1, 1, 0, 1, 0],
        "Sprinkler": [1, 0, 1, 0, 1, 0, 0, 1],
        "GrassWet": [1, 1, 0, 1, 1, 0, 1, 0],
    }
)

hc = HillClimbSearch(data)
best_model = hc.estimate(scoring_method=K2Score(data))

model = BayesianNetwork(best_model.edges())
model.fit(data, estimator=MaximumLikelihoodEstimator)
print("Learned structure : ", model.edges())

for cpd in model.get_cpds():
    print(f"\nCPD of {cpd.variable} :", cpd, sep="\n")

infer = VariableElimination(model)
q = infer.query(variables=["Rain"], evidence={"GrassWet": 1})
print("\nP (Rain | GrassWet = 1) :\n", q)

score = K2Score(data)
H_value = score.score(model)

print("\nH value : ", H_value)
