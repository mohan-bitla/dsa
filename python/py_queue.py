from node import Node
from list_comprehensive import ListComprehensive

class PyQueue(ListComprehensive):
  def __init__(self):
    self.node = None
    self.first = None
    self.last = None

  def is_empty(self):
    return self.first == None
  
  def push(self, item):
    old_node = self.last
    node = Node()
    node.next = None
    node.item = item
    self.last = node
    if self.first == None:
      self.first = self.last
    else:
      old_node.next = self.last 

  def pop(self):
    item = self.first.item
    self.first = self.first.next
    return item


if __name__ == "__main__":
  # test the queue(FIFO)
  # TODO: need to add iterator support
  q = PyQueue()
  print(q.is_empty())
  q.push("Hi")
  print(q.first.item)
  q.push("Hello")
  print(q.first.next.item)
  q.push("How are you")
  print(q.first.next.next.item)
  for s in q:
    print(s)