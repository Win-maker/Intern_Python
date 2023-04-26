class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

main_tree_data = []
for i in range(97, 123):
    main_tree_data.append(chr(i))

def insertion(character, root_tree:Node):
    if root_tree is None:
        return Node(character)
    if ord(character) < ord(root_tree.data):
        root_tree.left = insertion(character, root_tree.left)
    else:
        root_tree.right = insertion(character, root_tree.right)
    return root_tree

def printing(node):
    if node is not None:
        printing(node.left)
        print(node.data)
        printing(node.right)

length = len(main_tree_data)
mid = int(length / 2)
tree = Node('m')

first_part = main_tree_data[0: mid-1]
second_part = main_tree_data[mid:length]

first_part.reverse()
for i in range(len(first_part)):
    tree = insertion(first_part[i], tree)

for i in range(len(second_part)):
    tree = insertion(second_part[i], tree)
