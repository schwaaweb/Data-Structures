"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    if self.tail is None:
        self.tail = Node(value)
        self.head = self.tail
        return

    new_node = Node(value)
    self.tail.next_node = new_node
    self.tail = new_node
     
    

  def remove_head(self):
    if self.head is None:
      return None

    stale_head = self.head
    self.head = self.head.next_node
    stale_head.next_node = None
    if self.head is None:
      self.tail = None

    return stale_head.value

  def contains(self, value):
    current_node = self.head
    while current_node is not None:
      if current_node.value == value:
        return True
      else:
        current_node = current_node.next_node
    return False

  def get_max(self):
    if self.head is None:
      return None
    
    current_node = self.head
    maximum = current_node.value
    while current_node is not None:
      if current_node.get_value() > maximum:
        maximum = max(current_node.value, maximum)
        current_node = current_node.next_node
      else:
        current_node = current_node.next_node
    return maximum

  
        
