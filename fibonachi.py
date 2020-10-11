n=int(input("Enter max number"))

firstnum=1
secondnum=2

m=list(1)#this sequence has two "1" , and we will append other one in next loop

for i in range(1,n+1):
    #find next num, "n" times!
    newnum=firstnum+secondnum
    #find new number that is sum of first and second numbers
    m.append(firstnum)
    #add numbers to list
    firstnum=secondnum
    #new "first number" 
    secondnum=newnum
    #new "second number"
    
print(m)    

#wrote by Moein Rezaie
#github: mrgmcs
#instagram: mrg.mcs
