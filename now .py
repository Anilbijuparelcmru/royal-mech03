import random
count=0
def myroll():
	return random.randint(1,6)

while(count<=100):
	n=input("press r to roll the dice")
	if(n=='r'):
		r=myroll()
		count=count+r
		print("u got",r)
		print("new position is",count)

		if(count==8):
			count=37
			print("i got the ladder")
		elif(count==40):
			count=68
			print("sorry,u got snake")
		elif(count==38):
			count=9
			print("i got the ladder")
		elif(count==99):
			count=99+1
			print("i won")
		