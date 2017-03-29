# -*- coding: utf-8 -*-

'''
@author: Sky Hai
@contact: hsssgddtc@hotmail.com
@file: 03.control_structure.py
@time: 2017/3/29 11:39
@desc: Python control structure
'''

# Selective

## if...elif...else
var = 100
if var == 200:
   print("1 - Got a true expression value")
   print(var)
elif var == 150:
   print("2 - Got a true expression value")
   print(var)
elif var == 100:
   print("3 - Got a true expression value")
   print(var)
else:
   print("4 - Got a false expression value")
   print(var)

print("Good bye!")

## nesting
var = 100
if var < 200:
   print("Expression value is less than 200")
   if var == 150:
      print("Which is 150")
   elif var == 100:
      print("Which is 100")
   elif var == 50:
      print("Which is 50")
elif var < 50:
   print("Expression value is less than 50")
else:
   print("Could not find true expression")

print("Good bye!")
# Cycle

## while
count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1

print("Good bye!")

### else with while
count = 0
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")
   
### nesting
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print(i, " is prime")
   i = i + 1

print("Good bye!")

## for
for letter in 'Python':     # First Example
   print('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print('Current fruit :', fruit)

print("Good bye!")

### range
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print('Current fruit :', fruits[index])

print("Good bye!")

### else with for/nesting
for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print('%d equals %d * %d' % (num,i,j))
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print(num, 'is a prime number')


## break
for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)
    var = var - 1
    if var == 5:
        break

print("Good bye!")

## continue
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('Current variable value :', var)
print("Good bye!")

## pass
for letter in 'Python': 
   if letter == 'h':
      pass
      print('This is pass block')
   print('Current Letter :', letter)

print("Good bye!")

# Recursion

## factorial
def factorial(n) :
  if n == 1 :
    return 1
  return n * factorial(n - 1)

print(factorial(5))

#
i = 1
def move(n, mfrom, mto) :
  global i
  print("Step#%d: Move plate#%d from %s -> %s" %(i, n, mfrom, mto))
  i += 1

def hanoi(n, A, B, C) :
  if n == 1 :
    move(1, A, C)
  else :
    hanoi(n - 1, A, C, B) 
    move(n, A, C)    
    hanoi(n - 1, B, A, C)

n = 3
print("Move steps as following：")
hanoi(n, 'A', 'B', 'C')

## fibonacci
def fib_list(n) :
  if n == 1 or n == 2 :
    return 1
  else :
    m = fib_list(n - 1) + fib_list(n - 2)
    return m

n = 5
list2 = [0]
tmp = 1
while(tmp <= n):
  list2.append(fib_list(tmp))
  tmp += 1
print(list2)