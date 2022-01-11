## PIP259
## NAME - 20CE034 DEV GUNDALIA
# Github Repository link - https://github.com/20CE034/PIP-II

# A ) Write a Python script to check whether a given key already exists in a dictionary.

schema1={                         # defining a dictionary
    "name":"CHARUSAT",              # key,value
    "state":"GUJARAT",
    "year":2022,
    "Grade":"A",
}
#in
key=input("Enter Key : ")

for i in schema1:
    if i==key:
        print("Key exist")
    
else:
    print("Invalid Input (Key)")

# B ) Write a Python script to merge two Python dictionaries.
##          MERGING
schema2={
    "name":"Hostel",
    "room no":159
}
schema1.update(schema2)
print(schema1)

# C ) Write a Python program to sum all the items in a dictionary.

dict={
    'a':1.002,
    'b':2,
    'c':3
}
values=[] 
for x in dict:
    values.append(dict[x])
sum=sum(values)
print(sum)

# D ) Write a Python script to add a key to a dictionary.

dictionary={
    "1":1729,
    "0":255,
}
dictionary["3"]=2555
print(dictionary)

# E )  Write a Python script to concatenate following dictionaries to create a new one.

d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d4={}
d4.update(d1)
d4.update(d2)
d4.update(d3)
print(d4)