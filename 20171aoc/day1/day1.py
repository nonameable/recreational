file = open('input1', 'r')
text = file.read()
sum = 0
p = 'p'
for c in text:
    if c == p:
		sum = sum + int(c)
	p = c
if p == text[0]:
	sum = sum + int(p)

print(str(sum))
file.close()
