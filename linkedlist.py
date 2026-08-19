class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def__init(self):
    self.head=None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insert_at_end(self, data):
        new node =node(data)
        if self.head is none:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node