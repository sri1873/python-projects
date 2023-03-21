p=int(input("Enter the principle amount"))
r=int(input("Enter the Rate of Interest"))
t=int(input("Enter the Time Period"))
SR=(p*t*r)/100
print(SR)

#2
num_1=int(input("Enter the First number"))
num_2=int(input("Enter the 2nd number"))
if num_1>num_2:
          print(num_1," is greater than",num_2)
else:
    print(num_2," is greater than",num_1)
