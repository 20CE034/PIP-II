# Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.

# 20CE034 - DEV GUNDALIA
# GitHub Repo Link - https://github.com/20CE034/PIP-II
# stack by using list
class stack:
    def __init__(self):
        self.elements = []
        top = None
        # We use a list to form a stack whcih  have predefined functions like append and pop

    # push operation
    def push(self, element):
        self.elements.append(element)
        # print('pushed')

    # pop function

    def pop(self):
        return self.elements.pop()

    def print(self):
        for i in self.elements:
            print(i)


s1 = stack()

#  push 
s1.push(10)
s1.push(20)
s1.push(30)
#  push elements in stack
print("Elements in the Stack are - ")
s1.print()

#  pop 
s1.pop()
s1.pop()
#  after pop operation
print("Elements in the Stack after two pop operation are -")
s1.print()
