'''
这是一个递归
'''
def print_lol(the_list):
	'''
	这是一个循环
	'''
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print(each_item)
