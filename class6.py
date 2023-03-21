#1
print('Q1')
print('Loops and Iteration')
print()
n=int(input('Enter a number: '))
while n>0:
    print(n)
    n=n-1
print('Awesome!')
print(n)
#2
print('Q2')
print('Loops and Iteration')
print()
n=int(input('Enter a number: '))
while n>0:
    print('Lather')
    print('rinse')
print('dry off')
print(n)
#3
print('Q3')
print('Break statement')
print()
while True:
    line = input('>')
    if line=='done':
        break
    print(line)
print('done')
#4
print('Q4')
print('Continue statement')
print()
while True:
    line = input('>')
    if line[0]== '#':
        continue
    if line=='done':
        break
    print(line)
print('done')
