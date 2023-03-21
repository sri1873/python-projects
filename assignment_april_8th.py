#1
COUNT=0
print('before',COUNT)
for i in ("SRIKUMAR",'ARUN','BINDU','AKASH','VARUN','BRO','WHY',
        'SMILIN','BLEH','APARNA','GUNA','RUSHI','MANJITH','SATHI','SABAHAT'):
    COUNT+=1
    print(COUNT,i)
print('After',COUNT)
print()
#2
index=0
print('Before',index)
for marks in (24,48,11,16,40,97,33,95,56,70,75,2,52,88,47,84,59,46,49,81):
              index=index+marks
              print(index,marks)
print('After',index)
print()
#3
index=0
add=0
print('Before',index,add)
for marks in (61,44,92,60,78,34,47,18,74,9,59,27,5,82,
              99,25,46,91,73,64,15,75,76,100,21,93,14,41,35,77):
              index=index+1
              add=add+marks
              print(index,add,marks)
print('After',index,add,add/index)
print()
#4
index=0
print('Before')
for marks in (33,86,87,16,7,34,92):
    if marks>30:
        print('30 is greater than', marks)
print('After')
#5
goal= False
print('Before',goal)
for num in[25,42,15,64,98,23,75,9,21,11]:
    if num==23:
        goal=True
    print(goal,num)
print('After', goal)
print()
#6
smallest=8
print('Before',smallest)
for num in [9,16,7,4,20,2]:
    if num<smallest:
        smallest = num
    print(smallest, num)
print('After', smallest)
print()
