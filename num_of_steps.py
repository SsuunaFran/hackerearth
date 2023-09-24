array= input("Enter list length : ")
l1= list(map(int,(input("List a : ").split(' '))))
l2= list(map(int,(input("List b : ").split(' '))))
steps=0
# function to check if all elements in the llist are equal
def Equal(list):
    positive,negative = 0,0
    for pos in range(len(list)-1):
        if list[pos] == list[pos+1]:
            positive+=1
        else:
            negative+=1
    if negative == 0:
        return True
    else:
        return False   
    
def Equate(list1,list2,steps):    
    possible=0
    minimum=min(list1)            
    for a in list1:
        position=list1.index(a)
        if a >= list2[position] and a > minimum:
            # print(f"{a}-{list2[position]}")
            a=a-list2[position]
            list1[position]=a
            # print(list1)
            possible+=1
            steps+=1
    if possible == 0:
        print(-1)
        return
    elif Equal(list1):
        print(steps)
        return 
    elif not Equal(list1):
        return Equate(list1,list2,steps)
       
if Equal(l1):
    print(steps)
else:
    Equate(l1,l2,steps)


    






