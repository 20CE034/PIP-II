## PIP259
## NAME - 20CE034 DEV GUNDALIA
# Github Repository link - https://github.com/20CE034/PIP-II
#Code Link - https://github.com/20CE034/PIP-II/blob/main/P2_Set.py


# A ) Write a Python program to add member(s) in a set and clear a set

from typing import List

set= {1,2,3} 
print(set) # before 
set.add(7) # adding
print(set) # after


# B ) Write a Python program to remove an item from a set if it is present in the set.

set={2021,2022,2020,2019}
remove=int(input("Remove from list :"))
for i in set :
    if(i==remove):
        set.remove(remove)
        print("After removal")
        print(set)
        break
    print(i)
else:
    print(remove,"Invalid Input (no data found)")


# C )  Write a Python program to create an intersection, Union, difference of sets.

Set1={1,2,3,4,5,6,7,8,9,0}
Set2={5,6,7,1}

print("intersection of Set1 and Set2 :",Set1.intersection(Set2))
# Union will return the Union of two set as a new set
print("Union of A and B :",Set1.union(Set2))
# Difference will return the Difference of two set as a new set
print("difference of A and B :",Set1.difference(Set2))

# D ) Write a Python program to find maximum and the minimum value in a set.
Set3={1,2,-9,2,0,9}
print("Max in set :",max(Set3))
print("Min in Set :",min(Set3))


# E ) Write a Python program to find the most common elements and their counts from list, tuple, dictionary

# List
count = 0
List = [1,1,1,1,9]
num = List[0]
for i in List:
    curr_frequency = List.count(i)
    if(curr_frequency> count):
        count = curr_frequency
        num = i
print("Repeated Number = ")
print(num)
print("Frequency of Repeated Number =  ")
print(count)


# Dictionary
dic = { 101: 'CHARUSAT',
        102: 'PDEU',
        103: 'SPU',
        104: 'MSU',
        105: 'CHARUSAT',
          }
value=dic.values()

list1=list(value)
count1 = 0
names= list(list1[0])
for i in list1:
    curr_frequency = list1.count(i)
    if(curr_frequency> count1):
        count1 = curr_frequency
        name = i
print("Repeated Value is -  ")
print(names)
print("Frequency of Repeated Value is : ")
print(count1)
