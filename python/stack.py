from list_comprehensive import ListComprehensive
from node import Node

class Stack(ListComprehensive):

  def __init__(self):
    self.first = Node()

  def push(self, item):
    old_node = self.first
    node = Node()
    node.item = item
    node.next = old_node
    self.first = node

  def pop(self):
    item = self.first.item
    self.first = self.first.next
    return item

  def is_empty(self):
    return self.first == None


if __name__ == "__main__":
  # test the stack(LIFO)
  # TODO: need to add iterator support
  stack = Stack()
  print(stack.is_empty())
  print(stack.first.item)
  stack.push("Hi")
  print(stack.first.item)
  stack.push("Hello")
  print(stack.first.item)
  stack.push("How are you")
  print(stack.first.item)
  for s in stack:
    print(s)