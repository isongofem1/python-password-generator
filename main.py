#single line  comment 
'this is multi comment'

#output in python
print()

#variables
good_day=15
day='monday'
print(good_day)
print(day)

#datatypes in python
#strings
a='gabriel' #single quote 
b='james' #double quote
print(type(a))

#integers 
c=5
d=6
print(type(c))
 
#float
e=5.5
f=6.6
print(type(e))


#boolean
g=True
h=False
print(type(g))

#list
i=['list',2,3,True]
print(type(i))

#tuple
j=('list', 2, 3, True)
print(type(j))


#dictionary
k ={'key1':'hello', 'key2':15, 'key3':'hello', 'key4':'hello', 'key5':['cody,18''hello']} 
print(type(k))

#set
l={'listl', 2, 3.3, True}
print(type(l))




#operators
#Arithmetic operators
m=5
n=3
print(m+n)
print(m-n)
print(m/n)
print(m*n)
print(m%n)
print(m**n)
print(m//n)

L=25
M=15
print(L+M)
print(L-M)
print(L/M)
print(L*M)
print(L%M)
print(L**M)
print(L//M)


#COMPARISON operator

o=10
p=5
print(o==p)
print(o!=p)
print(o>p)
print(o<p)
print(o>=p)
print(o<=p)


#Logical operators

q=2.2
r=2.3
print((q!=r) and (q<r))

print(q!=r)
      
Q=5.5
R=8.6
print(Q!=R and Q<R)
print(q==r or Q<R)
print(not(Q==R and Q>R))


#Identity operators
print(q is r)
print(q is not r)

s=5.0
u=5
print(s is u)
print(s is not u)

#Membership operator

sequence =[1,2,3,4,5,6,7,8,9]
print(1 in sequence)
print(2 not in sequence)

#Assignment operators

live= 15
live +=1
live -=1
print(live)

#membership
s=[5,10,15,20,25,30]

print(5 in s)
print(6  in s)
print(9  in s)
print(10 in s)
print(15 in s)


print(5 not in s)
print (6 not in s)
print(8 not in s)
print(10 not in s)
print(20 not in s)

x=['apple','banana']
y=['apple','orange']

print(y is x)
print(x is not y )

#conditinal statement

var1 = 5
var2 = 10

if var1 > var2:
    print('first condition met')
elif var1== var2:
    print('second condition met')
elif var1 < var2:
    print('third condition met')
elif var1!=var2:
    print('fourth condition met')
else:
    print('last condition met')


s= 'abcdefghijklmno'
if 'p' in s:
  print('p is in sequence')
elif 'q' in s:
  print('s is in sequence')
elif 'd' in s:
  print('dis in sequence') 
else:
  print('none of the string is in sequence')



listl = ('hi', 2,3.3, True)
if 'hi' not in  listl:
    print('hello')
else:
    print('bye')



x=5
y=8
if x is y:
    print(x is y)
elif y is x:
    print(y is not  x)
else:
   print('hello')

#looping
#for loop 
   
for i in range(10):
   print(i)

for j in range(20):
   print(j)

"""
for k in range(10):
   numb1=eval(input('enter a number to find its square:')) 

   if numb1:
      print(numb1 **2) 
"""

      
"""for i in range(3):
   
   n=eval(input('enter first number to compare'))
   print()
   
   n2 = eval(input('enter second number to compare'))

   if n > n2:
      print('first number is greater')

   elif n< n2:
      print('second number is greater')
   else:
      print('none is greater')
"""

seq= ['a','b','c','d','e']

if 'f'  in seq:
    print('f is in sequence')
elif 'j' in seq:
    print('j in sequence')
elif 'k' in seq:
    print('k in sequence')
elif 'd' in seq:
    print('d in sequence') 
else:
    print(None) 


#while loop

x = 0
while x < 5:
    print('hello')
    x+=1 

x=5
while x<20:
    print('hello')    
    x+=1


j=0
while  j<20:
    print('1+j')  
    j+=1

"""
j=0
while j < 20:
    o=15
    p=25
    q=30

    if o > p and o < q:
        print('condition 1 is correct')

    elif p > o and p < o :
        print('condition 2 is correct')

    elif q>o and q < p:
        print('condition 3 is correct')

    else:
        print('no condition is correct')
        
    j+=1
"""

#classwork
lm = ['ball,''apple,''monkey''jose']

k=0
while k < 5:
    if 'ball' in lm:
        print('ball is available')
    elif 'mango' in lm:
        print('mango is available')
    elif 'sheep' in lm:
        print('sheep is available')
    else:
        print('no sheep available')

    k+=1

#string 
#concatination
print('hello' + 'welcome to' +'torbita')
print('Programming' + 'is' + 'coding')

#repitition
print('xauusd is perfect to win'* 3)
print('programming' *2)

prompt = input('enter a word:')
print(prompt * 2)

#indexing
joe = 'programming languages' 
print(joe[0]) 
print(joe)
print(joe[2])
print(joe[3]) 
print(joe[4])
print(joe[5])
print(joe[6])
print(joe[7])
print(joe[8])
print(joe[9])
print(joe[10])
print()
print(joe[-1])
print(joe[-2])
print(joe[-3])
print(joe[-4])
print(joe[-5])
print(joe[-6])
print(joe[-7])
print(joe[-8])

#slicing
print(joe[1:6])
print(joe[1:8:2])

#upper()
print(joe.upper())
print(joe.lower())

#replace()
print(joe.replace('programming','coding'))

#count()
print(joe.count('m'))

hakari= 'photosynthensis is physics' 

#capitalize()
print(hakari.capitalize())

#split()
print(hakari.split(' '))

#index()
print(hakari.index('n'))

#isalpha
print(hakari.isalpha())

#isnum()
print(hakari.isnumeric())

#join()
print(hakari.join(joe))

#list method

#list concatination

print([1,2,3,4,] + ['a','b','c','d'])

maki =['string',2,3.5,True]
mai =[False, 3,2.5,'integer']
print(maki + mai)


#list repetition
print(maki * 5)
print(mai * 2)

#indexing list
print(maki[0])


#Append()
fx=['AUD','GBP','CAD']
fx.append('USD')
fx.append('XAU')
fx.append('AUD')

#insert()
fx.insert(1, 'EUR')
fx.insert(3,'JpY')

#Remove()
fx.remove('AUD')

#pop()
fx.pop(2)


#Reverse()
fx.reverse()


#sort()
fx.sort()
print(fx.sort(reverse=True))



#count()
print(fx.count('EUR'))


#index()
print(fx.index('CAD'))

print(fx)

print(len(fx))
print(min(fx))
print(max(fx))


brown=['black','bull','ball']

brown.append('book')
brown.append('blue')
print(brown)
brown.insert(2, 'black')

brown.reverse()
brown.pop(2)
print(brown)
brown.sort()
print(brown)

brown.append('blue')
print(brown.count('blue'))
brown.index('black')
print(brown) 

print(len(brown))
print(min(brown))
print(max(brown))



#tuple 

tp1=(1,2,3,4,'Hi')
tp2=(5,6,7,'Hello')

#concatination
print(tp1 + tp2)

#repitition
print(tp1 *3)

#indexing
print(tp1[3])

#slicing
print(tp1[ 0:4]) 



#set
set1={1,2,3,4}
set2={2,4,8}


#union
print(set1 | set2)

#interset
print(set1 & set2)

#different of 2 sets
print(set1-set2)
print(set2-set1)

#symmetric set
print(set1 ^ set2)
 
#methodofset
set3 = {1, 2.2, 'three', True, 'five', False}
set3.add('six')

print(set3)

#remove()
set3.remove(False)

print(set3)

#issubset()
r=set1.issubset(set2)
 #issuperset()

s=set2.issuperset(set1)

print(set3)
print(r)
print(s)
 
 #dictionary
months={'january':31,'february':29, 'march':31,'april':30,'may':31,'june':30, 'july':31,'august':31,'september':30, 'october':31,'november':31,'december':31 }

print(months['january'])
print(months['february'])
print(months['march'])

#changing items in dictionary
item = {'A':100,'B':200,'C':300, 'D':800}
print(item)  
item['C']=400
item['D']=600
print(item)


#dictionary methods
#get()
s=item.get('A')
print(s)

#update()
item.update({'E':800,'F':1000})
print(item)

#pop()
item.pop('E')

#copy()
it = item.copy
print(it)  

#key()
h = item.keys()
print(h)

#values()
I= item.values()
print(I) 

#items()  
n=item.items()
print(n)

#popitem()
item.popitem()

#functions

def ball():
    print('ball')
    
def multi(num):
    return num *2

multi = multi(2) #calling a function
print(multi)

def user(first_name, last_name,age):
    return f'{ first_name } {last_name} is {age} years old'
for i in range(4):
    first_name = input('input your first name(Gabriel):')
    last_name = input('input your last name(william):')
    age = eval(input('input your age(28): '))  

    user_data = user(first_name, last_name, age)
    print(user_data)

    #keyword argument

def args(color1, color2, color3):
    return f"{color1} is the first color, {color2} is the second, {color3} is the third"

arg = args(color2='Blue', color3='Black', color1='Red')
print(arg)


def ab_args(**kwargs):
    return f"{kwargs['food1']}, {kwargs['food2']}, {kwargs['food3']}" 

ab = ab_args(food1='red', food2='beans', food3= 'chiken') 
print(ab)      

def kwargs(q, r,s, t):
    return q + r * s - t
kw = kwargs(q=5, s=6, r=7, t=8 )
print(kw)

#ARBITRARY KEYWORD ARGUMENT

def ab_args(**arb):
 return arb['s'] +arb['t']*arb['u']-arb['v']

akw = ab_args(s=6, t=8,u=10,v=2)
print(akw)


#default Arguments
def default(a,b,c,d=8):
    return a+ b + c + d

deflt= default(5,6,4)
print(deflt)

#global

def func1(a,b,c):
    global x
    x=5
    return(a + b+ c) * x

def func2(a,b):
    return(a+b)* x

func = func1(2,4,6)
print(func)

funct = func2(8,10)
print(funct)

#pass
def p():
    pass
 

#class
class Data:
    def __init__(self, first_name,midddle_name,last_name):
        self.first_name = first_name
        self.midddle_name = midddle_name
        self.last_name =last_name

    def first_names(self):
        return self.first_name
    
    def midddle_names(self):
        return self.midddle_name
    
    def last_names(self):
        return self.last_name
    
    def full_names(self):
        return self.first_name + ' ' +self.midddle_name + ' ' + self. last_name
    
data= Data('gabriel', 'Eshimoghe', 'williams')
print(data.last_names())
print(data. midddle_names())
print(data.first_names())
print(data.full_names())

class Arithmetic:
    def __init__(self,a,b):
        self.a =a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a- self.b
    
    def mult(self):
        return self.a* self.b
    def div(self):
        return self.a/ self.b
    
    def mod(self):
        return self. a & self.b 
    
    def expo(self):
        return self.a ** self.b 
    
    def floor(self):
        return self.a // self.b 



arith= Arithmetic(7,8)
print(arith.add())
print(arith.sub())
print(arith.div())
print(arith.mult())
print(arith.expo())
print(arith.mod())
print(arith.floor())
        

#class inheritance
class Parent:
    def __init__(self,lands, estates, companies, cars):
        self.lands = lands
        self.estates = estates
        self.companies = companies
        self.cars = cars

    def est(self):
        return self.estates
    
    def land(self):
        return self.lands
    
    def comp(self):
         return self.companies
    
    def car(self):
        return self.cars
    
class Child(Parent):
    def __init__(self ,lands, estates, companies, cars, house, buses, school):
        Parent.__init__(self, lands, estates, companies, cars)
        self.house = house
        self.buses = buses
        self.school = school

    def own_wealth(self):
        return f'{self.house}, {self.buses}, {self.school}'


parent= Parent(5,8,2,18)
print(parent.est())
print(parent.land())
print(parent.comp())
print(parent.car())

child = Child(5,8,2,18,1,1,1)
print(child.own_wealth())
print(child.est())
print(child.land())
print(child.comp())
print(child.car())


class Details:
    def __init__(self , quantity,item_no,price):
        self.quantity=quantity 
        self.item_no= item_no
        self.price = price

    def Details(self):
        return f'quantity:{self.quantity},item_number:{self.item_no}, price:${self.price}'
    
    class good(Details):
        def__init__(self,quantity,item_no, price,good):
        Details__init__ (self,quantity,item_no,price)
        self.good=good

        def good(self):
            return f'good:{self.good}'
        
        def all__details(self):
            return f'quantity:{self.quantity},item_number{self.item_no},price:${self.price},good:{self.good}

            product= good(5,567,50, 'apple watch')
            print(



#exception
try:
input_num = eval(input("pls write down a number of your choice:"))
print(4/input_num)                    

except ZeroDivisionError:
print('at divide by zero')

except:
print('wrong value inputed')
      
      else 
      print('you are good to go')
      

      #string formatting
      item = "ios smartnwatch"
      item_no =345
      price = 50
      all_out = "{} with item unmber {} is ${}' 
      print(all_out.format(item, item_no, price))

      #Modules
      import Module
      from module import greet, Name 
      fr  