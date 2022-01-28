# 20CE034 - GUNDALIA DEV
N = int(input()) # scores

list1=map(int,input().split()) # n scores (listarray)

list1 = sorted(list1) #sorting 
new_list = []

for i in list1:
    if i not in new_list:
        new_list.append(i)

if len(new_list)>1:
    print(new_list[len(new_list)-2])