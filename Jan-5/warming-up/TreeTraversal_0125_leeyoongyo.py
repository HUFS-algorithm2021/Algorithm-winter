#BOJ 1991 트리순회 leeyoongyo

class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def preorder(node):  # 노드와 자손 노드를 preorder로 방문하면서 출력
    print(node.key, end="")
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])

def inorder(node):  # 노드와 자손 노드를 inorder로 방문하면서 출력
    if node.left != '.':
        inorder(tree[node.left])
    print(node.key, end="")
    if node.right != '.':
        inorder(tree[node.right])

def postorder(node):  # 노드와 자손 노드를 postorder로 방문하면서 출력
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.key, end="")

n = int(input())
tree = {}
for i in range(n):
    data = input().split()
    tree[data[0]] = Node(key=data[0],left=data[1],right=data[2])
#root : 'A'
preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])

