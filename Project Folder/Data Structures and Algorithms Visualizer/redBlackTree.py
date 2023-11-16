import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import random

class RedBlackTree:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.value = value
            self.color = 'red'
            self.left = None
            self.right = None
            self.parent = None

    def insert(self, value):
        node = self.Node(value)
        if self.root is None:
            self.root = node
            self.root.color = 'black'
        else:
            self._insert_helper(self.root, node)
        self._fix_violations(node)

    def _insert_helper(self, parent, node):
        if node.value < parent.value:
            if parent.left is None:
                parent.left = node
                node.parent = parent
            else:
                self._insert_helper(parent.left, node)
        else:
            if parent.right is None:
                parent.right = node
                node.parent = parent
            else:
                self._insert_helper(parent.right, node)

    def _fix_violations(self, node):
        while node.parent is not None and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._rotate_left(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == 'red':
                    node.parent.color = 'black'
                    uncle.color = 'black'
                    node.parent.parent.color = 'red'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._rotate_right(node)
                    node.parent.color = 'black'
                    node.parent.parent.color = 'red'
                    self._rotate_left(node.parent.parent)

        self.root.color = 'black'

    def delete(self, value):
        node = self._search(value)
        if node is None:
            return
        if node.left is not None and node.right is not None:
            successor = self._minimum(node.right)
            node.value = successor.value
            node = successor
        if node.left is not None:
            child = node.left
        else:
            child = node.right
        if node.color == 'black':
            node.color = child.color
            self._delete_fixup(node)
        self._transplant(node, child)

    def _delete_fixup(self, node):
        while node != self.root and (node is None or node.color == 'black'):
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self._rotate_left(node.parent)
                    sibling = node.parent.right
                if (sibling.left is None or sibling.left.color == 'black') and \
                        (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                                sibling = node.parent.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self._rotate_left(node.parent)
                    sibling = node.parent.right
                if (sibling.left is None or sibling.left.color == 'black') and \
                        (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    node = node.parent
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                        if sibling.left is not None:
                            sibling.left.color = 'black'
                        sibling.color = 'red'
                        self._rotate_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = 'black'
                    if sibling.right is not None:
                        sibling.right.color = 'black'
                    self._rotate_left(node.parent)
                    node = self.root

    def _transplant(self, node1, node2):
        if node1.parent is None:
            self.root = node2
        elif node1 == node1.parent.left:
            node1.parent.left = node2
        else:
            node1.parent.right = node2
        if node2 is not None:
            node2.parent = node1.parent

    def _rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def _rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _search(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None

    def visualize(self):
        G = nx.Graph()
        self._build_graph(self.root, G)
        pos = nx.spring_layout(G)
        node_colors = [node[1]['color'] for node in G.nodes(data=True)]
        nx.draw_networkx(G, pos, node_color=node_colors, node_size=800, font_size=10, font_color='white')
        plt.axis('off')
        plt.show()

    def _build_graph(self, node, G, label_count=[0]):
        if node is not None:
            label = str(label_count[0])
            label_count[0] += 1
            G.add_node(label, value=node.value, color=node.color)
            if node.left is not None:
                self._build_graph(node.left, G, label_count)
                G.add_edge(label, str(label_count[0] - 1))
            if node.right is not None:
                self._build_graph(node.right, G, label_count)
                G.add_edge(label, str(label_count[0] - 1))
    
    def _build_graph(self, node, G):
        if node is not None:
            G.add_node(node.value, color=node.color)
            if node.left is not None:
                G.add_edge(node.value, node.left.value)
                self._build_graph(node.left, G)
            if node.right is not None:
                G.add_edge(node.value, node.right.value)
                self._build_graph(node.right, G)


def main():
    tree = RedBlackTree()

    # Create the tree by hand
    tree.root = tree.Node(19)
    tree.root.color = 'black'

    node2 = tree.Node(16)
    node2.color = 'red'
    node3 = tree.Node(15)
    node3.color = 'black'
    node4 = tree.Node(17)
    node4.color = 'black'
    node5 = tree.Node(24)
    node5.color = 'black'
    node6 = tree.Node(20)
    node6.color = 'red'
    node7 = tree.Node(28)
    node7.color = 'red'
    

    tree.root.left = node2
    node2.parent = tree.root
    tree.root.right = node5
    node5.parent = tree.root

    node2.left = node3
    node3.parent = node2
    node2.right = node4
    node4.parent = node2

    node5.left = node6
    node6.parent = node5
    node5.right = node7
    node7.parent = node5


    # Visualize the tree
    tree.visualize()

    # Interact with the tree
    while True:
        print("\nSelect an operation:")
        print("1. Insert a node")
        print("2. Delete a node")
        print("3. Visualize the tree")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            value = int(input("Enter the value to insert: "))
            tree.insert(value)
        elif choice == '2':
            value = int(input("Enter the value to delete: "))
            tree.delete(value)
        elif choice == '3':
            tree.visualize()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()