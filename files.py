#1
print("1st question")
file=open("mbox.txt")
count=0
for i in file:
    count+=1
print(count,"\n")

#2
print("2nd question")
file=open("mbox.txt")
inp=file.read()
print(len(inp))
print(inp[:20],"\n")

#3
print("3rd question")
file=open("mbox.txt")
for i in file:
    if i.startswith("From:"):
        print(i)
print()

#4
print("4th question")
file=open("mbox.txt")
for i in file:
    i=i.rstrip()
    if i.startswith("From:"):
        print(i)
print()

#5
print("5th question")
file=open("mbox.txt")
for i in file:
    i=i.rstrip()
    if not i.startswith("From:"):
        continue
    print(i)
print()

#6
print("6th question")
file=open("mbox.txt")
for i in file:
    i=i.rstrip()
    if not '@uct.ac.za' in i:
        continue
    print(i)
print()

#7
print("7th question")
fname=input("Enter file name:")
file=open(fname)
count=0
for i in file:
    if i.startswith("Subject:"):
        count+=1
print("There were ",count,'subject lines in ',fname)
