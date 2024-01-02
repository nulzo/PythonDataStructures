class Stack:
    """"
        Author: Nolan Gregory
        Date: 15th April, 2023
        Purpose: I use this as an abstraction away from using lists when doing work that require 
        stacks (particularly of a fixed size). Implements all the key features that a stack needs.
        Simple yet useful. If you want to just use an array then use an array. If you want to use a python
        stack library then use that. Doesn't matter in the long run. Do whatever makes you happy.
        
        Class Constructor Parameters:
            - *args:    Initally adds these values to your stack. Pass however many numbers you 
                        want into here (as long as there aren't more than your size...).

            - size:     By default this is set to 100. This is the size of your stack. Sometimes less is more.

            - warnings: How descriptive you want the error messages to be. 
                        "Verbose": Set to verbose by default. Shows all warnings and suggestions.
                        "Essential": Only show a warnings if you are doing something really bad.
                        "Off": Yeah. Ok. Turns ALL warnings off. Don't use this flag...

        Methods:
            - pop():
                parameters:     None
                returns:        last element from the stack (remember LIFO from your university data structures course). 

            - push():
                parameters:     None
                returns:        None. Just adds the element to the top of the stack.

            - increaseSize():
                parameters:     An integer that increases the size of your stack. You can pass in a float, but it'll
                                just get truncated.
                returns:        None

            - decreaseSize():
                parameters:     An integer that decreases the size of your stack. You can pass in a float, but it'll
                                just get truncated. Kind of pointless to pass in a float, hm?. Oh, also don't pass in
                                a string obviously... thanks for being dynamically typed, Python...
                returns:        None

            - isEmpty():
                parameters:     None
                returns:        Boolean corresponding to if the stack is empty.
    
            - isFull():
                parameters:     None
                returns:        Boolean corresponding to if the stack is full.
            
            - getSize():
                parameters:     None
                returns:        Integer corresponding to if the current size of the stack.
            
            - clearStack():
                parameters:     None
                returns:        None. Clears the current stack of ALL elements.

            - peek():
                parameters:     None
                returns:        This returns the last element but does NOT pop it from the stack.
                
        """
    def __init__(self, *args, size = 100, warnings="Verbose"):
        self.stack = list(args)
        self.size = size
        self._errorMessages = [": You shouldn't be looping through a stack. Perhaps you would like to use an array?",
                              ": You shouldn't try to display the entire stack. Try using .peek(). However, here is your stack: \n",
                              ": You shouldn't be indexing a stack. Perhaps use .peek() to see the top element?",
                              ": Attempting to pop from an empty stack!",
                              ": Writing over stack data! Consider increasing the size by using .increaseSize()?",
                              ": Enter a value less than that of your current stack! Consider using .increaseSize()?",
                              ": Enter a value greater than that of your current stack! Consider using .decreaseSize()?",
                              "\033[31;1;4mWARNING\033[0m",
                              "\033[31;1;4mERROR\033[0m",
                              ": Something unexpected happened...",
                              "Can't index a stack.",
                              "Size given is less than current stack size.",
                              "Size given is greater than current stack size.",
                              ": Invalid operation!"]
        self._size = len(args)
        self._string = ""
        self._warnings = warnings.capitalize()

    def __iter__(self):
        yield self._errorMessages[7] + self._errorMessages[0]
        
    def __str__(self):
        self._string = ""
        if self._size == 0:
            if self._warnings == "Verbose":
                return self._errorMessages[7] + self._errorMessages[1] + "Empty stack."
            else:
                return "Empty stack."
        try:
            for i in range(self._size):
                if i < self._size - 1:
                    self._string += str(self.stack[i]) + " -> "
                else:
                    self._string += str(self.stack[i])
            if self._warnings == "Verbose":
                return self._errorMessages[7] + self._errorMessages[1] + self._string
            elif self._warnings == "Essential":
                return self._errorMessages[7] + self._errorMessages[13]
            else:
                return ""
        except TypeError:
            return self._errorMessages[8] + self._errorMessages[9]
        
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if self._warnings == "Verbose":
            return self._errorMessages[7] + self._errorMessages[2]
        elif self._warnings == "Essential":
            return self._errorMessages[10]
        else:
            return ""
    
    def pop(self):
        if len(self.stack) > 0:
                try:
                    self._size -= 1
                    return self.stack.pop()
                except:
                    print(self._errorMessages[8] + self._errorMessages[3])
        print(self._errorMessages[8] + self._errorMessages[3])
        return None
            
    def push(self, value):
        if len(self.stack) < self.size:
            self._size += 1
            self.stack.append(value)
        else:
            if self._warnings == "Verbose":
                print(self._errorMessages[7] + self._errorMessages[4])
            self.stack.pop(0)
            self.stack.append(value)

    def increaseSize(self, size):
        if size <= self.size:
            if self._warnings == "Verbose":
                print(self._errorMessages[7] + self._errorMessages[6])
            elif self._warnings == "Essential":
                print(self._errorMessages[11])

        else:
            self.size = size
    
    def decreaseSize(self, size):
        if size >= self.size:
            if self._warnings == "Verbose":
                print(self._errorMessages[7] + self._errorMessages[5])
            elif self._warnings == "Essential":
                print(self._errorMessages[12])
        else:
            self.size = size
    
    def isEmpty(self):
        return self._size == 0
    
    def isFull(self):
        return self._size == self.size
    
    def getSize(self):
        return self._size
    
    def clearStack(self):
        self._size = 0
        try:
            self.stack.clear()
        except:
            print(self._errorMessages[9])

    def peek(self):
        try:
            return self.stack[-1]
        except:
            return "Empty stack."

