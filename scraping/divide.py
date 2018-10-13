import os.path

f = open('side.txt')
g = ''
u = 0
for i in f:
    k = i.split()
    if len(k) >1 and k[1] == 'done':
	if os.path.exists('d/'+k[0]+'.txt'):
		v = open('d/'+k[0]+'.txt', 'a')
		v.write(g)
	g=''
        
    else:
        g = g+i
	g = g + '\n'
