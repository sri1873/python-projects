#1
print('Q1')
x=15
print('hello')
def Srikumar():
    print("I wnat to break free")
    print("I want to break freeeeee")
print("PEACE OUT")
x=x+5
Srikumar()
print(x)
print()


#2
print('Q2')
name=str(input('Please enter your name:  '))
def Sri(name):
    if name == 'Sri':
        print('Hello Sri!')
    elif name == 'Bindu':
        print('Hello Bindu')
    elif name == 'Varun':
        print('Hello Varun')
    else:
        print('Hello Varun!')
Sri(name)
print()


#3
print('Q3')
print()
def SRIKUMAR():
    return'hello'
print(SRIKUMAR(), "Bindu")
print(SRIKUMAR(), "Pleased to meet you")  
print()


#4
print('Q4')
def Sri(lang):
    if lang=="jap":
        print("arigato")
    elif lang=="tam":
        print("nandri")
    else:
        print("thank you")
Sri("jap")
Sri("tam")
Sri("eng")
print()


def computepay(hour,rate):
    pay=0
    if hour<=40:
        pay=hour*rate
    else:
        pay=((hour-40)*1.5*rate)+(40*rate)
    return pay
print("The rate is:",computepay(45,10))
