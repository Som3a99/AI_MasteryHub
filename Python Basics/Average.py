# Average function
def avg(*args):
	"""Calculate the average of a sequence of numbers."""
	return sum(args) / len(args)

avg(2, 3, 4, 5)