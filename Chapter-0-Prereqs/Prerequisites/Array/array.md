# Introduction to Arrays (lists)
From a language agnostic standpoint, an array is any collection of elements that are of fixed size. Generally speaking, 
arrays are *contiguous* in memory (that is, the elements are "next to" one another in memory, similar to organizing items on a shelf where each item is right next to the other). 
In the context of Python specifically, we use the term `List` instead of `Array`, but the properties are somewhat similar. 
A list is a versatile data structure that we can use to store items. We call the items in the array the `Elements`, and 
the location of the `elements` in the list is called the `index`. 

In Python, lists are defined by square brackets `[]` and can contain elements of different data types, including numbers,
strings, or even other lists. So, we can have a list of strings and integers together, which lends to the power of these 
containers. Lists in Python are zero-indexed, meaning the first element is accessed with index 0, the second with index
1, and so on.

### Mutability
Lists are *mutable* data structures. This means that
a list can be changed during runtime, and the elements stored within (or their indexes) are not fixed. Unlike some data 
types that are immutable (cannot be changed), lists allow modifications such as adding, removing, or updating elements 
without creating a new list.

For example, if we have a list of numbers `[1, 2, 3]`, you can change it to `[1, 4, 3]` by modifying the second element. 
This dynamic nature makes lists mutable and a versatile choice for situations where you need to alter the collection 
of elements during the course of your program. 

### Dimensionality

Dimensionality refers to the number of indices or levels of organization needed to uniquely identify an element within a 
data structure. In the context of lists in Python, dimensionality indicates the level of nesting or hierarchy within the 
structure. You can think of a 1-D list as a single line of elements. You access each element by specifying its position in that line 
with a single index. A 2-D list can be thought of as a grid or a table. Each element is like a cell in the grid, and to 
access an element, you need two indices - one for the row and one for the column. A 3-D list can be thought of as a cube 
or a stack of 2D grids. Each element is located at a specific point in this cube, and to access an element, you need 
three indices - one for the depth, one for the row, and one for the column. In this course, we won't extend further than 3-D.

### Initializing Lists

In Python, lists can be initialized in several different ways. As mentioned above, we can use square brackets to initialize it.
We can also use the function `list()` to initialize an empty array. Both of these will create a list object which we can then
use to perform our operations on. Several examples are shown below

#### **Empty List**

```python
# Initialize with square brackets
some_list = []
# Initialize with function call
another_list = list()
```

#### **List with Elements**

```python
# A list of integers
numbers = [1, 2, 3, 4, 5]
# A list of strings
names = ["Python", "Is", "Fun"]
# A list of mixed types (int, string, float, bool)
mixed_list = [1, "string", 3.14159, False]
```

#### **Using the `list()` Constructor**

```python
# Construct via a single element
single_element = list("hello")
# Construct from another iterable container
multiples_elements = list(("This", "is", "tuple"))
```

### Common Methods

#### **`append()`:**

This method will add an element to the *end* of the list.

```python
# Initialize a list of [1, 2, 4]
some_list = [1, 2, 4]
# Append 6 to the list to produce [1, 2, 4, 6]
some_list.append(6)
```

#### **`extend()`:**
Appends the elements of another iterable (say, another list) to the end of the current list.

```python
some_list = [4, 5]
# Extend list to produce [4, 5, [6, 7, 8]]
some_list.extend([6, 7, 8])
```

#### **`insert()`:**

Add an element at a specified position within the list. 
It modifies the original list and shifts the existing elements to accommodate the new one.

 ```python
some_list = [4, 5, 6]
# Insert 99 at index 2, producing [4, 5, 99, 6]
some_list.insert(2, 99) 
 ```

#### **`remove()`:**

Removes the first occurrence of a specified value.

```python
some_list = [4, 3, 6]
# Removes the first occurrence of 3
some_list.remove(3) 
```

#### **`pop()`:**

Removes and returns the element at the specified index. If no index is provided, removes and returns the last element.

```python
some_list = [4, 3, 6]
# Removes and returns the element at index -1 (which is 6)
popped_value = some_list.pop()  
```

#### **`index()`:**

Returns the index of the first occurrence of a specified value.

```python
some_list = [4, 3, 6]
# Returns the index of the first occurrence of 4 (which is 0)
idx = some_list.index(4)
```

