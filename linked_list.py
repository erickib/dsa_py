""" An object for storing a single node of a linked list """
class Node:

    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data
    
""" Single linked list """
class LinkedList:
    def __init__(self):
        self.head = None
    def is_empty(self):
        return self.head == None
    
    """ Returns the number of nodes in the list. Takes O(n) time """
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node

        return count
    
    """ Adds new Node containing data at head of the list. Takes O(1) time """
    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    """ Inserts a new Node containing data at index position
        Insertion takes O(1) time but finding the node at the
        insertion point taes O(n) time.
        Takes overall O(n) time """
    def insert(self, data, index):
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node

    """ removes node containing data that matches the key. 
        Returns the node or None if key doesn't exist
        Takes O(n) time """
    def remove(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

    """ Search for the first node containing data that matches the key. Takes O(n) time """
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                print("if: ", current.data, key)
                return current
            else:
                print("else: ", current, key)
                current = current.next_node
        return None

    """ Returns a string representation of the list. Takes O(n) time """
    def __repr__(self):
        
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node 
        
        return '-> '.join(nodes)
    