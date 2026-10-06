# Write your solution here
def search(products: list, criterion: callable):
	newlist=[]
	for product in products:
		if criterion(product):
			newlist.append(product)
	return newlist