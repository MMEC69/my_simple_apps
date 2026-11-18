stack = []

# Using a Python list as a stack:
# push
stack.append("A")
stack.append("B")
stack.append("C")
print(f"Stack: {stack}")

# peek
topElement = stack[-1]
print(f"Peek: {topElement}")

# pop
poppedElement = stack.pop()
print(f"Pop: {poppedElement}")

# stack after pop
print(f"Stack after Pop: {stack}")

# isEmpty
isEmpty = not bool(stack)
print(f"isEmpty: {isEmpty}")

# Size
print(f"Size: {len(stack)}")