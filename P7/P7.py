#Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome. 

# 20CE034 - DEV GUNDALIA
# GitHub Repo Link - https://github.com/20CE034/PIP-II

# Test Cases
n=int(input())
list1=[]

for i in range(n):
    b = input()
    list1.append(b)

for i in list1:
    l=len(i)
    
    if l%2==0:
        a=i[:int(l/2)]
        b=i[int((l/2)):]
    else:
        a=i[:int(l/2)]
        b=i[int((l/2)+1):]

    
    a=sorted(a)
    b=sorted(b)
    if a==b:
        print("YES")
    else:
        print("NO")