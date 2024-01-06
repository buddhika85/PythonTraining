def print_grade(mark):
	if mark >= 90 and mark <= 100:
		print("A")
	elif mark >= 80 and mark <= 89:
		print("B")
	else:
		print("C")

print_grade(90)
print_grade(80)
print_grade(75)