def insert_after(self, val):
    currnent_next = self.next
    self.net = ListNode(val, self, current_next)
    if current_next:
        current_next.prev = self.next

def insert_before(self, val):
    current_prev = self.prev
    current_prev.next = self.prev

def delete(self):
    if self.prev:
        self.prev.next = self.next
    if self.next:
        self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

        def add_to_head(self, val):
            new_node = ListNode(val, None, self.head)
            if self.head:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node

        def remove_from_head(self):
            if not self.head:
                if not self.tail:
                    return None
                return self.remove_from_tail()
                else:
                    current_head = self.head
                    self.head = self.head.next
                    self.head.prev = None
                    return current_head.val

    def add_to_tail(self, val):
        if not self.tail:
            self.tail = ListNode(val, self.head, None)
        elif not self.head:
            self.head = self.tail
            self.tail  = ListNode(val, self.head, None)
            sself.head.next = self.tail


    def remove_from_tail(self):


    def move_to_front(self, node):


    def move_to_end(self, node):

        
