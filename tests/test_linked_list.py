import sys
sys.path.append('..')

from linked_list import Element
from linked_list import LinkedList

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
assert (ll.head.next.next.value == 3), "Failed in next.value"
# Should also print 3
assert (ll.get_position(3).value == 3), "Failed get_position"

# Test insert
ll.insert(e4, 3)
# Should print 4 now
assert (ll.get_position(3).value == 4), "Failed get_position after insert"

# Test delete
ll.delete(1)
# Should print 2 now
assert (ll.get_position(1).value == 2), "Failed get_position after delete"
# Should print 4 now
assert (ll.get_position(2).value == 4), "Failed get_position after delete"
# Should print 3 now
assert (ll.get_position(3).value == 3), "Failed get_position after delete"

print ("ALL TEST PASSED")
