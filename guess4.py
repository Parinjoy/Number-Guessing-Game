f=open('highscore1.txt','r')
highscore=int(f.read())
f.close()

import random
buf=[]

def caller(a):
	global buf
	c=random.randint(0,a-1)
	if c not in buf:
		buf.append(c)
		return c
	else:
		return caller(a)

def check(a):
	global sol
	global buf
	count=0
	b=list(str(a))
	for j in range(l):
		i=caller(l)
		if b[i] in sol and b[i]==sol[i]:
			print ('ga',end=' ')
			count+=1
		elif b[i] in sol and b[i]!=sol[i]:
			print ('re',end=' ')
		elif b[i] not in sol:
			print ('sa',end=' ')
	print ('\r')
	buf=[]
	return count

def guessing():
	global counter
	global l
	global n
	for i in range(20):
		counter+=1
		n=int(input('Enter a number :'))
		try:
			if len(str(n))==l:
				p=check(n)
				if p==l:
					print('You guessed it right !')
					print ('Your Score is :',counter)
					if counter<highscore:
						print('You have set a new highscore !')
						f=open('highscore1.txt','w')
						f.write(str(counter))
						f.close()
					else:
						print ('highscore is :',highscore)
		except:
			pass
		finally:
			if len(str(n))!=l:
				print ('Please enter',l,'digit number')
			elif p==l:
				break
	else:
		print('Sorry, tries over')
		confess=input('Do you want more tries ? (y/n)')
		if confess=='y':
			guessing()
		else:
			print ('The correct number is :',num)

ans='y'		
while ans=='y':
	print('Welcome to the guessing game')
	print ('sa : wrong number')
	print ('re : correct number, wrong position')
	print('ga : correct number, correct position')
	l=int(input('Enter number of digits of the number you want to guess: '))
	num=random.randint(10**(l-1),(10**l)-1)
	sol=list(str(num))
	print ('Guess a',l,'digit number')
	counter=0
	guessing()
	ans=input('Do you want to play again ? (y/n)')