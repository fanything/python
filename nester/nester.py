'''
这是一个递归
'''
def print_lol(the_list,indent=False,level=0,):
	'''
	这是一个循环
	'''
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item,indent,level+1)
		else:
			if indent:
				for num in range(level):
					print('\t',end='')
			print(each_item)