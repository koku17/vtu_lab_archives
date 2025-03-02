import re

class CFGParser:
	def __init__ (self):
		self.grammar = {
			'E': [['E', '+', 'T'], ['T']],
			'T': [['T', '*', 'F'], ['F']],
			'F': [['(', 'E', ')'], ['id']]
		}

	def tokenize (self, expression):
		return re.findall(r'\b\w+\b|[()+*]', expression)

	def parse_E (self):
		if not self.parse_T ():
			return False
		while self.index < len (self.tokens) and self.tokens[self.index] == '+':
			self.index += 1
			if not self.parse_T ():
				return False
		return True

	def parse_T (self):
		if not self.parse_F ():
			return False
		while self.index < len (self.tokens) and self.tokens[self.index] == '*':
			self.index += 1
			if not self.parse_F ():
				return False
		return True

	def parse_F (self):
		if self.match ('('):
			if self.parse_E () and self.match (')'):
				return True
			return False
		elif self.match ('id'):
			return True
		return False

	def match (self, expected):
		if self.index < len (self.tokens) and self.tokens[self.index] == expected:
			self.index += 1
			return True
		return False

	def top_down_parse (self, expression):
		self.tokens = self.tokenize (expression)
		self.index = 0
		return 'Accepted (Top-Down)' if self.parse_E () and self.index == len (self.tokens) else 'Rejected (Top-Down)'

	def bottom_up_parse (self, expression):
		stack, tokens, i = [], self.tokenize (expression), 0
		print ('\nBottom-Up Parsing Steps : ')
		while i < len (tokens) or stack:
			reduced = False

			if len (stack) >= 3 and stack[-3] == '(' and stack[-1] == ')':
				print (f'Reduce : {stack[-3:]} -> F')
				stack[-3:] = ['F']
				reduced = True
			elif stack[-1:] == ['id']:
				print (f'Reduce : {stack[-1]} -> F')
				stack[-1] = 'F'
				reduced = True
			elif stack[-1:] == ['F']:
				print (f'Reduce : {stack[-1]} -> T')
				stack[-1] = 'T'
				reduced = True
			elif len (stack) >= 3 and stack[-2] == '*' and stack[-1] == 'T':
				print (f'Reduce : {stack[-3:]} -> T')
				stack[-3:] = ['T']
				reduced = True
			elif len (stack) >= 3 and stack[-2] == '+' and stack[-1] == 'T':
				print (f'Reduce : {stack[-3:]} -> E')
				stack[-3:] = ['E']
				reduced = True
			elif stack[-1:] == ['T']:
				print (f'Reduce : {stack[-1]} -> E')
				stack[-1] = 'E'
				reduced = True

			if reduced:
				continue
	
			if i < len (tokens):
				print (f'Shift  : {tokens[i]}')
				stack.append (tokens[i])
				i += 1
			else:
				break
		return 'Accepted (Bottom-Up)' if stack == ['E'] else 'Rejected (Bottom-Up)'

parser = CFGParser ()
expression = input ('Enter an arithmetic expression using \'id\', \'+\', \'*\', and parentheses : ').strip ()
print ('', parser.top_down_parse (expression), parser.bottom_up_parse (expression), sep = '\n')

#expressions = [
#	'id', 'id + id', 'id * id', 'id + id * id', 'id * ( id + id )', '( id + id ) * id', '+ id', 'id *', 'id +',
#	'( id +', 'id + id )'
#]
#for i in expressions:
#	print ('\nEnter an arithmetic expression using \'id\', \'+\', \'*\', and parentheses :', i)
#	expression = i.strip ()
#	print ('', parser.top_down_parse (expression), parser.bottom_up_parse (expression), sep = '\n')
