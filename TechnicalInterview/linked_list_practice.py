"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        i = 1
        if position < 1:
            return None
        current = self.head
        while i < position:
            if current.next is None:
                return None
            current = current.next
            i += 1
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        i = 1
        if position > 1:
            current = self.head
            while i < position:
                if i == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                i += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next

        if current.value == value:
            if previous is None:
                self.head = current.next
            else:
                previous.next = current.next


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
assert ll.head.next.next.value == 3
# Should also print 3
assert ll.get_position(3).value == 3
assert ll.get_position(1).value == 1
assert ll.get_position(2).value == 2
assert ll.get_position(4) is None

# Test insert
ll.insert(e4, 3)
# Should print 4 now
assert ll.get_position(1).value == 1
assert ll.get_position(2).value == 2
assert ll.get_position(3).value == 4
assert ll.get_position(4).value == 3

# Test delete
ll.delete(1)
# Should print 2 now
assert ll.get_position(1).value == 2
# Should print 4 now
assert ll.get_position(2).value == 4
# Should print 3 now
assert ll.get_position(3).value == 3

ll.delete(4)
assert ll.get_position(1).value == 2
assert ll.get_position(2).value == 3
