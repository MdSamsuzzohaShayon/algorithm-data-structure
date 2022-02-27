print("🔩🔩🔩 Stacks 🔸🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹▪️ ▫🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫")
# PUSH AN ITEM INTO THE STACK
# LIFO - LAST-IN-FIRST-OUT
# ALL PUSH AND POP OPERATIONS ARE TO/FROM THE TOP OF THE STACK
# UNDO - STACK WHICH COMMANDS HAVE BEEN EXECUTED. POP LAST COMMAND OFF COMMAND STACK TO UNDO IT

my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(9)
my_stack.append(5)
my_stack.append(2)
print(my_stack)  # [4, 7, 9, 5, 2]
print(my_stack.pop())  # 2
print(my_stack.pop())  # 5
print(my_stack)  # [4, 7, 9]

print("\n\n🔩🔩🔩 STACK WITH WRAPPER 🔸🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫🔹▪️ ▫🔹▪️ ▫🔹🔸▪️ ▫🔹🔸▪️ ▫")


# WE CREATE A STACK CLASS AND A FULL SET OF STACK METHODS BUT THE UNDERLYING DATA STRUCTURE IS REALLY  A PYTHON LIST.
# FOR POP AND PEEK METHODS WE FIRST CHECK WHETHER THE STACK IS VACANT, TO AVOID EXCEPTION
class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        return str(self.stack)

my_stack = Stack()
my_stack.push(1)
my_stack.push(3)
print(my_stack) # [1, 3]
print(my_stack.pop()) # 3
print(my_stack.peek()) # 1
print(my_stack.pop()) # 1
print(my_stack.pop()) # None
