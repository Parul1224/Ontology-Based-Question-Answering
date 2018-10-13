output = open("test_questions3.txt", "a")
inpu=input("Enter")
filen=open(inpu,"r")
lines1 = filen.readlines()
x=0
for i in lines1:
    x=x+1
    if x>=21:
        output.write(i)
output.close()
filen.close()
