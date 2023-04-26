# import main
# import owntree
# import secondtree
#
# first_tree = owntree.tree
# second_tree = secondtree.tree
# print(first_tree)


# class LengthNode:
#     def __init__(self, data):
#         self.data = data
#         self.user_db:list = []
#         self.sorted_db = []
#         self.get_ord = None
#         self.left = None
#         self.right = None
# test = LengthNode(5)



# def getData(node):
#     while True:
#         user = input('enter name')
#         node.user_db.append(user)
#         print(node.user_db)
#         ask = input('enter e to exit')
#         if ask == 'e':
#             break
#         else:
#             continue
#
# getData(test)
#
#
# # Sorted Third Tree
# def sorted_third_tree(node):
#     for i in range(len(node.user_db)):
#         get_ord = 0
#         for j in range(len(node.user_db[i])):
#             get_ord += ord(node.user_db[i][j])
#         # node.sorted_db.append(get_ord)
#         update_sorted = sorted(node.sorted_db)
#     # print(node.sorted_db)
#     print(update_sorted)
#
# sorted_third_tree(test)
