# Stack using list
stack = []

# Push
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack:", stack)

# Pop
print("Popped:", stack.pop())
print("Stack after pop:", stack)

# Peek
print("Top element:", stack[-1])

# Check empty
print("Is empty?", len(stack) == 0)
