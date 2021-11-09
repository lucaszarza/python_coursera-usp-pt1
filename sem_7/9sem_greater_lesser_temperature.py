def mininum_temperature(arr_temp):
	min_val = arr_temp[0]
	i = 1
	while i < len(arr_temp): 
		if (i < min_val):
			min_val = arr_temp[i]
		i += 1
	return min_val

def maximum_temperature(arr_temp):
	max_val = arr_temp[0]
	i = 1
	while i < len(arr_temp): 
		if (i > max_val):
			max_val = arr_temp[i]
		i += 1
	return max_val

def min_max(temperature):
	print(temperature)
	print(f'A menor temperatura do mês foi de: {mininum_temperature(temperature)}')
	print(f'A maior temperatura do mês foi de: {maximum_temperature(temperature)}\n')

def main():
	min_max([1,2,3,4,5,6,7])
	min_max([-1,-2,-3,-4,-5,-6,-7])
	min_max([-1,-2,-3,-4,-5,-6,-7,-50,100,30,31,312,3,11,54,1,42,3,12,312,31,541,3,12,31])

main()