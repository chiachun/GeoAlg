from tree import node, tree, right_rotate, left_rotate
from copy import deepcopy

# Construct a test tree
t = tree()

# Using a list
t.fromlist([17,13,11,12,15,10,8,16,22,33,99,100,105])
t.traverse_and_print()

# Find height of the whole tree
h1= t.find_height_recursion(t.get_root(),0)
print "original height", h1


    
parent, branch, imbalanced_node = t.search(99)
new_node = left_rotate(imbalanced_node)

if branch =='l':
    parent.l = new_node
elif branch =='r':
    parent.r = new_node

layer = t.traverse_and_print()
h2 = t.find_height_recursion(t.get_root(),0)
print "height after rotation", h2
