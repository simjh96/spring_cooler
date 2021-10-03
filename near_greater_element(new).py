# # successer 구현하다가 포기 ㅠㅠ
#
# # 출처: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
# # Python code to insert a node in AVL tree
#
# # Generic tree node class
# class TreeNode(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.height = 1
#
#
# # AVL tree class which supports the
# # Insert operation
# class AVL_Tree(object):
#     self.found = None
#
#     def insert(self, root, key):
#         if not root:
#             return TreeNode(key)
#         elif key < root.val:
#             root.left = self.insert(root.left, key)
#         else:
#             root.right = self.insert(root.right, key)
#         root.height = 1 + max(self.getHeight(root.left),
#                               self.getHeight(root.right))
#         balance = self.getBalance(root)
#         if balance > 1 and key < root.left.val:
#             return self.rightRotate(root)
#         if balance < -1 and key > root.right.val:
#             return self.leftRotate(root)
#         if balance > 1 and key > root.left.val:
#             root.left = self.leftRotate(root.left)
#             return self.rightRotate(root)
#         if balance < -1 and key < root.right.val:
#             root.right = self.rightRotate(root.right)
#             return self.leftRotate(root)
#         return root
#
#     def find(self, root, key):
#         if key < root.val:
#             if root.left:
#                 self.find(root.left, key)
#             else:
#
#         else:
#             if root.right:
#                 self.find(root.right, key)
#
#     def leftRotate(self, z):
#         y = z.right
#         T2 = y.left
#         y.left = z
#         z.right = T2
#         z.height = 1 + max(self.getHeight(z.left),
#                            self.getHeight(z.right))
#         y.height = 1 + max(self.getHeight(y.left),
#                            self.getHeight(y.right))
#         return y
#
#     def rightRotate(self, z):
#         y = z.left
#         T3 = y.right
#         y.right = z
#         z.left = T3
#         z.height = 1 + max(self.getHeight(z.left),
#                            self.getHeight(z.right))
#         y.height = 1 + max(self.getHeight(y.left),
#                            self.getHeight(y.right))
#         return y
#
#     def getHeight(self, root):
#         if not root:
#             return 0
#         return root.height
#
#     def getBalance(self, root):
#         if not root:
#             return 0
#         return self.getHeight(root.left) - self.getHeight(root.right)
#
#     def preOrder(self, root):
#         if not root:
#             return
#         print("{0} ".format(root.val), end="")
#         self.preOrder(root.left)
#         self.preOrder(root.right)
#
#
# # Driver program to test above function
# myTree = AVL_Tree()
# root = None
#
# root = myTree.insert(root, 10)
# root = myTree.insert(root, 20)
# root = myTree.insert(root, 30)
# root = myTree.insert(root, 40)
# root = myTree.insert(root, 50)
# root = myTree.insert(root, 25)
#
#
# def nge(i, reversed_list: 'shared', result: 'shared', great_wall=-1, comp_tree: AVL_Tree = None, root=None, comp_set=None):
#     # if param == none
#     if comp_tree is None:
#         comp_tree = AVL_Tree()
#     if comp_set is None:
#         comp_set = set()
#
#     # if great_wall:
#     #     nge(new_avl_tree, new comp_set)
#     if reversed_list[i] >= great_wall:
#         result.append(-1)
#         great_wall = reversed_list[i]
#         nge(i+1, reversed_list, result, great_wall)
#
#     # elif i < i - 1:
#     #     if i - 1 in comp_set
#     #         result에만 append
#     #     else
#     #         result와 comp_set 그리고 avl tree에도 insert
#     #     nge(그대로)
#     elif reversed_list[i] < reversed_list[i - 1]:
#         if reversed_list[i - 1] in comp_set:
#             result.append(reversed_list[i - 1])
#         else:
#             result.append(reversed_list[i - 1])
#             comp_set.add(reversed_list[i - 1])
#             # 메모리 문제 없나? outer scope 에 다른 root들 안지워 질텐데...
#             root = comp_tree.insert(root, reversed_list[i - 1])
#         nge(i + 1, reversed_list, result, great_wall, comp_tree, root, comp_set)
#
#     # else
#     #     avl_tree.find
#     #     result.append
#     #     nge(그대로)
#     else:
#         result.append(comp_tree.find(root, reversed_list[i]))
#         nge(i + 1, reversed_list, result, great_wall, comp_tree, root, comp_set)
#
