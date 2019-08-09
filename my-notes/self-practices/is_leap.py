def is_leap(year):
	"""
	input a int, check if is a leap year.
	param: year: an int
	return: True:if input is a leap year
			False: if input is not a leap year.
	"""
	n = int(year)
	return n % 4 == 0  and (n % 100 != 0 or n % 400 == 0)