class Node:
    def __init__(self, data):
        self.data = data
        self.second_data = None
        self.left:Node = None
        self.right:Node = None

# number main tree data
main_tree_data = []
for i in range(1, 26):
    main_tree_data.append(i)

# insertion function
def insertion(number, tree:Node):
    if tree is None:
        return Node(number)
    if number < tree.data:
        tree.left = insertion(number, tree.left)
    else:
        tree.right = insertion(number, tree.right)

    return tree

# printing node
def printing(node):
    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)


lenght = len(main_tree_data)
mid = int(lenght / 2)

first_part = main_tree_data[0: mid]
second_part = main_tree_data[mid+1: lenght]

tree = Node(4)

first_part.reverse()

for i in range(len(first_part)):
    tree = insertion(first_part[i], tree)

for i in range(len(second_part)):
    tree = insertion(second_part[i], tree)

# printing(tree)