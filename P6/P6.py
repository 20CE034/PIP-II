# AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

# 20CE034 - DEV GUNDALIA
# GitHub Repo Link - https://github.com/20CE034/PIP-II

a = int(input())          # Test Cases
arr = []
for i in range(a):
    b = input()           # N words
    arr.append(b)

set1 = set(arr)

print(len(set1))

arr2 = []    
arr3 = []   

for i in arr:
    if i in arr2:
        pass
    else:
        arr2.append(i)
        arr3.append(arr.count(i))

for j in arr3:
    print(j, end=' ')  # Number of occurrences
