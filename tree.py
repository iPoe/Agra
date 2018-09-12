def print_tree(x,r):
	if 2*r<len(x):
		print('(',end='')
		print_tree(x,2*r)
		print(')',end='')

	print(x[r],end='')

	if 2*r+1 < len(x):
		print('(',end='')
		print_tree(x,2*r+1)
		print(')',end='')
	return

x = [3,[2,10,]]