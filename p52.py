x = 1
while True:
	x2, x3, x4, x5, x6 = 2*x,3*x, 4*x, 5*x, 6*x
	x2_list, x3_list, x4_list, x5_list, x6_list = sorted(list(str(x2))), sorted(list(str(x3))), sorted(list(str(x4))), sorted(list(str(x5))), sorted(list(str(x6)))
	if x2_list == x3_list == x4_list == x5_list == x6_list:
		print(x)
		break
	x += 1
