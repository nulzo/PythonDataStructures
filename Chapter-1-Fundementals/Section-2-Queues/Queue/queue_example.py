from Queue.queue_structure import Queue

# +========================[ queue Example ]=========================+

queue = Queue(size=5)

queue.enqueue(20)
queue.enqueue(30)

print(f"I can see that the element at the front of the queue is {queue.peek()}!")
top_element = queue.dequeue()
print(f"I have dequeueped {top_element} from the queue and now the front element is {queue.peek()}!")

top_element = queue.dequeue()
queue_length = queue.getSize()

print(f"Uh oh... I dequeueped {top_element} and now my queue size is now {queue_length}!")
print("If I dequeue from my queue, something bad might happen. Let's test it out...\n")

top_element = queue.dequeue()

print("\nWow! It knew I couldn't remove any more elements!")
print("Now let's add a LOT of elements to my queue (more than the space I have allocated).")

queue.enqueue(2)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(8)
queue.enqueue(9)

print(f"\nOk. I added 5 elements. If I add one more I'll go over the size limit of {queue.size}... I wonder what will happen?\n")

queue.enqueue(10)

print(f"\nOh, wow. It won't let me add anymore! Let me increase the size like it says!")

queue.increaseSize(10)

print(f"Ok, I increased my size to {queue.size}... let's try that again!")

queue.enqueue(2)

print(f"\nAwesome, no warnings! It must've added it!")
print(f"These queues are awesome! Let me print out my entire queue to see what is in it!\n")

print(queue)

print(f"\nOh, I had no idea you shouldn't display the whole queue!")
print(f"Well, maybe I am supposed to simply loop through the queue? Let me try that out!\n")

for element in queue:
    print(element)

print(f"\nOh, jeez! So I shouldn't loop through a queue OR try to display the whole queue...")
print(f"I guess I *should* just stick with enqueue(), dequeue(), and peek() methods!")
print(f"Well, let's clear this queue then!\n")

queue.clearQueue()

print(f"Looks like the length of my queue is now {queue.getSize()}. It really did clear it!")
print("I can't wait to use my newfound understanding of queues... Think of all the things I can do with them!\n")



