#!/bin/python

facts=[
	['croaks','frog'],
	['eatsflies','frog'],
	['frog','green'],
	['chirps','canary'],
	['sing','canary'],
	['canary','yellow']
]

def find_related_facts(starting_facts,all_facts):
	related_facts=[]
	keep_finding=True
	while keep_finding==True:
		keep_finding=False
		for fact in starting_facts:
			for f in all_facts:
				if f[0]==fact:
					new_related_fact=[fact,f[1]]
					if new_related_fact not in related_facts:
						related_facts+=[new_related_fact]
						starting_facts+=[f[1]]
						keep_finding=True
	return related_facts

print(find_related_facts(['croaks','frogs'],facts))
