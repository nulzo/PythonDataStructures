from Stack.stack_structure import Stack

# +========================[ Stack Example ]=========================+

stack = Stack(size=5)

stack.push(20)
stack.push(30)

print(f"I can see that the element at the top of the stack is {stack.peek()}!")
top_element = stack.pop()
print(f"I have popped {top_element} from the stack and now the top element is {stack.peek()}!")

top_element = stack.pop()
stack_length = stack.getSize()

print(f"Uh oh... I popped {top_element} and now my stack size is now {stack_length}!")
print("If I pop from my stack, something bad might happen. Let's test it out...\n")

top_element = stack.pop()

print("\nWow! It knew I couldn't remove any more elements!")
print("Now let's add a LOT of elements to my stack (more than the space I have allocated).")

stack.push(2)
stack.push(5)
stack.push(6)
stack.push(8)
stack.push(9)

print(f"\nOk. I added 5 elements. If I add one more I'll go over the size limit of {stack.size}... I wonder what will happen?\n")

stack.push(10)

print(f"\nOh, wow. It wrote over the data at the bottom of my stack! Let me increase the size like it says!")

stack.increaseSize(10)

print(f"Ok, I increased my size to {stack.size}... let's try that again!")

stack.push(2)

print(f"\nAwesome, no warnings! It must've added it!")
print(f"These stacks are awesome! Let me print out my entire stack to see what is in it!\n")

print(stack)

print(f"\nOh, I had no idea you shouldn't display the whole stack!")
print(f"Well, maybe I am supposed to simply loop through the stack? Let me try that out!\n")

for element in stack:
    print(element)

print(f"\nOh, jeez! So I shouldn't loop through a stack OR try to display the whole stack...")
print(f"I guess I *should* just stick with push(), pop(), and peek() methods!")
print(f"Well, let's clear this stack then!\n")

stack.clearStack()

print(f"Looks like the length of my stack is now {stack.getSize()}. It really did clear it!")
print("I can't wait to use my newfound understanding of stacks... Think of all the things I can do with them!\n")



