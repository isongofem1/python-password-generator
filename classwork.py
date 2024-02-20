 #classwork
#dictionary
yaya = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6}

#keys()
ya= yaya.keys()
print(ya)

a= yaya.values()
print(a)

y= yaya.items()
print(y)

yaya.popitem()
print(yaya) 


#Assignment
#number guessing games
import random

num=random.randint(1,10)
for i in range(6):
    guess=int(input('guess a number between 1 and 10: '))
    if guess < num:
        print('your guess is too low, try again')
    elif guess > num:
        print('your guess is too high, try again')   
    else:
        print('you guessed it right.')
        break


#classwork
    
def kwargs(sentence1,sentence2, sentence3):
    return sentence1 + sentence2 + sentence3
OF=kwargs(sentence1='MR OFEM NA SENIOR MAN ',sentence2='HIM FACE SHOW ',sentence3='HIM SHOE SHINE' )

print(OF)


#classwork 
class Comparison:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def equal(self):
        return self.a==self.b 
    def less(self):
        return self.a < self.b 
    def greater(self):
        return  self.a > self.b 
    def lessor(self):
        return self.a <= self.b 
    def greator(self):
        return self.a >=self.b 
    def noteq(self):
        return self.a!=self.b 

compare = Comparison(7, 8) 
print(compare.equal())
print(compare.less())
print(compare.greater())  
print(compare.lessor())
print(compare.greator())
print(compare.noteq()) 



#Assignment class comparison

class number:
    def__init__(self,n1,n2)
    self.n1 = n1
    self.n2 = m2

    def logic1(self):
        return self.n1



#assignment
#password generator
# importing the relevant
import random
from random import randint

#all upper password
password= ""

for i in range(10):
    i= chr(randint(65,98))
    password = str(password) + i
    print(password)

#upper and lowercase power
    password = ""
    for i in range(5):
      i= chr(randint(65, 98))
    for j in range(5):
        j = chr(randint(65,98)).lower()

        password =str(password) + i + j
    print(password)   


