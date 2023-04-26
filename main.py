import owntree
import secondtree

# get first tree and second tree from previous file
first_tree = owntree.tree
second_tree = secondtree.tree


class LengthNode:
    def __init__(self, data):
        self.data = data
        self.user_db: list = []
        self.sorted_db = []
        self.get_ord = None
        self.index = None
        self.left = None
        self.right = None


lengthNode = LengthNode(5)


# find connection between user name with first own tree
def connection_test(ftree, name):
    if ftree is not None:
        connection_test(ftree.left, name)
        if ftree.data == name[0]:
            sec_tree_con_test(second_tree, len(name), name)
            return
        connection_test(ftree.right, name)


# find connection between user input with second tree length
def sec_tree_con_test(sec_tree, length, name):
    if sec_tree is not None:
        sec_tree_con_test(sec_tree.left, length, name)
        if sec_tree.data == length:
            sec_tree.second_data = name
            print("we found for third three", len(sec_tree.second_data), second_tree.second_data)

            checkLengthToInsert(lengthNode, name, first_tree)

            return
        sec_tree_con_test(sec_tree.right, length, name)


# Insert data into node that has lenght 5 function
def checkLengthToInsert(node, name, ftree):
    if node is not None:
        if node.data == len(name) and name[0] == ftree.data:
            node.user_db.append(name)
        print('here insertion complete', node.user_db)


# print result function
def printing(node):
    if node is not None:
        printing(node.left)
        if node.second_data is not None:
            print(node.second_data)
        printing(node.right)


# Sorted Third Tree
def sorted_third_tree(node):
    for i in range(len(node.user_db)):
        get_ord = 0
        for j in range(len(node.user_db[i])):
            get_ord += ord(node.user_db[i][j])
        node.sorted_db.append(get_ord)
    print(node.sorted_db)


# Sorting Function -- insertion
def sorting_fun(node):
    for i in range(1, len(node.sorted_db)):
        value = node.sorted_db[i]

        j = i - 1
        while j >= 0 and value < node.sorted_db[j]:
            node.sorted_db[j + 1] = node.sorted_db[j]
            j = j - 1
            node.sorted_db[j + 1] = value
    print('here is sorted list', node.sorted_db)


def search(sorted_db, target):
    start = 0
    end = len(sorted_db) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if sorted_db[mid] > target:
            end = mid - 1

        elif sorted_db[mid] < target:
            start = mid + 1

        else:
            return mid
    return -1


# main function
def getUserName():
    while True:
        name = input('Enter gmail')
        new_length = len(name) - 10
        update_name = name[0:new_length]
        # print('update name', update_name, len(update_name))

        connection_test(first_tree, update_name)

        ask = input('enter e to exit')
        if ask == 'e':
            sorted_third_tree(lengthNode)
            sorting_fun(lengthNode)
            break

        print(search(lengthNode.sorted_db, 533))


def transferUserData():
    return lengthNode.user_db

def transferSortedData():
    return lengthNode.sorted_db

def transferIndex():
    return search(lengthNode.sorted_db, 533)
# print(getUserName())


#
# search_key = input('enter search key')
# if search_key in lengthNode.user_db:
#     print('search key is ', search_key)
# else:
#     print('not found')