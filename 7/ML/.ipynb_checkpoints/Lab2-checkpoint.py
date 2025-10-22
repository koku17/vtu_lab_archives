import pandas as pd
import math

def foil_gain (P, N, p, n):
	if p == 0 or P == 0:
		return -1e9
	return p * (math.log2 (p / (p + n)) - math.log2 (P / (P + N)))

def foil_algorithm (df, target_attr):
	rules = []
	pos_examples = df[df[target_attr] == 'Yes']
	neg_examples = df[df[target_attr] == 'No']
	attributes = [col for col in df.columns if col != target_attr]
	while len (pos_examples) > 0:
		rule = []
		covered_pos = pos_examples.copy ()
		covered_neg = neg_examples.copy ()
		while len (covered_neg) > 0:
			best_gain = -1e9
			best_literal = None
			best_pos, best_neg = None, None
			for attr in attributes:
				for value in df[attr].unique ():
					literal = (attr, value)
					pos_subset = covered_pos [covered_pos[attr] == value]
					neg_subset = covered_neg[covered_neg[attr] == value]
					gain = foil_gain (len (covered_pos), len (covered_neg), len (pos_subset), len (neg_subset))
					if gain  >  best_gain:
						best_gain = gain
						best_literal = literal
						best_pos, best_neg = pos_subset, neg_subset
			if best_literal is None:
				break
			rule.append (best_literal)
			covered_pos = best_pos
			covered_neg = best_neg
		rules.append (rule)
		pos_examples = pos_examples.drop (covered_pos.index)
	return rules
data = {
		'Outlook':['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain'], 
		'Temperature':['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild'], 
		'Humidity':['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal'], 
		'Wind':['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Weak', 'Weak'], 
		'Play':['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes']
}
df = pd.DataFrame (data)
rules = foil_algorithm (df, 'Play')
print ('Learned rules :')
for i, rule in enumerate (rules, 1):
	conds = ' AND ' .join ([f'{attr} = {val}' for attr, val in rule])
	print (f'Rule{i} :\nIF {conds} THEN Play = Yes')
