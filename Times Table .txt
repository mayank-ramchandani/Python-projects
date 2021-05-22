def OutputTimesTable():
    n = int(input("Enter the times' table you would like to see"))
    end = int(input("Till which number would like to see?"))
    for i in range (1,end+1):
        print( i , "x" , n , "=" , (i*n))
    print()
    k=input("Press any key on the keyboard and program closes")

OutputTimesTable()