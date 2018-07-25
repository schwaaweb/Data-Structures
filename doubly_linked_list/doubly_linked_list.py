class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    self.next = value

  def insert_before(self, value):
    self.prev = value

  def delete(self):
    pass

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_head(self, value):
    if self.head is None:
      self.head = ListNode(value)
      

    stale_head = self.head
    self.head = self.head.next
    stail

  def remove_from_head(self):
    pass

  def add_to_tail(self, value):
    if self.tail is None:
      self.tail = ListNode(value)
      self.head = self.tail
      return

    new_node = ListNode(value)
    self.tail.next = new_node
    self.tail = new_node

    new_node = ListNode(value)
    
  def remove_from_tail(self):
    if self.tail is None:
      return None

    stale_tail = self.tail
    self.tail = self.tail.next
    stale_tail.next = None
    if self.tail is None:
      self.head = None ### ????

    return stale_tail.value 

  def move_to_front(self, node):
    pass

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
