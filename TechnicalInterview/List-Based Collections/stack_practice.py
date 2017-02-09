"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList and return it"
        first = self.head
        if first is not None:
            self.head = self.head.next
        return first

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        top = self.ll.delete_first()
        return top

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Test LinkedList functionality
ll = LinkedList(e1)
assert ll.head.value == 1
ll.insert_first(e2)
assert ll.head.value == 2
assert ll.head.next.value == 1
ll.insert_first(e3)
assert ll.head.value == 3

assert ll.delete_first().value == 3
assert ll.delete_first().value == 2
assert ll.delete_first().value == 1

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)

assert stack.pop().value == 3
assert stack.pop().value == 2
assert stack.pop().value == 1
assert stack.pop() is None
stack.push(e4)
assert stack.pop().value == 4
