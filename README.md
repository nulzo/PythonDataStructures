# Common Data Structures in Python 🐍

Well, I have needed some of these previously, so I have begun to just build them out myself. I'll continually keep adding more as I find the time to write them (that is, if I can have some time between my university courses) ;^).

##


### Stack
The *esteemed* structure... The humble stack. Remember LIFO? Well, now you can use it in Python. I don't care that you can "*implement a stack yourself*". You really want to do that everytime you try to use solve a simple problem?
"*Oh, I can just use list\[-1\] everytime I want to treat an array like a stack*", yeah well I can also use a chainsaw to cut my steak, but that doesn't make it a dinner knife, does it?
###
Joking aside, this is a simple data strucure. One of, if not **THE** simplest structure. Why do you think I did it first? ;^)
###
##
### Queue
This is the stacks more formal relative. So sophisticated and civilized, the queue really thinks that just because you're the first in you should also be the first out?! Well... actually... I guess that would be useful when you
want to keep track of priority... or if you want to process things in sequential order... or if you want to... nevermind, I think you get the point. Oh, and don't even think for a second that you can just use an array like a
queue. I mean, you totally can (it's actually what it is in my library 💀). BUT, if you use *MY* queue, you can only do queue operations. Two words: That's freaking **EPIC**. Hm, that's not two words? Ok, get in the *queue* of people
who have told me I'm wrong... you'll just have to wait your turn! ;^)
###
This structure is just like a stack, but FIFO instead of LIFO. That's pretty much it. Later on we can talk about priority queues, but we'll get there eventually!
##
### Linked List

#### An Aside About Recursion
Okay, take a deep breath. It's about to get serious. Well, if you know recursion, then it's not really serious and you can skip this part. However, if you are just hearing this strange word ***"recursion"*** for the first time, then allow me to briefly write it out for you:

<p align="center">
<img src="https://imgur.com/IXNIdqj.png"  width="60%" height="30%">
</p>

Simple, right? I'm just kidding. I wrote that out in LaTeX to mess with you. It's the principle of recursive definition, but let me try to give you a human-understandable version. Try to imagine you're working piecewise functions again (the ones where the function changes based on the state of whatever you plug into the function).
Well, that is *kind of* like recursion, we just need to solve for the formula we are currently looking at. Still confused? Not a problem. Imagine you are trying to solve for a factorial (in this example, we'll say 5!). Well, to know 5! then we obviously need to know 5 * 4!, and to know 4! we need to solve 4 * 3!. This is getting too much to type out
right here, but let me write it out in LaTeX so it's easier to see. 

<p align="center">
<img src="https://imgur.com/zqk7ywS.png"  width="30%" height="10%">
</p>
 
Okay! How is that? Let's go over it. Recall that "||" just means "or" (I'm a programmer, not a math-magician)! We can pretty clearly see the recursive nature of this function. IF we have an *n* of 0 or 1, we can just return 1, otherwise we have to call the function again using *n-1* until we reach our base case of 
n == 1 or n ==0 . Pretty cool, right? In code (I'll just use Python since that is what this repo is written with), we could write the recursive function as:

```python
def factorial(n):
  if n < 0:
      print("Don't want to code up negative values ;^)!")
  elif 0 <= n <= 1:
      return 1
  else:
      return n * factorial(n-1)
```
Go ahead and try that out in your own IDE! Debug it if you want to watch the recursion take place. If you understand what this function is doing then you will be in good shape going into this section of the repository. From this point on, I'll start using recursion quite extensively, so buckle up!
###
#### Back to Linked Lists
This is just a simple singly-linked list. Maybe I'll add a doubly-linked list if I have time, but I doubt it. Linked lists are a magnet for interview questions, it's like companies only care about linked lists... The benefits of linked list?
Well... They are non-contiguous memory I guess? Other than that... 🤷‍♂️. Good to know conceptually for trees, though.
What is a tree? Well, linked lists are a seed in your mind for these structures called trees - no pun intended! Let's discuss them further in later sections. For now, I think you deserve a break! 

##

### Erm... 

I haven't added any more structures yet... I plan on adding BSTs, B+ Trees, AVL trees, Undirected Graphs, Directed Graphs, Directed Acyclic Graphs, Hash Tables, Heaps, and perhaps some sorting algorithms like Merge Sort and Quick Sort.
