# Kaitlyn Forsberg - creates a tree with the nodes from Tree_Nodes(3).txt and creates the
# mirror of the tree as well. Each of these trees are printed, as well as information about
# the original tree. Python's OOP capabilities are used for this program. 

from timeit import default_timer as timer
import sys


# Create the tree

# global variables to create the tree

# level of the tree
treeDepth = 1
# counts the num of nodes on the left side
num_LeftNodes = 0
# counts the num of nodes on the right side of the tree
num_RightNodes = 0
# counts the total num of nodes
num_nodes = 0
# holds the value of the smallest node
smallest_counter = 0
# holds the value of the largest node
largest_counter = 0
# determines whether the nodes on the right side should be counted or not
start_RightCount = False
# holds the node that starts the right side of the tree (in this case it is "C")
start_RightSide = ""
# for printing the tree
spaces = "    "


class Node:

    def __init__(self, name):
        self.ID = name
        self.left = None
        self.right = None
        self.parent = None


# Function to create and label all of the nodes in the tree

def labelTree(treeNode):
    # statements below allow this function to alter the global variables
    global treeDepth
    global treeLoc
    global smallest_value
    global largest_value
    global num_nodes
    global num_LeftNodes
    global num_RightNodes
    global smallest_counter
    global largest_counter
    global start_RightCount
    global start_RightSide

    # count num of nodes
    num_nodes += 1

    # moves down one level in the tree
    treeDepth += 1  # we are now one level deeper in the tree

    # sets current location to parent and moves to the next node
    treeNode.parent = treeLoc  # set parent node to the previous node processed
    treeLoc = treeNode  # set the tree pointer node to the node passed to the function

    # prints out the tree based on the depth of each node.
    # nodes with greater depth will be spaced out farther
    if treeDepth == 2:
        print(treeDepth * spaces, treeNode.ID)
    elif treeDepth == 3:
        print(treeDepth * spaces, treeNode.ID)
    elif treeDepth == 4:
        print(treeDepth * spaces, treeNode.ID)
    elif treeDepth == 5:
        print(treeDepth * spaces, treeNode.ID)
    elif treeDepth == 6:
        print(treeDepth * spaces, treeNode.ID)

    # determines the smallest node value
    if treeLoc.ID < smallest_value:
        smallest_value = treeLoc.ID

    # determines the largest node value
    if treeLoc.ID > largest_value:
        largest_value = treeLoc.ID

    if treeDepth < 6 and (len(nodeNames) > 0):
        treeLoc.left = Node(nodeNames.pop(0))  # create left child

        if len(nodeNames) > 0:
            treeLoc.right = Node(nodeNames.pop(0))  # create right child

            start_RightSide = root.right.ID  # holds node that starts the right side ("C")

        # if the location is the start of the right side, then it will start counting how many
        # nodes are on the right side by making the below variable = True
        if treeLoc.ID == start_RightSide:
            start_RightCount = True

        # counts the num of nodes on the left and right side
        if start_RightCount is False and treeLoc.ID != root.ID:
            num_LeftNodes += 1
        elif start_RightCount is True:
            num_RightNodes += 1

        if treeLoc.left is not None:
            labelTree(treeLoc.left)  # process the left hand side using recursion
        if treeLoc.right is not None:
            labelTree(treeLoc.right)  # process the right hand side using recursion

    # counts the number of nodes on the left and right side for the nodes that do not
    # recurse (last depth level)
    if treeLoc.left is None and treeLoc.right is None:
        if start_RightCount is False:
            num_LeftNodes += 1
        elif start_RightCount is True:
            num_RightNodes += 1

    treeDepth -= 1  # we are now moving one level up in the tree when we return
    treeLoc = treeLoc.parent  # done with this set of children, reset current tree pointer to parent node

    return


# create global variables for create_mirror function

# holds the depth level of the mirror tree
mirror_TreeDepth = 1
# holds the nodes to be printed in order
print_MirrorImage = []


# pass in the first node
def create_mirror(mirror_TreeNode):
    # statements allow the global variables above to be altered
    global mirror_TreeLoc
    global mirror_TreeDepth
    global print_MirrorImage

    # increment through the level of the tree
    mirror_TreeDepth += 1

    # sets the current node to be the parent and moves onto the next node
    mirror_TreeNode.parent = mirror_TreeLoc
    mirror_TreeLoc = mirror_TreeNode

    if mirror_TreeDepth < 6 and (len(mirror_NodeNames) > 0):
        mirror_TreeLoc.right = Node(mirror_NodeNames.pop(0))  # create right children first

        if len(mirror_NodeNames) > 0:
            mirror_TreeLoc.left = Node(mirror_NodeNames.pop(0))  # create left child

        if mirror_TreeLoc.right is not None:
            create_mirror(mirror_TreeLoc.right)  # process the right hand side using recursion
        if mirror_TreeLoc.left is not None:
            create_mirror(mirror_TreeLoc.left)  # process the left hand side using recursion

    # appends each node to the list below and separates the nodes by spaces based upon
    # its depth in the tree. The list of nodes is initially in reverse order
    print_MirrorImage.append(((mirror_TreeDepth*spaces) + mirror_TreeNode.ID))

    # once the list contains all of the nodes from the file, reverse the list then print the nodes
    if len(print_MirrorImage) == size:
        print_MirrorImage.reverse()
        for node in print_MirrorImage:
            print(node)

    mirror_TreeDepth -= 1  # we are now moving one level up in the tree when we return
    mirror_TreeLoc = mirror_TreeLoc.parent  # done with this set of children, reset current tree pointer to parent node

    return


# start timer
start = timer()

# Parse the node name file and load the names into a list

if len(sys.argv) != 2:
    raise ValueError('Please provide a file name.')

sys.argv[0] = sys.argv[0][0:len(sys.argv[0]) - sys.argv[0][::-1].find('/')]

inputFile1 = sys.argv[0] + sys.argv[1]

print("\nThe file that will be used for input is {0}".format(sys.argv[1]))

# adjusted per announcement
infile1 = open(sys.argv[1], "r")

nodeNames = infile1.readline().rstrip().split()

#
# Create root node of tree
#


# global variables to be used in the functions above
mirror_NodeNames = nodeNames.copy()

# intializes the smallest and largest values to be the first node initially
smallest_value = nodeNames[0]
largest_value = nodeNames[0]
# size -> number of nodes
size = len(nodeNames)
root = Node(nodeNames.pop(0))
# initializes the tree's current location to be the root ("A")
treeLoc = root

mirror_root = Node(mirror_NodeNames.pop(0))
# initializes the mirrored tree's current location to be the root
mirror_TreeLoc = mirror_root


#
# Create the rest of tree and label each of the nodes
#

print("\nBuilding the tree:\n")
labelTree(root)
print("\nBuilding mirror image of the tree:\n")
create_mirror(root)
print(f"\n**********************"
      f"\n***** Statistics *****"
      f"\n**********************"
      f"\nNumber of Nodes: {num_nodes}"
      f"\nNumber of Nodes On Left Side: {num_LeftNodes}"
      f"\nNumber of Nodes On Right Side: {num_RightNodes}"
      f"\nSmallest Node Value: {smallest_value}"
      f"\nLargest Node Value: {largest_value}")

end = timer()
print("\nTime: ", end-start)
