"""
To retrive value we need to use coresponding key
An object is not an itterable
"""


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def getName(self):
        self.name

    def getAge(self):
        self.age


personObj = Person("Bruce", 44)
print(personObj)
print(getattr(personObj, 'age'))
delattr(personObj, 'name')
# print(personObj.getName())
print(personObj.getAge())
print(vars(personObj))

"""
Object - Big-O time complexity

__init__ O(1) 
The initialization method has a constant time complexity of O(1) because it performs a fixed number of operations, regardless of the size of the input.

print(personObj) - O(1)
The print statement here will call the __str__ method (if implemented) or the __repr__ method of the Person class. If these methods have a constant time complexity, the overall time complexity is O(1).

getattr(personObj, 'age') - O(1)
The getattr function has an average time complexity of O(1), but it can be O(n) in the worst case if the attribute lookup involves traversing the class hierarchy. However, in this case, it's a simple attribute lookup, so the expected time complexity is O(1).

delattr(personObj, 'name') - O(1)
The delattr function has an average time complexity of O(1) as it involves a simple attribute deletion.

print(personObj.getAge()) - O(1)
The getAge method has a constant time complexity of O(1).

vars(personObj) - O(n)
The vars function has a time complexity of O(n), where n is the number of attributes in the object. In this case, it's O(2) because there are two attributes (name and age).
"""
