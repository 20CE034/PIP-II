
#without floating point
print(7//2)

#may contain floating point
print(7/2)

#modulo
print(10%5)

#exponential (2^3)
print(2**3)

#constants
print('Value of pi is ',3.14)

#declaring variable at the top first
a=3

print(a)

#complex number
print('Multiplying complex number',(1+1j)*(1+2j))

#length of char,int & Printing some strings
print(len('DEV'))
print(len('DEV')>len('XYZW'))
print(True==True)
print("""Works""")
print('''Also 


                works''')

f_name="DEV"
l_name="G"
space=" "
#storing in strings
full_name=f_name+space+l_name
print(full_name)
print(len(f_name))
print(len(l_name))
print(len(full_name))

#strings and storing char`s
lan1="Python"
a,b,c,d,e,f=lan1
print(d)
last_char=lan1[-1]
last_char_0=lan1[0]
print(last_char) # starts from last -1
print(last_char_0) # starts from first 0

#slicing
slice1=lan1[:-1]
print(slice1)

#skipping char`s
slice2=lan1[0:6:2] # 0 wont work (can`t skip zero)
print(slice2)

#for storing more char in pointer
lan="Python"
a,b,c,*d=lan
print(*d)

#using \t (tabs)

print('Day\t H')
print('Day 1\t3\t5 ')
print('DayPPP 2\t3\t5 ')

print('\\') #backslash  \\ = \

print('\"Hello\"') #printing 2xcomma  \" = "

# capitalize()
print(lan1.capitalize())

# count()
print(lan1.count('P'))
print(lan1.count('P',0,7)) # from 0 to 7 (index)
print(lan1.count('Py'))

# endswith()
prac="hello in \tlab"
print(prac)
print(prac.endswith('ab'))

# expandtabs()
print(prac.expandtabs(8))

# find() - position of char/string
print(prac.find('lab'))

#format() 
x_name='hello'
y_name='my'
z_name='name'
w_name='is'
sentence= '{} {} {} {} DEV.'.format(x_name,y_name,z_name,w_name)
print(sentence)

# isalnum() - checks if all alpha+ num

# isalpha() - checks if all char are alphabets 

# isdigit() - if num

# isdecimal() -checks if num is decimal 

num='10'
print(num.isdecimal())

num='10.55'
print(num.isdecimal())

# isidentifier() - checks valid variable names


string='_var'
print(string.isidentifier())

string1='2ok'
print(string1.isidentifier())

# islower() - checks if all alph are lowercase lly , isupper()

print(string.islower())

# isnumeric() - check for num

# join() - "Hi"+"World"
web={'html','css','js'}
res=' also use ,'.join(web)
print(res)

# strip() - removes leading and trailing chars
str1='x   i am in python lab'
print(str1.strip('x')) # argument must be leading char

# replace() -  replaces substring inside


# split() - splits chars from left

# swapcase() - case swap

# startswith()