import sys
sys.path.append('..')

from my_queue import Queue

# Setup
q = Queue(1)
q.enqueue(3)

# Test peek
# Should be 1
assert (q.peek() == 1), "Failed in q.peek()"

# Test dequeue
# Should be 1
assert (q.dequeue() == 1), "Failed in q.dequeue()"

# Test enqueue
q.enqueue(4)
# Should be 3
assert (q.dequeue() == 3), "Failed in q.dequeue()"
# Should be 4
assert (q.dequeue() == 4), "Failed in q.dequeue()"
q.enqueue(5)
# Should be 5
assert (q.peek() == 5), "Failed in q.peek()"

print ("ALL TEST PASSED")
