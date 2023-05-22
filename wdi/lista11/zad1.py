class TreeItem:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

#zad2
def get_items_at_level(t):
    if t == None:
        return 0
    return get_items_at_level(t.left) + get_items_at_level(t.right) + 1


tree = TreeItem(1)
tree.left = TreeItem(2)
tree.right = TreeItem(3)
tree.left.left = TreeItem(4)
tree.left.right = TreeItem(5)
tree.right.right = TreeItem(7)
tree.left.left.left = TreeItem(8)
tree.left.left.left.left = TreeItem(9)
print(get_items_at_level(tree))

#zad3
def get_tree_height(t):
    if t == None:
        return 0
    return max(get_tree_height(t.left) + 1, get_tree_height(t.right) + 1)

print(get_tree_height(tree))

#zad5
tree_bst = TreeItem(10)
tree_bst.left = TreeItem(4)
tree_bst.right = TreeItem(12)
tree_bst.left.left = TreeItem(2)
tree_bst.left.right = TreeItem(24)
tree_bst.right.left = TreeItem(7)
tree_bst.right.right = TreeItem(16)


def check_if_bst(t):
    if t.left == None and t.right == None:
        return True
    if t.left == None and t.right.val > t.val:
        return True
    if t.left.val < t.val and t.right == None:
        return True
    if t.left.val >= t.val or t.right.val <= t.val:
        return False
    return check_if_bst(t.left) and check_if_bst(t.right)

print(check_if_bst(tree))
print(check_if_bst(tree_bst))

#zad7
def add_item(t, val):
    while t.left != None:
        t = t.left
    t.left = TreeItem(val)
