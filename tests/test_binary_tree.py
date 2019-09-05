import sys
sys.path.append('..')

from binary_tree import BinaryTree
from binary_tree import Node

# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
assert (tree.search(4) == True), "Failed in tree.search"
# Should be False
assert (tree.search(6) == False), "Failed in tree.search"

# Test print_tree
# Should be 1-2-4-5-3
assert (tree.print_tree() == "1-2-4-5-3"), "Failed in print_tree"

print ("ALL TEST PASSED")
