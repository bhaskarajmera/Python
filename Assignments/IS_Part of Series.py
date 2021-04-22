# Write Python code to find if all the numbers in a given list of integers are part of the series defined by the following. 
# f(0) = 0 f(1) = 1 f(n) = 9*f(n-1) - 4*f(n-2) for all n > 1. 
# def is_part_of_series(lst):

def is_part_of_series(lst):
  if lst==0:
    return 0
  elif lst==1:
  	return 1
  else:
  	return 9*is_part_of_series(lst-1)-4*is_part_of_series(lst-2)
for lst in range(0,11):
	print(is_part_of_series(lst))