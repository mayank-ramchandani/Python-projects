columns = int(input("enter the number of columns you want :"))
thing = input("enter the character/word you want :")
midspace = columns - 2
initialspace = 0
space = (' ' * len(thing))
columncounter = 0
if columns % 2 != 0:
    while midspace > 0 :
        print(initialspace* space , thing , space * midspace , thing , initialspace * space ) 
        initialspace +=1
        midspace -=2
    print(initialspace * space, thing , initialspace * space )
    if midspace < 0 :
        while columncounter != columns//2:
            initialspace -= 1
            midspace += 2
            print(initialspace * space, thing, space * midspace, thing, initialspace * space)
            columncounter +=1
close = input("press anything to stop program")
