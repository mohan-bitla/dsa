class ListComprehensive:
  def __iter__(self):
    return self
  
  def __next__(self):
    if self.first is None:
      raise StopIteration
    else:
      return self.pop()