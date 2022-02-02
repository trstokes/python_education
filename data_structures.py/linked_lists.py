# defining our node class (object)
class Node: 

    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return self.data 

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next 

class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head 
        self.tail = tail 

    def __repr__(self):
        node = self.head 
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next_node
        nodes.append('None')
        return ' -> '.join(nodes)

    def insert_head(self, data):
        
        # define a new node 
        new_node = Node(data)

        # set second node to equal the old first one 
        new_node.set_next(self.head)

        # the new head will be the new node 
        self.head = new_node 

llist = LinkedList()

print(llist)

first_node = Node('a')
llist.head = first_node
print(llist)