def format_string (line):
	print(line)
	print(type(line))
	print("----------------------------")
	line2 = line.replace("[\s]+", "$")
	print(line2)
	print("----------------------------")
	

with open('input') as file:
	line = file.readline()
	format_string(line)