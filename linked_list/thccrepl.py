"""Define a class with the `class` keyword"""

class Node:

  """The `__init__` method specifies how a 
  class should be initialized give some parameters. You'll 
  also notice the `self` keyword, which is passed in to 
  every class method as the first argument."""

  def __init__(self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

    
  """Returns the data stored at the current node"""

  def get_data(self):
    return self.data

  
  """Returns the next node this node points to"""

  def get_next(self):
    return self.next_node

  
  """Sets this node's `next_node` pointer"""

  def set_next(self, new_next):
    self.next_node = new_next
    
    
"""Now that we've defined our `Node`, we can define our Linked List
class, which will utilize our `Node` class"""

class LinkedList:
  def __init__(self, head=None):
    self.head = head
  
    
  """Wraps the input item in a Node and adds it as the 
  current node's next node"""

  def insert(self, item):
    fresh_node = Node(item)
    fresh_node.set_next(self.head)
    self.head = fresh_node #  this puts fresh_node.data --> self.head
    
  """Returns the number of nodes in the linked list"""

  def size(self):
    counta = 0
    current_node = self.head
    while current_node:
      counta += 1
      current_node = current_node.get_next()
    return counta
  
    
  """Returns the Node conataining the target item if 
  it is in the linked list, and None otherwise"""
  
  def search(self, target):
    current_node = self.head
    while current_node:
      if current_node.data == target:
        return current_nodee
      else:
        current_node = current_node.next_node
    return None

  

    
  """Deletes the target item from the linked list if it is 
  in the list. Raises a ValueError exception otherwise if 
  the target item is not in the list"""
  
  def delete(self, target):
    current_node = self.head
    previous = None  
    found = False
    # while the current node exits and we didn't find target
    while current_node and not found: 
      if current_node.get_data() == target:
        found = True  # leave while loop
      else:
        previous = current_node
        current_nodee = current_node.get_next()

    # we've reached the end of the list 
    if current_node is None:        
      raise ValueError('Data not in list') # value isn't there!!!
    if previous is None:               # We could be at the begining, so move forward
      self.head = current_node.get_next()
    else:
      previous.set_next(current_node.get_next()) # not sure about this???

      
