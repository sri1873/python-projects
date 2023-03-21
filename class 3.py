#1
print('Q1')
print('Multi Way: no else')
print()
x=int(input('enter a number: '))
if x<2:
    print("small")
elif x<10:
    print("medium")
print("all done")


#2
print('Q2')
print('Multi Way: puzzles')
print()
x=int(input('enter a number: '))
if x<2:
    print('Below 2')
elif x>=2:
    print('two or more')
else:
    print('something else')
#for x= 5 and 50

#3
print('Q3')
print('Multi Way: puzzles')
print()
x=int(input('enter a number: '))
if x<2:
    print('below 2')
elif x<20:
   print('below 20')
elif x<10:
    print('below 10')
else:
    print('something else')

#3
hour=float(input('Enter the number of hours:  '))
rate=float(input('Enter the rate:  '))
pay=0
if hour<=40:
    pay=hour*rate
elif hour>40:
    pay=40*rate
    hour-=40
    rate*=1.5
    pay+=hour*rate
print(pay)

#4
try:
    hour1=float(input('Enter the number of hours:  '))
except:
    print("Ërror please enter numeric input")
try:
    rate1=float(input('Enter the rate:  '))
except:
    print("Ërror please enter numeric input")
pay=0
if hour1<=40:
    pay=hour1*rate1
elif hour1>40:
    pay=40*rate1
    hour1-=40
    rate1*=1.5
    pay+=hour1*rate1
print(pay)