class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_min(root):
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left

    return current.val

if __name__ == "__main__":

    values = [0, -5, 10, -12, 3]
    root = None
    
    for val in values:
        root = insert(root, val)

    min_value = find_min(root)

    print(f"Знайдений мінімум: {min_value}")

    print(f"Мінімум для порожнього дерева: {find_min(None)}")