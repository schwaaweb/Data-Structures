

class LinkedList:
  def __init__(self, head=None):
    self.head = head
    
  """Wraps the input item in a Node and adds it as the 
  current node's next node"""
  def insert(self, item):
    new_node = Node(item)
    new_node.set_next(self.head)
    self.head = new_node
    
  """Returns the number of nodes in the linked list"""
  def size(self):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current.get_next()
    return count
    
  """Returns the target item if it is in the linked list,
  and None otherwise"""
  def search(self, target):
    current = self.head
    while current:
      if current.data == target:
        return current
      current = current.next_node
    return None
    
  """Deletes the target item from the linked list if it is 
  in the list. Raises a ValueError exception otherwise if 
  the target item is not in the list"""
  def delete(self, target):
    current = self.head
    previous = None
    found = False
    while current and not found:
      if current.get_data() == target:
        found = True
      else:
        previous = current
        current = current.get_next()
    if current is None:
      raise ValueError('Data not in list')
    if previous is None:
      self.head = current.get_next()
    else:
      previous.set_next(current.get_next())
      
