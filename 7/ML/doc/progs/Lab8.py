from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([("B", "R"), ("B", "A"), ("R", "S"), ("A", "S")])
cpd_B = TabularCPD(
    variable="B", variable_card=2, values=[[0.5], [0.5]], state_names={"B": ["T", "F"]}
)
cpd_R = TabularCPD(
    variable="R",
    variable_card=2,
    values=[[0.3, 0.8], [0.7, 0.2]],
    evidence=["B"],
    evidence_card=[2],
    state_names={"R": ["T", "F"], "B": ["T", "F"]},
)
cpd_A = TabularCPD(
    variable="A",
    variable_card=2,
    values=[[0.1, 0.5], [0.9, 0.5]],
    evidence=["B"],
    evidence_card=[2],
    state_names={"A": ["T", "F"], "B": ["T", "F"]},
)
cpd_S = TabularCPD(
    variable="S",
    variable_card=2,
    values=[[0.0, 0.8, 0.6, 1.0], [1.0, 0.2, 0.4, 0.0]],
    evidence=["R", "A"],
    evidence_card=[2, 2],
    state_names={"S": ["T", "F"], "R": ["T", "F"], "A": ["T", "F"]},
)
model.add_cpds(cpd_B, cpd_R, cpd_A, cpd_S)
model.check_model()
infer = VariableElimination(model)
print(
    "P(S):",
    infer.query(variables=["S"]),
    "\nP(S | B = T):",
    infer.query(variables=["S"], evidence={"B": "T"}),
    "\nP(S | A = T):",
    infer.query(variables=["S"], evidence={"A": "T"}),
    "\nP(R | S = T):",
    infer.query(variables=["R"], evidence={"S": "T"}),
    "\nP(B | S = T):",
    infer.query(variables=["B"], evidence={"S": "T"}),
    sep="\n",
)
