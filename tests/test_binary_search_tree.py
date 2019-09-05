import sys
sys.path.append('..')

from binary_search_tree import BST

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
assert (tree.search(4) == True), "Failed in tree.search"
# Should be False
assert (tree.search(6) == False), "Failed in tree.search"

print ("ALL TEST PASSED")
