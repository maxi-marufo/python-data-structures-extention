import sys
sys.path.append('..')

from linked_list import Element
from stack import Stack

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
assert (stack.pop().value == 3), "Failed in stack.pop()"
assert (stack.pop().value == 2), "Failed in stack.pop()"
assert (stack.pop().value == 1), "Failed in stack.pop()"
assert (stack.pop() is None), "Failed in stack.pop()"
stack.push(e4)
assert (stack.pop().value == 4), "Failed in stack.pop()"

print ("ALL TEST PASSED")
