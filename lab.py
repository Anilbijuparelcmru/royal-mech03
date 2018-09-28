import random
while True:
	a=input('press r to roll the dice:')
	if(a=='r'):
		r=random.randint(1,6)
		print(r)
	else:
		print('wrong key!!')
		break

	