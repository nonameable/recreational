def captcha(string):
	i = 0
	l = len(string)
	half_l = int( l / 2)
	sum = 0
	for c in text:
		c2 =  string[ ((half_l + i + 1) % l) - 1] 
		if c == c2:
			sum = sum + int(c)
		i = i + 1	
	return sum	

file = open('input1', 'r')
text = file.read()
print(str(captcha(text)))
file.close()