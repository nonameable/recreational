def delta_line (line):
	new_line = line.splitlines()[0]
	numbers = new_line.split("-")
	smallest = 10000
	biggest = -1
	for number_as_string in numbers:
		number = int(number_as_string)
		if number > biggest:
			biggest = number
		if number < smallest:
			smallest = number
	delta = biggest - smallest
	return delta

with open('inputv2') as file:
	checksum = 0
	for line in file:
		if 'str' in line:
			break
		checksum = checksum + delta_line(line)
	print(str(checksum))