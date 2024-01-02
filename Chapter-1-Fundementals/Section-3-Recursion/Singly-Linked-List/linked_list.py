class Node:

    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self):
        self.root = None
        self.size = 0

    def __str__(self):
        return self.__showList()

    def __iter__(self):
        head = self.root
        while head != None:
            yield head.value
            head = head.next

    def __setitem__(self, index, value):
        node = self.root
        self.__updateNodeByIndex(node, index, value)

    def __getitem__(self, index):
        return self.__getAtIndex(self.root, index)
    
    def __len__(self):
        return self.size
    
    def __del__(self):
        return

    def __addNodeAtEnd(self, node, value):
        if node.next == None:
            node.next = Node(value)
            return
        else:
            self.__addNodeAtEnd(node.next, value)

    def __getAtIndex(self, node, index, count=0):
        if node == None:
            raise SystemExit(f"IndexError: Index {index} out of bounds with size {self.size}.")
        elif count == index:
            return node.value
        else:
            return self.__getAtIndex(node.next, index, count + 1)
        
    def __deleteNextNode(self, node):
        nodeToDelete = node.next
        node.next = nodeToDelete.next
        self.size -= 1

    def __deleteHead(self, node):
        self.root = node.next
        self.size -= 1
        
    def __deleteNodeAtIndex(self, node, index, count=1):
        if node.next == None:
            raise SystemExit(f"IndexError: Element to be deleted is not within the list.")
        elif count == index:
            self.__deleteNextNode(node)
        else:
            self.__deleteNodeAtIndex(node.next, index, count + 1)

    def __deleteNodeByValue(self, node, value):
        if node.next == None:
            raise SystemExit(f"IndexError: Element to be deleted is not within the list.")
        elif value == node.next.value:
            self.__deleteNextNode(node)
        else:
            self.__deleteNodeByValue(node.next, value)

    def __updateNodeByIndex(self, node, index, value, count = 0):
        if node == None:
            raise SystemExit(f"IndexError: Element to be deleted is not within the list.")
        elif count == index:
            node.value = value
        else:
            self.__updateNodeByIndex(node.next, index, value, count + 1)
        
    def __showList(self):
        if self.root == None:
            return "[ ]"
        string = "[ "
        head = self.root
        while head.next != None:
            string += str(head.value) + ", "
            head = head.next
        string += str(head.value) + " ]"
        return string

    def addNodeAtEnd(self, value):
        if self.root == None:
            self.root = Node(value)
        node = self.root
        self.size += 1
        self.__addNodeAtEnd(node, value)

    def getAtIndex(self, index):
        if self.root == None:
            raise SystemExit(f"IndexError: Index {index} out of bounds with size {self.size}.")
        node = self.root
        t = self.__getAtIndex(node, index)
        return t

    def addNodesInOrder(self, *args):
        itemsToAdd = list(args)
        while len(itemsToAdd) > 0:
            self.addNodeAtEnd(itemsToAdd[0])
            itemsToAdd.pop(0)

    def addNodeAtBeginning(self, value):
        node = Node(value, self.root)
        self.size += 1
        self.root = node

    def deleteNodeAtIndex(self, index):
        if self.root == None:
            raise SystemExit(f"Erm: You are trying to delete a node from an empty list...")
        node = self.root
        self.__deleteNodeAtIndex(node, index)

    def deleteNodeByValue(self, value):
        if self.root == None:
            raise SystemExit(f"Erm: You are trying to delete a node from an empty list...")
        node = self.root
        if node.value == value:
            self.__deleteHead(node)
        else:
            self.__deleteNodeByValue(node, value)    
