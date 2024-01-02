def displayGrade(mark):
	if 100 >= mark >= 90:
		print(mark, " A")
	elif 89 >= mark >= 80:
		print(mark, " B")
	elif 79 >= mark >= 0:
		print(mark, " C")
	else:
		print(mark, " invalid")

for i in range(-1, 102):
	displayGrade(i)