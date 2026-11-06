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

def find_sum(root):
    if root is None:
        return 0
    
    return root.val + find_sum(root.left) + find_sum(root.right)

if __name__ == "__main__":

    values = [0, -5, 10, -12, 3]
    root = None
    
    for val in values:
        root = insert(root, val)

    total_sum = find_sum(root)
    
    print(f"Знайдена сума: {total_sum}")