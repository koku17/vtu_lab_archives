#!/bin/python
def negate_literal(literal):
	if literal.startswith('~'):
		return literal[1:]
	else:
		return '~'+literal

def resolve(clause1,clause2):
	new_clause=[]
	resolved=False
	for literal in clause1:
		if negate_literal(literal) in clause2:
			resolved=True
		else:
			new_clause.append(literal)
	for literal in clause2:
		if negate_literal(literal) not in clause1:
			new_clause.append(literal)
	if resolved:
		return new_clause
	else:
		return None

def resolution(propositional_kb,query):
	kb=propositional_kb[:]
	kb.append([negate_literal(query)])
	while True:
		new_clauses=[]
		n=len(kb)
		resolved_pairs=set()
		for i in range(n):
			for j in range(i+1,n):
				clause1=kb[i]
				clause2=kb[j]
				if(i,j) not in resolved_pairs:
					resolved_pairs.add((i,j))
					resolvent=resolve(clause1,clause2)
					if resolvent is None:
						continue
					if len(resolvent)==0:
						return True
					if resolvent not in new_clauses:
						new_clauses.append(resolvent)
		if all(clause in kb for clause in new_clauses):
			return False
		kb.extend(new_clauses)

if __name__=="__main__":
	propositional_kb=[
		['~P','Q'],
		['P','~Q','R'],
		['~R','S']
	]
	query='S'
	result=resolution(propositional_kb,query)
	if result:
		print(f"The query '{query}' is PROVED")
	else:
		print(f"The query '{query}' is DISPROVED")
