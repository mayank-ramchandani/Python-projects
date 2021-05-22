def inputnumbers():
    x = int(input("Enter the value of number"))
    y = int(input("Enter the value of divisible"))
    return x,y
def isDivisible(Num1 , Num2):
    if Num1 %Num2 == 0 :
        print (True)
    else:
        print (False)
def Main():
    x,y = inputnumbers() 
    isDivisible(x,y) 
    
Main()
