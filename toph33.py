brackets = input()
stack = []
for b in brackets:
	if b == '(' or b=="{" or b=="[":
		stack.append(b)
	else:
		if len(stack) > 0:
			stack.pop()
		else:
			stack.append(b)
			break

if len(stack) == 0:
	print('Yes')
else:
	print('No')