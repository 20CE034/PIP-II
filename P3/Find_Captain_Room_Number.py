# 20CE034 - GUNDALIA DEV
N = int(input())  #input N group

list1 =map(int,input().split()) #input elements of the room number list.
list1 = sorted(list1)

for i in range(len(list1)):
    if i!=len(list1)-1 :
        if list1[i]!=list1[i-1] and list1[i]!=list1[i+1] :
            print(list1[i]) # Captain's room number.
    else:
        print(list1[i])  # Captain's room number.